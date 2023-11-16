from django.shortcuts import render
from django.http import HttpResponse
import base64
from PIL import Image
from io import BytesIO

from .models import Student, Teacher, Course, CourseSchedule, Enrollment
from .face_rec import face_rec, pil_to_cv2

def index(request):
    return HttpResponse("Hello, world. You're at the manager index.")

def details(request, course_id):
    return HttpResponse("You are looking at the details of course %s." % course_id)

# def schedule(request):
    # get the logged in student

    # update later
    
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        image_data = request.POST.get('photo')
        format, imgstr = image_data.split(';base64,') 
        image = Image.open(BytesIO(base64.b64decode(imgstr)))

        # 在这里处理用户名和照片
        # 例如，保存照片，验证用户名等
        student_name = face_rec(pil_to_cv2(image))

        # 打印用户名和识别出的学生名字
        print(f"Username: {username}, Recognized as: {student_name}")

        return HttpResponse(f"Username: {username}, Recognized as: {student_name}, Photo received.")

    return render(request, 'login.html')
