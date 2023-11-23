# Generated by Django 4.2.7 on 2023-11-22 03:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("manager", "0014_courseschedule_classroom_address_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="moodle_link",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="courseschedule",
            name="weekday",
            field=models.IntegerField(
                choices=[
                    (6, "Sunday"),
                    (4, "Friday"),
                    (5, "Saturday"),
                    (3, "Thursday"),
                    (2, "Wednesday"),
                    (0, "Monday"),
                    (1, "Tuesday"),
                ],
                default=0,
            ),
        ),
    ]
