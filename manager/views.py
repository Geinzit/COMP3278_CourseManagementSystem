from django.shortcuts import render
from django.http import HttpResponse
import base64
from PIL import Image
from io import BytesIO

from .models import Student, Teacher, Course, CourseSchedule, Enrollment

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
        print(username)

        return HttpResponse(f"Username: {username}, Photo received.")

    return render(request, 'login.html')
