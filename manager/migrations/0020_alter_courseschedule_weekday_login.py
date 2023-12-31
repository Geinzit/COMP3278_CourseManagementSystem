# Generated by Django 4.2.7 on 2023-11-23 09:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("manager", "0019_alter_courseschedule_weekday"),
    ]

    operations = [
        migrations.AlterField(
            model_name="courseschedule",
            name="weekday",
            field=models.IntegerField(
                choices=[
                    (4, "Friday"),
                    (6, "Sunday"),
                    (1, "Tuesday"),
                    (0, "Monday"),
                    (3, "Thursday"),
                    (2, "Wednesday"),
                    (5, "Saturday"),
                ],
                default=0,
            ),
        ),
        migrations.CreateModel(
            name="Login",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("login_time", models.DateTimeField(blank=True, null=True)),
                ("logout_time", models.DateTimeField(blank=True, null=True)),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="student_login",
                        to="manager.student",
                    ),
                ),
            ],
        ),
    ]
