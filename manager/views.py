from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
from django.utils import timezone
from datetime import datetime, timedelta
from .models import Student, Teacher, Course, CourseSchedule, Enrollment
from .forms import EventForm

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

    
