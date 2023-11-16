# COMP3278_CourseManagementSystem
Group Project for COMP3278

## Introduction

[TODO]

## How to Start

1. Install all requirement package using conda

```bash
conda create -n comp3278 python=3.11
pip install -r requirements.txt
```

2. Set the SQL setting

Under `courseManager/setting` set your sql information,

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

3. Run the code

```bash
python manage.py runserver
```

4. Add user data

* Add user face data:
  * run `manager/face_data.py` to collect the data and train the model
* Add user course data:
  * @Haoyu to finish it
