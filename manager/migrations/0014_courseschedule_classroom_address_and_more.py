# Generated by Django 4.2.7 on 2023-11-21 12:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("manager", "0013_student_login_time_alter_courseschedule_weekday"),
    ]

    operations = [
        migrations.AddField(
            model_name="courseschedule",
            name="classroom_address",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="courseschedule",
            name="weekday",
            field=models.IntegerField(
                choices=[
                    (4, "Friday"),
                    (2, "Wednesday"),
                    (3, "Thursday"),
                    (0, "Monday"),
                    (1, "Tuesday"),
                    (5, "Saturday"),
                    (6, "Sunday"),
                ],
                default=0,
            ),
        ),
    ]
