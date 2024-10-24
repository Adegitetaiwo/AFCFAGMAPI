# Generated by Django 5.0.7 on 2024-10-05 22:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("CentralApp", "0042_programschedule"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="historyimage",
            options={
                "verbose_name_plural": "Throwback Historical Pictures from Alumni"
            },
        ),
        migrations.RenameField(
            model_name="reportimage",
            old_name="picture1",
            new_name="picture",
        ),
        migrations.RemoveField(
            model_name="reportimage",
            name="picture2",
        ),
        migrations.RemoveField(
            model_name="reportimage",
            name="picture3",
        ),
        migrations.RemoveField(
            model_name="reportimage",
            name="picture4",
        ),
        migrations.AlterField(
            model_name="reportimage",
            name="campusOrSchoolAcronym",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="CentralApp.campusavs"
            ),
        ),
    ]
