# COMP3278_CourseManagementSystem
Group Project for COMP3278

## Introduction

This is an interactive Course Selection / Management System. The system uses facial recognition to authenticate the user. And all logged in Users can freely enroll/drop courses from our featured course list. Through this information, you can view your course timetable, as well as receive notification from upcoming courses in 1 hour. You can also view each course's detailed information and its Lecturer's information. You can also view recommended courses on a course detail page based on similarities in the course information page. Finally, you can send and email notification to remind yourself of your upcoming courses.

### Features

* Face Recognition-based Login and Authentication System 
* Fully interactable course selection / removal system with a full fledged Course Timetable for easy visualization
* Detecting and informing details on upcoming courses (in one hour to be precise)
* Full list of viewable Courses, including their weekly schedules, and Lecturers' information
### Design of URLs and Parameter

* Login Page: `http://host-address/manager/login/`
* Course Timetable: `http://host-address/manager/curriculum/`
* Course List: `http://host-address/manager`
* Course Detail: `http://host-address/manager/course/?course-id={{ course_id }}`

## How to Start

1. Install all requirement package using conda

```bash
conda create -n comp3278 python=3.11
conda activate comp3278
pip install -r requirements.txt
```

2. Database settings

Set up your Database server(make sure the server has proper support with django). It's recommended to use a new empty database to avoid migration problems.
2. Database settings

Set up your Database server(make sure the server has proper support with django). It's recommended to use a new empty database to avoid migration problems.

Under `courseManager/settings.py` set your database information,

by default, the settings are.
```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "CourseManager",
        "USER": "root",
        "PASSWORD": "123456",
        "HOST": "localhost",
        "PORT": "5432",
    }
}
```
next, perform the migrations.
```bash
python manage.py migrate
```

3. Run the server

```bash
python manage.py runserver
```

4. Add user data

* Add user face data:
  * run `manager/face_data.py` to collect the data and train the model
* Add user in database:
  * You need a Student type data in models.py with UID
  * Either add them through the SQL server, or add them into our sample file student_data.py, and then check out the next section
  
## How to add our sample data to database
- Simply run `python manage.py load_data_fromPython`

[Alternative]

- under the project folder, enter django shell with ```python manage.py shell```
- run the corresponding data python file(Course_data.py, Schedule_data.py etc.) in the shell, for example ```exec(open('Schedule_data.py').read())```

## Add your face data

0. Unzip our existing [dataset](https://drive.google.com/file/d/1mhWGQm_pGOPZohD24spFRHFVY-Nh__oC/view?usp=sharing) under into `manager/data`.

1. If you want, you can create your own face data under `manager` directory

   * Step 1: Modify the `manager/face_data.py`, then run the code to collect the data

     ```python
     if __name__ == "__main__":
         capture_data(user_name="UID YOU WANT")
         # train_model("data/data", "data")
     ```

   * Step 2: Modify the `manager/face_data.py`, then run the code to train the model
     
     ```python
     if __name__ == "__main__":
         # capture_data(user_name="UID YOU WANT")
         train_model("data/data", "data")
     ```
## How to set up the email notification system

0. Go to courseManager/settings.py and find the EMAIL settings:
   ```python
    # Email Settings
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'your-email-host'
    EMAIL_PORT = 587
    EMAIL_HOST_USER = 'your-host-email-address'
    EMAIL_HOST_PASSWORD = 'your-email-password'
    EMAIL_USE_TLS = True
   ```
1. Change the `EMAIL_HOST` to your desired email host(for example, smtp.gmail.com)
2. Change the `EMAIL_HOST_USER` to your desired host email address(example@gmail.com)
3. Change the `EMAIL_HOST_PASSWORD` to your corresponding email password(gmail, for example, requires an app password)
4. Go to manager/views.py and find this particular section in the `send_email` method.
    ```python
    # enter the email address you wish to send from
    from_email = "your-email-address"
    ```
5. Change the `from_email` to your desired email address to send from(it should typically be the same as the address you entered in `EMAIL_HOST_USER`)
6. Run the server and you're good to go!
