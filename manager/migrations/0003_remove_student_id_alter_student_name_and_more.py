# Generated by Django 4.2.7 on 2023-11-08 10:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("manager", "0002_student_name_student_student_id"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="student",
            name="id",
        ),
        migrations.AlterField(
            model_name="student",
            name="name",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="student",
            name="student_id",
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
