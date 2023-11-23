# Helper function to convert weekday and time to a datetime object for the current week
def get_schedule_data():
    from manager.models import Course, CourseSchedule
    from django.utils import timezone
    from datetime import datetime
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
        "030810": [("Mon", "13:30", "15:20", "CYPP2"), ("Thu", "18:30", "20:20", "CYPP2")],
        "030811": [("Tue", "10:00", "11:50", "CPD-LG.08"), ("Fri", "14:30", "16:20", "CPD-LG.08")],
        "030812": [("Sun", "15:30", "17:20", "CYPP2"), ("Thu", "11:00", "12:50", "CYPP2")],
        "030814": [("Mon", "16:00", "17:50", "MWT1"), ("Wed", "13:30", "15:20", "MWT1")],
        "030815": [("Tue", "14:30", "16:20", "CYCC501"), ("Fri", "09:30", "11:20", "CYCC501")],
        "030816": [("Mon", "10:30", "12:20", "CYCP1"), ("Thu", "15:30", "17:20", "CYCP1")],
        "030817": [("Wed", "12:00", "13:50", "MWT1"), ("Fri", "16:30", "18:20", "MWT1")],
        "030823": [("Tue", "13:30", "15:20", "CPD-LG.09"), ("Thu", "10:00", "11:50", "CPD-LG.09")],
        "030825": [("Mon", "14:00", "15:50", "CBC"), ("Wed", "11:30", "13:20", "CBC")],
        "030828": [("Tue", "11:00", "12:50", "CBC"), ("Fri", "12:30", "14:20", "CBC")],
        "030830": [("Wed", "10:30", "12:20", "MBG07"), ("Thu", "14:00", "15:50", "MBG07")],
        "030833": [("Sun", "11:30", "13:20", "MB167"), ("Wed", "14:30", "16:20", "MB167")],
        "030837": [("Tue", "15:30", "17:20", "CYPP3"), ("Fri", "13:00", "14:50", "MWT2")],
        "030838": [("Mon", "12:30", "14:20", "CBA"), ("Thu", "09:30", "11:20", "CBA")],
        "030844": [("Tue", "09:00", "10:50", "CYCP1"), ("Fri", "15:00", "16:50", "CYCP1")],
        "033795": [("Wed", "13:00", "14:50", "CPD-3.04"), ("Thu", "16:30", "18:20", "CPD-3.04")],
        "034494": [("Mon", "09:30", "11:20", "CBC"), ("Wed", "16:00", "17:50", "CBC")],
        "037006": [("Sun", "12:00", "13:50", "WLGH"), ("Fri", "11:30", "13:20", "KB223")],
        "038210": [("Mon", "10:00", "11:50", "RHT"), ("Thu", "12:30", "14:20", "CYCP1")],
        "038858": [("Tue", "14:00", "15:50", "CYPP4"), ("Wed", "09:00", "10:50", "CYPP4")],
    }

    CourseSchedule.objects.all().delete()
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
        for weekday, start, end, address in times:
            start_time = datetime.strptime(start, "%H:%M").time()
            end_time = datetime.strptime(end, "%H:%M").time()
            new_course_schedule = CourseSchedule(course=course, weekday=weekdays[weekday], start_time=start, end_time=end, classroom_address=address)
            new_course_schedule.save()
get_schedule_data()

