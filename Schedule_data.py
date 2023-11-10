from django.utils import timezone
import datetime

# Helper function to convert weekday and time to a datetime object for the current week
def get_weekday_datetime(weekday_str, time_str):
    weekdays = {
        'Mon': 0, 'Tue': 1, 'Wed': 2, 'Thu': 3, 'Fri': 4, 'Sat': 5, 'Sun': 6
    }
    weekday = weekdays[weekday_str]
    time_obj = datetime.datetime.strptime(time_str, '%H:%M').time()
    today = timezone.now()
    start_of_week = today - datetime.timedelta(days=today.weekday())
    return datetime.datetime.combine(start_of_week, time_obj) + datetime.timedelta(days=weekday)

# Course schedule data
schedule_data = {
    "030815": [("Fri", "17:30", "18:20"), ("Tue", "16:30", "18:20")],
    "030811": [("Fri", "12:30", "14:20"), ("Tue", "12:30", "13:20")],
    # ... other course schedules
}

# Creating CourseSchedule instances
for course_id, times in schedule_data.items():
    course = Course.objects.get(course_id=course_id)
    for weekday, start, end in times:
        start_time = get_weekday_datetime(weekday, start)
        end_time = get_weekday_datetime(weekday, end)
        course_schedule = CourseSchedule(course=course, start_time=start_time, end_time=end_time)
        course_schedule.save()
