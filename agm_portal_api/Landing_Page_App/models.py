from django.db import models
from cloudinary.models import CloudinaryField
from cloudinary_storage.storage import RawMediaCloudinaryStorage

# Create your models here.

# Create your models here.
class WebPageIndexData(models.Model):
    event_name = models.CharField(max_length=50, unique=True, verbose_name ='Event Name')
    event_Live_link = models.URLField(blank=True, null=True, verbose_name ='Event Live link')

    posted = models.DateTimeField(
        auto_now=False, auto_now_add=True)


    def __str__(self):
        return self.event_name
    class Meta:
        verbose_name_plural = 'Latest Event'

EVENT_DAY_CHOICES = (
    ('Saturday 26th October, 2024','Saturday 26th October, 2024'),
  )

class ProgramSchedule(models.Model):
    AGM_Day = models.CharField(max_length=50, choices=EVENT_DAY_CHOICES, verbose_name ='Day of the AGM Program', default='Saturday 26th October, 2024')
    program_activity_title = models.CharField(max_length=50, unique=True, verbose_name ='Program Title')
    activity_timeline = models.CharField(max_length=50, unique=True, verbose_name ='Timeline of Activity (e.g 10:00 - 12:00 am GMT+1)')
    program_activity_link = models.URLField(blank=True, null=True, verbose_name ='Program Activity link')
    program_attachment = models.FileField(upload_to="program_activity_attachment_files/", storage=RawMediaCloudinaryStorage(), blank=True, verbose_name ='Program_attachment')

    posted = models.DateTimeField(
        auto_now=False, auto_now_add=True)


    def __str__(self):
        return self.program_activity_title
    class Meta:
        verbose_name_plural = 'Program Schedule Activities'


# class HistoryImage(models.Model):
#     campusOrSchoolAcronym = models.CharField(max_length=50, blank=False)
#     picture = models.FileField(upload_to="history_images/", storage=RawMediaCloudinaryStorage())

#     def __str__(self):
#         return self.campusOrSchoolAcronym

#     class Meta:
#         verbose_name_plural = 'Campus AVS Historical Pictures'