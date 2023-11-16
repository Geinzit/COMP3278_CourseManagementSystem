from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
from django.utils import timezone
from datetime import datetime, timedelta
from .models import Student, Teacher, Course, CourseSchedule, Enrollment

import base64
from PIL import Image
from io import BytesIO

from .models import Student, Teacher, Course, CourseSchedule, Enrollment
from .face_rec import face_rec, pil_to_cv2

def index(request):
    student_name = "3035844077" # subject_to_change
    Enrollments = Enrollment.objects.filter(student = student_name)
    Enrolled_courses = Course.objects.filter(course_id__in = Enrollments)
    
    Events = CourseSchedule.objects.filter(course__in = Enrolled_courses)
    Events = Events.order_by("start_time")

    # getting the events that will happen in an hour
    current_time = timezone.now()
    one_hour_later = current_time + timedelta(hours=1)

    current_weekday = current_time.weekday()
    next_weekday = (current_weekday + 1) % 7

    EventsIn1H = Events.filter(Q(weekday=current_weekday, start_time__range = (current_time.time(), one_hour_later.time())) | Q(weekday=next_weekday, start_time__lte=one_hour_later.time()))

    
    context = {"enrolled_classes": Enrolled_courses, "events": Events, "events1h": EventsIn1H}
    return render(request, "manager/index.html", context)
    
#def add_course(request):
   # if request.method == "POST":
        

def details(request, course_id):
    return HttpResponse("You are looking at the details of course %s." % course_id)

    
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
