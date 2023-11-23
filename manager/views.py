from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.db.models import Q
from django.utils import timezone
from django.core.mail import send_mail
from django.http import HttpResponse
from django.contrib import messages

from datetime import datetime, timedelta
from .models import Student, Teacher, Course, CourseSchedule, Enrollment, Login

import base64
from PIL import Image
from io import BytesIO

from .models import Student, Teacher, Course, CourseSchedule, Enrollment
from .face_rec import face_rec, pil_to_cv2

def send_email(request):
    if(request.session.get('authentication', None) is None):
        return redirect('/manager/login')
    if(request.method == 'POST'):
        student_id = request.session['authentication']
        Sessions, SessionIn1H = getSessions(student_id)
        subject = "Reminder: You have classes in 1 hour"
        
        message = ""
        for session in SessionIn1H:
            print(session)
            message += f"Course: {session.course.course_name} - {session.course.description}\nTime: {session.start_time} - {session.end_time}\nVenue: {session.classroom_address} \n"

        # enter the email address you wish to send from
        from_email = "your-email-address"
        recipient_list = [Student.objects.get(name = request.session['authentication']).email]

        # clear messages
        list(messages.get_messages(request))
        
        try:
            send_mail(subject, message, from_email, recipient_list)
            messages.success(request, f"Email sent successfully")
        except Exception as e:
            messages.error(request, f"Error sending email: {str(e)}")

        return redirect('/manager/curriculum')
            
def remove_course(request, course_id):
    if request.session.get('authentication', None) is None:
        return redirect('/manager/login')

    if request.method == 'POST':
        student_id = request.session['authentication']

        # Get the student and course objects
        student = get_object_or_404(Student, name=student_id)
        course = get_object_or_404(Course, course_id=course_id)

        # Check if the enrollment exists
        if not Enrollment.objects.filter(course=course, student=student).exists():
            messages.error(request,"You are not enrolled in this course.")
            return redirect('/manager/course/'+str(course_id)) 

        # Delete the enrollment object
        enrollment = Enrollment.objects.get(course=course, student=student)
        enrollment.delete()
        messages.success(request,"Successfully dropped.")
        return redirect('/manager/course/'+str(course_id)) 

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
            messages.error(request,"You are already enrolled in this course.")
            return redirect('/manager/course/'+str(course_id)) 


        Enrollments = Enrollment.objects.filter(student = student_id)
        Enrolled_courses = Course.objects.filter(course_id__in = Enrollments.values_list('course'))
        courseToEnroll = CourseSchedule.objects.filter(course=course_id)
        for courses in courseToEnroll:
            weekday=courses.weekday
            start = courses.start_time
            end = courses.end_time
            Sessions = CourseSchedule.objects.filter(course__in = Enrolled_courses, weekday=weekday)
            conflicts = Sessions.filter(Q(start_time__range = (start, end))|Q(end_time__range = (start, end)))            
            if conflicts.exists():
                for conflict in conflicts:
                    course_name=conflict.course.course_name
                messages.error(request,"Time Conflict! Please drop the other courses first: "+course_name)
                return redirect('/manager/course/'+str(course_id)) 
        # Create a new enrollment object
        enrollment = Enrollment(course=course, student=student)
        enrollment.save()

        messages.success(request,"Successfully enrolled.")
        return redirect('/manager/course/'+str(course_id)) 
        #return redirect('/manager')  # Redirect to the curriculum page after enrollment

def index(request):
    now = timezone.now()
    courses = Course.objects.all()
    return render(request, 'index.html', {'course_list': courses})
    return render(request, 'index.html', {'course_list': courses})
   
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
        try:
            username = request.POST.get('username')
            image_data = request.POST.get('photo')
            format, imgstr = image_data.split(';base64,') 
            image = Image.open(BytesIO(base64.b64decode(imgstr)))

            # 在这里处理用户名和照片
            # 例如，保存照片，验证用户名等
            student_id = face_rec(pil_to_cv2(image))
        except:
            return HttpResponse("No photo taken!")
        # 打印用户名和识别出的学生名字
        print(f"Username: {username}, Recognized as: {student_id}")

        # for testing
        # student_id = "3035844077"
        try:
            student = Student.objects.get(name = student_id)
            if username != student_id:
                return HttpResponse("Incorrect Username")
            request.session['authentication'] = student_id
            #record login time
            student.login_time = timezone.localtime(timezone.now())
            student.save()
        
        except:
            return HttpResponse("Student not found")

        
        return redirect(f'/manager/curriculum/?student_id={student_id}')

    return render(request, 'login.html')

def login_history(request):
    if request.session.get('authentication', None) is None:
        return redirect('/manager/login')

    login_filter = Login.objects.filter(student = request.session['authentication'])
    records = []

    for record in login_filter:
        deltatime = (record.logout_time - record.login_time)
        deltatime = f"{deltatime.seconds // 3600} hours, {(deltatime.seconds // 60) % 60} minutes, {deltatime.seconds % 60} seconds"
        records.append((record.login_time.strftime("%Y-%m-%d %H:%M:%S"), record.logout_time.strftime("%Y-%m-%d %H:%M:%S"), deltatime))
    return render(request, 'login_history.html', {'records': records})

def logout(request):
    if request.session.get('authentication', None) is None:
        return redirect('/manager/login')
    
    student = Student.objects.get(name = request.session['authentication'])
    record = Login(login_time = student.login_time, logout_time = timezone.localtime(timezone.now()), student = student)

    record.save()
    
    request.session.flush()
    return redirect('/manager/login')

def course_detail(request, course_id):
    # 构造响应字符串
    response_content = f"This is course {course_id}"
    # 从数据库中获取课程信息
    course = Course.objects.get(course_id=course_id)
    # 使用模板渲染课程信息
    return render(request, 'course1_information.html', {'course': course})
    # 返回响应
    return HttpResponse(response_content)

def getSessions(student_id):
    Enrollments = Enrollment.objects.filter(student = student_id)
    # print(Enrollments.values_list('course', flat=True))
    Enrolled_courses = Course.objects.filter(course_id__in = Enrollments.values_list('course'))
    # print(Enrolled_courses.values_list('course_id', flat=True))
    Sessions = CourseSchedule.objects.filter(course__in = Enrolled_courses)
    Sessions = Sessions.order_by("start_time")

    # getting the events that will happen in an hour
    current_time = timezone.localtime(timezone.now())
    one_hour_later = current_time + timedelta(hours=1)

    current_weekday = current_time.weekday()
    next_weekday = (current_weekday + 1) % 7

    SessionIn1H = Sessions.filter(Q(weekday=current_weekday, start_time__range = (current_time.time(), one_hour_later.time())))
    return Sessions, SessionIn1H

def curriculum(request):
    # http://127.0.0.1:8000/manager/curriculum/?student_id=123
    # authenticate the student
    if request.session.get('authentication', None) is None:
        return redirect('/manager/login')

    student_id = request.session['authentication']
    student = Student.objects.get(name=student_id)
    login_time = timezone.localtime(student.login_time).strftime("%Y-%m-%d %H:%M:%S")
    student_name=student.usrname
    
    Sessions, SessionIn1H = getSessions(student_id)
    
    if SessionIn1H.exists():
        context = {"student_name": student_name, "sessions1h": SessionIn1H, "login_time": login_time}
        return render(request, "curriculum.html", context)
    else:
        return redirect(f'/manager/schedule')
    
def schedule(request):
    if request.session.get('authentication', None) is None:
        return redirect('/manager/login')

    student_id = request.session['authentication']
    student = Student.objects.get(name=student_id)
    login_time = timezone.localtime(student.login_time).strftime("%Y-%m-%d %H:%M:%S")
    student_name=student.usrname
    
    Sessions, SessionIn1H = getSessions(student_id)

    course_schedule = []
    time_ranges_str = ['8:30-9:20','9:30-10:20', '10:30-11:20', '11:30-12:20', '12:30-13:20','13:30-14:20','14:30-15:20','15:30-16:20','16:30-17:20','17:30-18:20','18:30-19:20','19:30-20:20']
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
        duration = end_time.hour * 60 + end_time.minute -start_time.hour * 60 -start_time.minute
        half = False
        if (start_time.minute == 0):
            start_datetime = datetime.combine(datetime.today(), start_time)
            updated_datetime = start_datetime - timedelta(minutes=30)
            start_time = updated_datetime.time()
            end_datetime = datetime.combine(datetime.today(), end_time)
            updated_datetime = end_datetime + timedelta(minutes=30)
            end_time = updated_datetime.time()
            half=True

        day = course.weekday
        course_schedule[day].append((course.get_weekday_display(),start_time, end_time, course, duration,half))

    context = {"student_name": student_name,'course_schedule': course_schedule,'time_ranges': time_ranges, 'days': days, "login_time": login_time}
    return render(request, "schedule.html", context)

    
def timetable(request):
    if request.session.get('authentication', None) is None:
        return redirect('/manager/login')

    student_id = request.session['authentication']
    student = Student.objects.get(name=student_id)
    login_time = timezone.localtime(student.login_time).strftime("%Y-%m-%d %H:%M:%S")
    student_name=student.usrname
    
    Sessions, SessionIn1H = getSessions(student_id)

    course_schedule = []
    time_ranges_str = ['8:30-9:20','9:30-10:20', '10:30-11:20', '11:30-12:20', '12:30-13:20','13:30-14:20','14:30-15:20','15:30-16:20','16:30-17:20','17:30-18:20','18:30-19:20','19:30-20:20']
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
        duration = end_time.hour * 60 + end_time.minute -start_time.hour * 60 -start_time.minute
        half = False
        if (start_time.minute == 0):
            start_datetime = datetime.combine(datetime.today(), start_time)
            updated_datetime = start_datetime - timedelta(minutes=30)
            start_time = updated_datetime.time()
            end_datetime = datetime.combine(datetime.today(), end_time)
            updated_datetime = end_datetime + timedelta(minutes=30)
            end_time = updated_datetime.time()
            half=True

        day = course.weekday
        course_schedule[day].append((course.get_weekday_display(),start_time, end_time, course, duration, half))

    context = {"student_name": student_name,'course_schedule': course_schedule,"sessions1h": SessionIn1H,'time_ranges': time_ranges, 'days': days, "login_time": login_time}
    return render(request, "timetable.html", context)
