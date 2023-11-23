
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

tokenizer = AutoTokenizer.from_pretrained('facebook/contriever')
model = AutoModel.from_pretrained('facebook/contriever')

def mean_pooling(token_embeddings, mask):
    token_embeddings = token_embeddings.masked_fill(~mask[..., None].bool(), 0.)
    sentence_embeddings = token_embeddings.sum(dim=1) / mask.sum(dim=1)[..., None]
    return sentence_embeddings

embeddings_dict = {}
def init():
    global embeddings_dict

    print("Initializing related courses...")

    # 从数据库获取所有课程的信息及其ID
    courses = Course.objects.filter(course_information__isnull=False)
    course_infos = [course.course_information for course in courses]

    # 检查课程信息是否为空
    if not course_infos:
        print("No course information found.")
        return

    # 应用分词器
    inputs = tokenizer(course_infos, padding=True, truncation=True, return_tensors='pt')

    # 计算token嵌入
    with torch.no_grad():
        outputs = model(**inputs)

    # 计算句子嵌入
    embeddings = mean_pooling(outputs[0], inputs['attention_mask'])

    # 将course_id与对应的嵌入关联起来
    embeddings_dict = {course.course_id: embedding for course, embedding in zip(courses, embeddings)}

    print("Now is init on relared courses")
    # Here is test code
    print(get_related_courseID("030833"))

init()

if __name__ == "__main__":
    pass