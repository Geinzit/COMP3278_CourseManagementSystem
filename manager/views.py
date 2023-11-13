from django.shortcuts import render
from django.http import HttpResponse

from .models import Student, Teacher, Course, CourseSchedule, Enrollment

def index(request):
    return HttpResponse("Hello, world. You're at the manager index.")

def details(request, course_id):
    return HttpResponse("You are looking at the details of course %s." % course_id)

# def schedule(request):
    # get the logged in student

    # update later
    
