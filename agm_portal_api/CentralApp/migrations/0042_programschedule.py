# Generated by Django 5.0.7 on 2024-09-30 12:42

import cloudinary_storage.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("CentralApp", "0041_campusavs_updateaboutschool"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProgramSchedule",
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
                (
                    "AGM_Day",
                    models.CharField(
                        choices=[("saturday", "saturday")],
                        default="saturday",
                        max_length=50,
                        verbose_name="Day of the AGM Program",
                    ),
                ),
                (
                    "program_activity_title",
                    models.CharField(
                        max_length=50, unique=True, verbose_name="Program Title"
                    ),
                ),
                (
                    "activity_timeline",
                    models.CharField(
                        max_length=50,
                        unique=True,
                        verbose_name="Timeline of Activity (e.g 10:00 - 12:00 am GMT+1",
                    ),
                ),
                (
                    "program_activity_link",
                    models.URLField(
                        blank=True, null=True, verbose_name="Program Activity link"
                    ),
                ),
                (
                    "program_attachment",
                    models.FileField(
                        blank=True,
                        storage=cloudinary_storage.storage.RawMediaCloudinaryStorage(),
                        upload_to="program_activity_attachment_files/",
                        verbose_name="Program_attachment",
                    ),
                ),
                ("posted", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name_plural": "Program Schedule Activities",
            },
        ),
    ]
