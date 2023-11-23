
import torch
from transformers import AutoTokenizer, AutoModel
from .models import Course


from scipy.spatial.distance import cosine

def get_related_courseID(course_id):
    try:
        curr_course_embedding = embeddings_dict[course_id].numpy()
    except KeyError:
        return "Course ID not found in embeddings."
    # print(course_id)

    similarities = {}
    for other_course_id, other_embedding in embeddings_dict.items():
        if other_course_id != course_id:
            # 计算余弦相似度
            similarity = 1 - cosine(curr_course_embedding, other_embedding.numpy())
            similarities[other_course_id] = similarity

    # 对结果按相似度进行排序，并取前三个
    related_courses = sorted(similarities, key=similarities.get, reverse=True)[:3]
    
    # print(related_courses)
    return related_courses

def mean_pooling(token_embeddings, mask):
    token_embeddings = token_embeddings.masked_fill(~mask[..., None].bool(), 0.)
    sentence_embeddings = token_embeddings.sum(dim=1) / mask.sum(dim=1)[..., None]
    return sentence_embeddings

embeddings_dict = {}

import pickle
import os
EMBEDDINGS_FILE = 'course_embeddings.pkl'

def init():
    global embeddings_dict

    print("Initializing related courses...")

    # 检查是否已存在嵌入缓存
    if os.path.exists(EMBEDDINGS_FILE):
        with open(EMBEDDINGS_FILE, 'rb') as file:
            embeddings_dict = pickle.load(file)
        print("Loaded embeddings from cache.")
    else:
        tokenizer = AutoTokenizer.from_pretrained('facebook/contriever')
        model = AutoModel.from_pretrained('facebook/contriever')
        courses = Course.objects.all()
        course_infos = [course.course_information for course in courses if course.course_information]

        if not course_infos:
            print("No course information found.")
            return

        inputs = tokenizer(course_infos, padding=True, truncation=True, return_tensors='pt')
        with torch.no_grad():
            outputs = model(**inputs)

        embeddings = mean_pooling(outputs[0], inputs['attention_mask'])
        embeddings_dict = {course.course_id: embedding for course, embedding in zip(courses, embeddings)}

        # 保存嵌入到文件
        with open(EMBEDDINGS_FILE, 'wb') as file:
            pickle.dump(embeddings_dict, file)

        print("Embeddings generated and saved.")

    # 测试代码
    print(get_related_courseID("030833"))

init()

if __name__ == "__main__":
    pass