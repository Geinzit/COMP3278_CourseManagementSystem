from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('login/', views.login_page, name='login'),
    path('course/<str:course_id>/', views.course_detail, name='course_detail'),
    path('curriculum/', views.curriculum, name='curriculum'),
]
