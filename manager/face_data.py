import os
import numpy as np
from PIL import Image
import cv2
import pickle

def capture_data(user_name = "Jack", NUM_IMGS = 400):
    video_capture = cv2.VideoCapture(0)
    # 创建存储图像的目录
    data_dir = f'data/data/{user_name}'
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    cnt = 1
    font = cv2.FONT_HERSHEY_SIMPLEX
    bottomLeftCornerOfText = (10, 50)
    fontScale = 1
    fontColor = (102, 102, 225)
    lineType = 2

    while cnt <= NUM_IMGS:
        # 捕捉帧
        ret, frame = video_capture.read()
        # 可选：在图像上显示一些文本信息
        msg = f"Capturing {user_name}'s Face Data [{cnt}/{NUM_IMGS}]"
        cv2.putText(frame, msg, bottomLeftCornerOfText, font, fontScale, fontColor, lineType)
        # 显示图像
        cv2.imshow('Video', frame)
        # 保存图像
        cv2.imwrite(f"{data_dir}/{user_name}{cnt:03d}.jpg", frame)
        cnt += 1
        # 按'q'退出
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # 释放摄像头和关闭所有窗口
    video_capture.release()
    cv2.destroyAllWindows()

def train_model(img_dir, model_dir):
    face_cascade = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')
    recognizer = cv2.face.LBPHFaceRecognizer_create()

    current_id = 0
    label_ids = {}
    y_labels = []
    x_train = []

    for root, dirs, files in os.walk(img_dir):
        for file in files:
            if file.endswith("png") or file.endswith("jpg"):
                path = os.path.join(root, file)
                label = os.path.basename(root).replace(" ", "").upper()
                if label not in label_ids:
                    label_ids[label] = current_id
                    current_id += 1

                id_ = label_ids[label]
                pil_image = Image.open(path).convert("L")  # convert to grayscale
                image_array = np.array(pil_image, "uint8")
                faces = face_cascade.detectMultiScale(image_array, scaleFactor=1.5, minNeighbors=5)

                for (x, y, w, h) in faces:
                    roi = image_array[y:y+h, x:x+w]
                    x_train.append(roi)
                    y_labels.append(id_)

    with open(os.path.join(model_dir, "labels.pickle"), "wb") as f:
        pickle.dump(label_ids, f)

    recognizer.train(x_train, np.array(y_labels))
    recognizer.save(os.path.join(model_dir, "train.yml"))

if __name__ == "__main__":
    # capture_data(user_name="Zhiheng Lyu")
    train_model("data/data", "data")