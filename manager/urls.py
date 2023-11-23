from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout, name='logout'),
    path('login_history/', views.login_history, name='login_history'),
    path('course/<str:course_id>/', views.course, name='course_detail'),
    path('course/<str:course_id>/detail', views.course_detail, name='course1_information'),
    path('curriculum/', views.curriculum, name='curriculum'),
    path('teacher/<int:teacher_id>/', views.teacher),
    path('add_course/<str:course_id>/', views.add_course, name='add_course'),
    path('remove_course/<str:course_id>/', views.remove_course, name='remove_course'),
    path('send_email/', views.send_email, name='send_email'),
    path('schedule/', views.schedule, name='schedule'),
    path('timetable/', views.timetable, name='timetable')

]
