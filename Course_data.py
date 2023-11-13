from django.db import models

from manager.models import Course, Teacher

course1 = Course(course_id="030815", course_name="COMP1117", teacher=Teacher.objects.get(name="Dr. Loretta Choi"), description="Computer Programming")
course2 = Course(course_id="030811", course_name="COMP2119", teacher=Teacher.objects.get(name="Dr. H.T.H. Chan"), description="Introduction to data structures and algorithms")
course3 = Course(course_id="030812", course_name="COMP2120", teacher=Teacher.objects.get(name="Dr. Qi Zhao"), description="Computer organization")
course4 = Course(course_id="030810", course_name="COMP2121", teacher=Teacher.objects.get(name="Dr. H.T.H. Chan"), description="Discrete mathematics")
course5 = Course(course_id="030823", course_name="COMP2396", teacher=Teacher.objects.get(name="Dr. T.W. Chim"), description="Object-oriented programming and Java")
course6 = Course(course_id="037006", course_name="COMP2113", teacher=Teacher.objects.get(name="Dr. Chenxiong Qian"), description="Programming technologies")
course7 = Course(course_id="038210", course_name="COMP2501", teacher=Teacher.objects.get(name="Dr. Ruibang Luo"), description="Introduction to Data Science and Engineering")
course8 = Course(course_id="030816", course_name="COMP3230", teacher=Teacher.objects.get(name="Dr. A.T.C. Tam"), description="Principles of operating systems")
course9 = Course(course_id="030825", course_name="COMP3231", teacher=Teacher.objects.get(name="Dr. Heming Cui"), description="Computer architecture")
course10 = Course(course_id="030817", course_name="COMP3234", teacher=Teacher.objects.get(name="Dr. A.T.C. Tam"), description="Computer and communication networks")
course11 = Course(course_id="038858", course_name="COMP3251", teacher=Teacher.objects.get(name="Dr. Zhiyi Huang"), description="Algorithm design")
course12 = Course(course_id="033795", course_name="COMP3258", teacher=Teacher.objects.get(name="Dr. B. Oliveira"), description="Functional programming")
course13 = Course(course_id="030828", course_name="COMP3259", teacher=Teacher.objects.get(name="Dr. B. Oliveira"), description="Principles of programming languages")
course14 = Course(course_id="030830", course_name="COMP3270", teacher=Teacher.objects.get(name="Dr. D. Schnieders"), description="Artificial intelligence")
course15 = Course(course_id="030814", course_name="COMP3278", teacher=Teacher.objects.get(name="Dr. C.K. Chui"), description="Introduction to database management systems")
course16 = Course(course_id="030833", course_name="COMP3314", teacher=Teacher.objects.get(name="Dr. Hengshuang Zhao"), description="Machine learning")
course17 = Course(course_id="034494", course_name="COMP3316", teacher=Teacher.objects.get(name="Dr. Giulio Chiribella"), description="Quantum information and computation")
course18 = Course(course_id="030837", course_name="COMP3322", teacher=Teacher.objects.get(name="Dr. A.T.C. Tam"), description="Modern Technologies on World Wide Web")
course19 = Course(course_id="030838", course_name="COMP3323", teacher=Teacher.objects.get(name="Dr. R.C.K. Cheng"), description="Advanced database systems")
course20 = Course(course_id="030844", course_name="COMP3329", teacher=Teacher.objects.get(name="Dr. T.W. Chim"), description="Computer game design and programming")

for i in range(1,21):
    #print(i)
    name = f"course{i}"
    #print(name,globals()[name])
    course = globals()[name]
    course.save()
    #course, created = Course.objects.get_or_create(globals()[name])
   # if not created:
    #    break

