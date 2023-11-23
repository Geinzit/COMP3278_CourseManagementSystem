# Generated by Django 4.2.7 on 2023-11-23 10:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("manager", "0021_alter_courseschedule_weekday"),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="message",
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name="courseschedule",
            name="weekday",
            field=models.IntegerField(
                choices=[
                    (4, "Friday"),
                    (1, "Tuesday"),
                    (5, "Saturday"),
                    (3, "Thursday"),
                    (6, "Sunday"),
                    (0, "Monday"),
                    (2, "Wednesday"),
                ],
                default=0,
            ),
        ),
    ]
