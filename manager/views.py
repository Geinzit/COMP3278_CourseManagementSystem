from django.shortcuts import render, redirect, get_object_or_404
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

def add_course(request, course_id):
    if request.method == 'POST':
        student_id = request.user.name  # assuming the student's username is used as the student_id

        # Get the student and course objects
        student = get_object_or_404(Student, name=student_id)
        course = get_object_or_404(Course, course_id=course_id)

        # Check if the enrollment already exists
        if Enrollment.objects.filter(course=course, student=student).exists():
            return HttpResponse("You are already enrolled in this course.")

        # Create a new enrollment object
        enrollment = Enrollment(course=course, student=student)
        enrollment.save()

        return redirect('/manager')  # Redirect to the curriculum page after enrollment

def index(request):
    now = timezone.now()
    courses = Course.objects.all()
    schedule = CourseSchedule.objects.all()
    processed_courses = []
    for course in courses:
        print(course)
        course_schedules = schedule.filter(course=course)
        for course_schedule in course_schedules:
            print(course.course_name, course_schedule.weekday, course_schedule.start_time, course_schedule.end_time)
            processed_courses.append({
                'course_id': course.course_id,
                'course_name': course.course_name,
                'weekday': course_schedule.get_weekday_display(),
                'start_time': course_schedule.start_time,
                'end_time': course_schedule.end_time,
                'teacher': course.teacher,
                'description': course.description,
            })
    return render(request, 'index.html', {'course_list': processed_courses})
   
def course(request, course_id):
    course = Course.objects.get(course_id = course_id)
    course_schedules = CourseSchedule.objects.filter(course = course_id)
    context = {"course":course, "course_schedules":course_schedules}
    return render(request, "course.html", context)
    
def teacher(request, teacher_id):
    teacher = Teacher.objects.get(id=teacher_id)
    return render(request, 'teacher.html', {'teacher': teacher})

    
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

        # database check required here

        return redirect(f'/manager/curriculum/?student_id={student_name}')

    return render(request, 'login.html')


def course_detail(request, course_id):
    # 构造响应字符串
    response_content = f"This is course {course_id}"
    # 从数据库中获取课程信息
    course = Course.objects.get(course_id=course_id)
    # 使用模板渲染课程信息
    return render(request, 'course1_information.html', {'course': course})
    # 返回响应
    return HttpResponse(response_content)


def curriculum(request):
    # http://127.0.0.1:8000/manager/curriculum/?student_id=123
    def is_valid_student(student_id):
        return True
    
    # 获取查询参数 student_id
    student_id = request.GET.get('student_id', None)

    # 这里实现你的验证逻辑
    if not student_id or not is_valid_student(student_id):
        # 如果验证失败，可以重定向或返回错误信息
        return HttpResponse("Invalid or missing student ID", status=400)

    # 如果验证成功，继续处理
    Enrollments = Enrollment.objects.filter(student = student_id)
    Enrolled_courses = Course.objects.filter(course_id__in = Enrollments)
    
    Sessions = CourseSchedule.objects.filter(course__in = Enrolled_courses)
    Sessions = Sessions.order_by("start_time")

    # getting the events that will happen in an hour
    current_time = timezone.now()
    one_hour_later = current_time + timedelta(hours=1)

    current_weekday = current_time.weekday()
    next_weekday = (current_weekday + 1) % 7

    SessionIn1H = Sessions.filter(Q(weekday=current_weekday, start_time__range = (current_time.time(), one_hour_later.time())) | Q(weekday=next_weekday, start_time__lte=one_hour_later.time()))
    student_name=Student.objects.get(name=student_id).usrname
    
    if SessionIn1H.exists():
        context = {"student_name": student_name, "sessions1h": SessionIn1H}
        return render(request, "curriculum.html", context)
    else:
        course_schedule = {}
        time_ranges = ['9:30-10:20', '10:30-11:20', '11:30-12:20', '12:30-13:20', '13:30-14:20','13:30-14:20','14:30-15:20','15:30-16:20','16:30-17:20','17:30-18:20','18:30-19:20']
        days = [0,1,2,3,4,5,6]

        for course in Sessions:
            # Assuming the course has fields 'start_time' and 'end_time' representing the course duration
            start_time = course.start_time
            end_time = course.end_time

            day = course.weekday

            # Create a list to store the time range for each day
            if day not in course_schedule:
                course_schedule[day] = []

            # Add the course name and time range to the corresponding day
            course_schedule[day].append((start_time, end_time))

        context = {"student_name": student_name,'course_schedule': course_schedule,'time_ranges': time_ranges, 'days': days}
        return render(request, "schedule.html",context)
    #return HttpResponse(f"Curriculum for student ID: {student_id}")
