# Generated by Django 5.0.7 on 2024-10-05 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "Landing_Page_App",
            "0002_historyimage_alter_programschedule_activity_timeline",
        ),
    ]

    operations = [
        migrations.DeleteModel(
            name="HistoryImage",
        ),
        migrations.AlterField(
            model_name="programschedule",
            name="AGM_Day",
            field=models.CharField(
                choices=[
                    ("Saturday 26th October, 2024", "Saturday 26th October, 2024")
                ],
                default="Saturday 26th October, 2024",
                max_length=50,
                verbose_name="Day of the AGM Program",
            ),
        ),
    ]
