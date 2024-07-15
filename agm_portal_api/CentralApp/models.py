from django.db import models
from cloudinary.models import CloudinaryField
from cloudinary_storage.storage import RawMediaCloudinaryStorage

# Create your models here.

class CampusAVS(models.Model):
    campusOrSchoolAcronym = models.CharField(max_length=50)
    campusName = models.TextField()
    about = models.TextField()
    flyer = models.ImageField(upload_to="campus_avs_images/", blank=True)
    
    bibleStudyTime = models.CharField(max_length=50, blank=True)
    bibleStudyVenue = models.TextField(blank=True)

    fellowshipTime = models.CharField(max_length=50, blank=True)
    fellowshipVenue = models.TextField(blank=True)

    OtherScheduleOfServiceDetails = models.TextField(blank=True)

    averageNumberOfStudent = models.PositiveIntegerField(default=0, blank=True, null=True)
    numberOfWorkforce = models.PositiveIntegerField(default=0, blank=True, null=True)

    joinAlumiGroup = models.URLField(blank=True, null=True)
    

    coordinator_name = models.CharField(max_length=300, blank=True, null=True)
    coordinator_picture = models.ImageField(upload_to="campus_avs_images_cord/", height_field=None, width_field=None, max_length=None, blank=True)
    coordinator_course = models.CharField(max_length=800, blank=True, null=True)
    coordinator_level = models.CharField(max_length=50, blank=True, null=True)
    coordinator_email = models.EmailField(max_length=254, blank=True, null=True)
    coordinator_phonenumber = models.CharField(max_length=50, blank=True, null=True)


    secretary_name = models.CharField(max_length=300, blank=True, null=True)
    secretary_picture = models.ImageField(upload_to="campus_avs_images_sect/", height_field=None, width_field=None, max_length=None, blank=True)
    secretary_course = models.CharField(max_length=800, blank=True, null=True)
    secretary_level = models.CharField(max_length=50, blank=True, null=True)
    secretary_email = models.EmailField(max_length=254, blank=True, null=True)
    secretary_phonenumber = models.CharField(max_length=50, blank=True, null=True)


    posted = models.DateTimeField(
        auto_now=False, auto_now_add=True)
    last_edited = models.DateTimeField(auto_now=True, auto_now_add=False)

    
    def __str__(self):
        return self.campusOrSchoolAcronym
    class Meta:
        verbose_name_plural = 'Campus AVS'


class CampusAVSReport(models.Model):
    campusOrSchoolAcronym = models.CharField(max_length=50)
    program_type = models.CharField(max_length=50) # welcome_program or revival_program
    year = models.CharField(max_length=50, blank=True)
    salvation = models.CharField(max_length=50, blank=True)
    sanctification = models.CharField(max_length=50, blank=True)
    baptism = models.CharField(max_length=50, blank=True)
    healing = models.CharField(max_length=50, blank=True)
    TotalAttendanceMale = models.CharField(max_length=50, blank=True)
    TotalAttendanceFemale = models.CharField(max_length=50, blank=True)
    TotalAttendance = models.CharField(max_length=50, blank=True)
    body = models.TextField(blank=True, null=True)

    
    def __str__(self):
        return self.campusOrSchoolAcronym
    class Meta:
        verbose_name_plural = 'Campus AVS Report'


class ReportImage(models.Model):
    campusOrSchoolAcronym = models.CharField(max_length=50, blank=False)
    program_type = models.CharField(max_length=50, blank=False) # welcome_program or revival_program
    picture1 = models.FileField(upload_to="report_images/", storage=RawMediaCloudinaryStorage())
    picture2 = models.FileField(upload_to="report_images/", storage=RawMediaCloudinaryStorage())
    picture3 = models.FileField(upload_to="report_images/", storage=RawMediaCloudinaryStorage())
    picture4 = models.FileField(upload_to="report_images/", storage=RawMediaCloudinaryStorage())
    
    def __str__(self):
        return self.campusOrSchoolAcronym

    class Meta:
        verbose_name_plural = 'Campus AVS Report Images'


class HistoryImage(models.Model):
    campusOrSchoolAcronym = models.CharField(max_length=50, blank=False)
    picture = models.FileField(upload_to="history_images/", storage=RawMediaCloudinaryStorage())
    
    def __str__(self):
        return self.campusOrSchoolAcronym

    class Meta:
        verbose_name_plural = 'Campus AVS Historical Pictures'

