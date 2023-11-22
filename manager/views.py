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

"""
TODO

remove_course

logout_button

"""


def add_course(request, course_id):
    # authenticate the student
    if request.session.get('authentication', None) is None:
        return redirect('/manager/login')
    
    if request.method == 'POST':
        student_id = request.session['authentication']
        # assuming the student's username is used as the student_id

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
    return render(request, 'course1_information.html', {'course': course})
    
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

        # for testing
        # student_name = "3035844077" 
        try:
            student = Student.objects.get(name = student_name)
            request.session['authentication'] = student_name
        except:
            return HttpResponse("Student not found")
        
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
    # authenticate the student
    if request.session.get('authentication', None) is None:
        return redirect('/manager/login')

    student_id = request.session['authentication']
    # 如果验证成功，继续处理
    Enrollments = Enrollment.objects.filter(student = student_id)
    #print(Enrollments.values_list('course', flat=True))
    Enrolled_courses = Course.objects.filter(course_id__in = Enrollments.values_list('course'))
    #print(Enrolled_courses.values_list('course_id', flat=True))
    Sessions = CourseSchedule.objects.filter(course__in = Enrolled_courses)
    Sessions = Sessions.order_by("start_time")
    #print(Sessions.values_list('course', flat=True))

    # getting the events that will happen in an hour
    current_time = timezone.now()-timedelta(hours=2)#for testing only
    one_hour_later = current_time + timedelta(hours=1)

    current_weekday = current_time.weekday()
    next_weekday = (current_weekday + 1) % 7

    SessionIn1H = Sessions.filter(Q(weekday=current_weekday, start_time__range = (current_time.time(), one_hour_later.time())) | Q(weekday=next_weekday, start_time__lte=one_hour_later.time()))
    student_name=Student.objects.get(name=student_id).usrname
    
    if SessionIn1H.exists():
        context = {"student_name": student_name, "sessions1h": SessionIn1H, "current_time":current_weekday}#test only
        return render(request, "curriculum.html", context)
    else:
        course_schedule = []
        time_ranges_str = ['9:30-10:20', '10:30-11:20', '11:30-12:20', '12:30-13:20','13:30-14:20','14:30-15:20','15:30-16:20','16:30-17:20','17:30-18:20','18:30-19:20']
        time_ranges = []
        for time_range in time_ranges_str:
            time_range = time_range.split('-')
            time_range = [datetime.strptime(time, '%H:%M').time() for time in time_range]
            time_range = (time_range[0], time_range[1])
            time_ranges.append(time_range)
        
        days = [0,1,2,3,4,5,6]
        for day in days:
            course_schedule.append([])
        for course in Sessions:
            # Assuming the course has fields 'start_time' and 'end_time' representing the course duration
            start_time = course.start_time
            end_time = course.end_time

            day = course.weekday
            #print(day, start_time, end_time)
            # Create a list to store the time range for each day
            #if day not in course_schedule:
            #    course_schedule[day] = []
            # print(day, start_time, end_time, course.course.course_name)
            # Add the course name and time range to the corresponding day
            course_schedule[day].append((course.get_weekday_display(),course.start_time, end_time, course.course.course_name))
        for day in days:
            for schedule in course_schedule[day]:
                print(schedule)
        context = {"student_name": student_name,'course_schedule': course_schedule,'time_ranges': time_ranges, 'days': days}
        return render(request, "schedule.html",context)
    #return HttpResponse(f"Curriculum for student ID: {student_id}")
