from django.utils import timezone
from datetime import datetime

from manager.models import Course, CourseSchedule


# Helper function to convert weekday and time to a datetime object for the current week
weekdays = {
    'Mon': 0, 'Tue': 1, 'Wed': 2, 'Thu': 3, 'Fri': 4, 'Sat': 5, 'Sun': 6
}
"""
def get_weekday_datetime(weekday_str, time_str):
    weekdays = {
        'Mon': 0, 'Tue': 1, 'Wed': 2, 'Thu': 3, 'Fri': 4, 'Sat': 5, 'Sun': 6
    }
    weekday = weekdays[weekday_str]
    time_obj = datetime.datetime.strptime(time_str, '%H:%M').time()
    today = timezone.now().date()
    current_weekday = today.weekday()
    days_difference = (weekday - current_weekday) % 7
    start_of_week = today - datetime.timedelta(days=current_weekday)
    target_weekday = start_of_week + datetime.timedelta(days=days_difference)
    
    # Create a timezone-aware datetime object
    target_datetime = timezone.make_aware(datetime.datetime.combine(target_weekday, time_obj))
    
    return target_datetime
"""
# Course schedule data
schedule_data = {
    "030810": [("Mon", "13:30", "15:20"), ("Thu", "18:30", "20:20")],
    "030811": [("Tue", "10:00", "11:50"), ("Fri", "14:30", "16:20")],
    "030812": [("Sun", "15:30", "17:20"), ("Thu", "11:00", "12:50")],
    "030814": [("Mon", "16:00", "17:50"), ("Wed", "13:30", "15:20")],
    "030815": [("Tue", "14:30", "16:20"), ("Fri", "09:30", "11:20")],
    "030816": [("Mon", "10:30", "12:20"), ("Thu", "15:30", "17:20")],
    "030817": [("Wed", "12:00", "13:50"), ("Fri", "16:30", "18:20")],
    "030823": [("Tue", "13:30", "15:20"), ("Thu", "10:00", "11:50")],
    "030825": [("Mon", "14:00", "15:50"), ("Wed", "11:30", "13:20")],
    "030828": [("Tue", "11:00", "12:50"), ("Fri", "12:30", "14:20")],
    "030830": [("Wed", "10:30", "12:20"), ("Thu", "14:00", "15:50")],
    "030833": [("Sun", "11:30", "13:20"), ("Wed", "14:30", "16:20")],
    "030837": [("Tue", "15:30", "17:20"), ("Fri", "13:00", "14:50")],
    "030838": [("Mon", "12:30", "14:20"), ("Thu", "09:30", "11:20")],
    "030844": [("Tue", "09:00", "10:50"), ("Fri", "15:00", "16:50")],
    "033795": [("Wed", "13:00", "14:50"), ("Thu", "16:30", "18:20")],
    "034494": [("Mon", "09:30", "11:20"), ("Wed", "16:00", "17:50")],
    "037006": [("Sun", "12:00", "13:50"), ("Fri", "11:30", "13:20")],
    "038210": [("Mon", "10:00", "11:50"), ("Thu", "12:30", "14:20")],
    "038858": [("Tue", "14:00", "15:50"), ("Wed", "09:00", "10:50")],
}


def get_schedule_data():
    # Iterating through schedule data
    for course_id, times in schedule_data.items():
        # If CourseSchedules exist, update the times; otherwise, create new ones
        """
        if course_schedules.exists():
            for course_schedule in course_schedules:
                for weekday, start, end in times:
                    # Update the existing CourseSchedule
                    start_time = datetime.strptime(start, "%H:%M").time()
                    end_time = datetime.strptime(end, "%H:%M").time()
                    course_schedule.weekday = weekdays[weekday]
                    course_schedule.start_time = start_time
                    course_schedule.end_time = end_time
                    course_schedule.save()
        else:
        """
            # CourseSchedules don't exist, create new ones
            # print(course_id)
        course = Course.objects.get(course_id=course_id)
        for weekday, start, end in times:
            start_time = datetime.strptime(start, "%H:%M").time()
            end_time = datetime.strptime(end, "%H:%M").time()
            new_course_schedule = CourseSchedule(course=course, weekday=weekdays[weekday], start_time=start, end_time=end)
            new_course_schedule.save()

CourseSchedule.objects.all().delete()
get_schedule_data()

