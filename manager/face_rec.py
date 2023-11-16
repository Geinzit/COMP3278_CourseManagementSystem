import cv2
import pickle
import numpy as np

def pil_to_cv2(pil_image):
    open_cv_image = np.array(pil_image) 
    # Convert RGB to BGR 
    open_cv_image = open_cv_image[:, :, ::-1].copy() 
    return open_cv_image

curr_dir = "/Users/lvzhiheng/COMP3278_CourseManagementSystem/manager/"

def load_recognizer_and_labels():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read(f"{curr_dir}data/train.yml")

    with open(f"{curr_dir}data/labels.pickle", "rb") as f:
        labels = pickle.load(f)
        labels = {v: k for k, v in labels.items()}

    return recognizer, labels

def face_rec(img):
    # Input: image
    # Output: name of student
    recognizer, labels = load_recognizer_and_labels()
    face_cascade = cv2.CascadeClassifier(f"{curr_dir}data/haarcascade_frontalface_default.xml")

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)

    for (x, y, w, h) in faces:
        roi_gray = gray[y:y + h, x:x + w]
        id_, conf = recognizer.predict(roi_gray)
        print(conf)
        if conf >= 0.001:
            return labels[id_]
        else:
            return "Unknown"

    return "No Face Found"

if __name__ == "__main__":
    img_path = "/Users/lvzhiheng/COMP3278_CourseManagementSystem/manager/data/data/Jack/Jack277.jpg"
    # TODO: finish the test code'
    img = cv2.imread(img_path)
    name = face_rec(img)
    print(f"Recognized: {name}")