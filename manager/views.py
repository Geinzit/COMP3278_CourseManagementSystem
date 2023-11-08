from django.shortcuts import render, redirect
from django.http import HttpResponse
#from django.contrib.auth import login,authenticate, logout
#from django.contrib.auth.decorate import login_required
#from django.contrib.auth.models import User
from .models import Student, Teacher, Course, CourseSchedule, Enrollment

def index(request):
    return HttpResponse("Hello, world. You're at the manager index.")

def details(request, course_id):
    return HttpResponse("You are looking at the details of course %s." % course_id)

