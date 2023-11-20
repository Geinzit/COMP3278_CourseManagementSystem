
function check_time_range(time_range, start_time, end_time) {
    var time = parseInt(time_range.split(':')[0]);
    var course_start = parseInt(start_time.split(':')[0]);
    var course_end = parseInt(end_time.split(':')[0]);

    return time >= course_start && time < course_end;
}