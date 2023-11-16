from django.db import models
# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length = 100, primary_key = True)
    usrname = models.CharField(max_length = 100, null = True, blank = True)
    email = models.CharField(max_length = 100, null = True, blank = True)
    bio = models.CharField(max_length = 1000, null = True, blank = True)

    
class Teacher(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length = 100, null = True, blank = True)
    department = models.CharField(max_length = 100, null = True, blank = True)
    bio = models.CharField(max_length = 10000, null = True, blank = True)

    
class Course(models.Model):
    course_id = models.CharField(max_length = 15, primary_key = True,unique = True)
    course_name = models.CharField(max_length = 15, null = True, blank = True)
    teacher = models.ForeignKey(Teacher, on_delete = models.CASCADE, null = True, blank = True)
    description = models.CharField(max_length = 1000, null = True, blank = True)

    
class CourseSchedule(models.Model):
    WEEKDAY_CHOICES = {
        (0, "Monday"),
        (1, "Tuesday"),
        (2, "Wednesday"),
        (3, "Thursday"),
        (4, "Friday"),
        (5, "Saturday"),
        (6, "Sunday"),
    }

    
    course = models.ForeignKey(Course, related_name = "course_schedule", on_delete = models.CASCADE)
    weekday = models.IntegerField(choices = WEEKDAY_CHOICES, default = 0)
    start_time = models.TimeField(null = True, blank = True)
    end_time = models.TimeField(null = True, blank = True)


    
class Enrollment(models.Model):
    course = models.ForeignKey(Course, related_name = "course_enrollments", on_delete = models.CASCADE)
    student = models.ForeignKey(Student, related_name = "student_courses", on_delete = models.CASCADE)
    class Meta:
        unique_together = ('course', 'student')

