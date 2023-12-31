# Generated by Django 4.2.7 on 2023-11-16 09:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "manager",
            "0009_courseschedule_weekday_alter_courseschedule_end_time_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="courseschedule",
            name="weekday",
            field=models.IntegerField(
                choices=[
                    (0, "Monday"),
                    (3, "Thursday"),
                    (4, "Friday"),
                    (5, "Saturday"),
                    (6, "Sunday"),
                    (1, "Tuesday"),
                    (2, "Wednesday"),
                ],
                default=0,
            ),
        ),
    ]
