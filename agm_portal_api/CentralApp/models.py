from django.db import models
from cloudinary.models import CloudinaryField
from cloudinary_storage.storage import RawMediaCloudinaryStorage

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
    ('saturday','saturday'),
  )

class ProgramSchedule(models.Model):
    AGM_Day = models.CharField(max_length=50, choices=EVENT_DAY_CHOICES, verbose_name ='Day of the AGM Program', default='saturday')
    program_activity_title = models.CharField(max_length=50, unique=True, verbose_name ='Program Title')
    activity_timeline = models.CharField(max_length=50, unique=True, verbose_name ='Timeline of Activity (e.g 10:00 - 12:00 am GMT+1')
    program_activity_link = models.URLField(blank=True, null=True, verbose_name ='Program Activity link')
    program_attachment = models.FileField(upload_to="program_activity_attachment_files/", storage=RawMediaCloudinaryStorage(), blank=True, verbose_name ='Program_attachment')

    posted = models.DateTimeField(
        auto_now=False, auto_now_add=True)


    def __str__(self):
        return self.event_name
    class Meta:
        verbose_name_plural = 'Program Schedule Activities'



SCHOOLTYPE_CHOICES = (
    ('university','University'),
    ('college', "College of Education/Medcine or Technology"),
    ('polytechnic', "Polytechnic")

)

ACTIVE_CHOICES = (
    ('active','active'),
    ('inactive', "inactive")
)

class CampusAVS(models.Model):
    campusOrSchoolAcronym = models.CharField(max_length=50, unique=True, verbose_name ='School Acronym', help_text='Acronym like FUTA or UNILAG')
    campusName = models.CharField(max_length=150, verbose_name ='Campus Full name')
    institutionType = models.CharField(max_length=50, choices=SCHOOLTYPE_CHOICES, verbose_name ='Type of Institution')
    active_Inactive = models.CharField(max_length=50, choices=ACTIVE_CHOICES, verbose_name ='Active or Inactive')
    about = models.TextField(verbose_name ='Remarks or Report if Inactive', help_text='State the reason why Fellowhip is not active, and give the details of who someone that we can reachout to.')
    fellowship_facebook_link = models.URLField(blank=True, null=True, verbose_name ='Fellowship Facebook link')
    fellowship_instagram_link = models.URLField(blank=True, null=True, verbose_name ='Fellowship Instagram Link')
    fellowship_email = models.CharField(max_length=50, blank=True, verbose_name ='Campus Fellowship Email Address')
    # fellowship_phone_number = models.CharField(max_length=50,  blank=True, verbose_name ='Campus Fellowship Phone number')
    flyer = models.ImageField(upload_to="campus_avs_images/", blank=True, verbose_name ='AFCF Picture', help_text='Upload A Group Photograph of AFCF or Picture taken during a service.')
    flyer2 = models.ImageField(upload_to="campus_avs_images/", blank=True, verbose_name ='AFCF Picture2', help_text='Upload ANOTHER Group Photograph of AFCF or Picture taken during a service')
    bibleStudyDay = models.CharField(max_length=50, blank=True, verbose_name ='Day of the Week')
    bibleStudyTime = models.CharField(max_length=50, blank=True, verbose_name ='Time')
    bibleStudyVenue = models.CharField(max_length=400, blank=True, verbose_name ='Venue')

    fellowshipDay = models.CharField(max_length=50, blank=True, verbose_name ='Day of the Week')
    fellowshipTime = models.CharField(max_length=50, blank=True, verbose_name ='Time')
    fellowshipVenue = models.CharField(max_length=400, blank=True, verbose_name ='Venue')

    OtherScheduleOfServiceDetails = models.TextField(blank=True, verbose_name ='Other Fellowship Service Details')

    # Update about the School
    UpdateAboutSchool = models.TextField(blank=True, verbose_name ='AFCF Campus Update', help_text="What's going on in your Campus Fellowhship that you'll want others to know about")


    averageNumberOfStudent = models.PositiveIntegerField(default=0, blank=True, null=True, verbose_name ='Average number of Student')
    numberOfWorkforce = models.PositiveIntegerField(default=0, blank=True, null=True, verbose_name ='Total number of workforce')

    joinAlumiGroup = models.URLField(blank=True, null=True, verbose_name ='Link to join Alumni Group')


    coordinator_name = models.CharField(max_length=300, blank=True, null=True, verbose_name ='Coordinator name')
    coordinator_picture = models.ImageField(upload_to="campus_avs_images_cord/", height_field=None, width_field=None, max_length=None, blank=True, verbose_name ='Upload Coordinator picture (Headshot only)')
    coordinator_course = models.CharField(max_length=800, blank=True, null=True, verbose_name ='Coordinator Course')
    coordinator_level = models.CharField(max_length=50, blank=True, null=True, verbose_name ='Coordinator Level Or program')
    coordinator_email = models.EmailField(max_length=254, blank=True, null=True, verbose_name ='Coordinator email')
    coordinator_phonenumber = models.CharField(max_length=50, blank=True, null=True, verbose_name ='Coordinator Phone number')


    secretary_name = models.CharField(max_length=300, blank=True, null=True, verbose_name ='Secretary name')
    secretary_picture = models.ImageField(upload_to="campus_avs_images_sect/", height_field=None, width_field=None, max_length=None, blank=True, verbose_name ='Upload Secretary Picture  (Headshot only)')
    secretary_course = models.CharField(max_length=800, blank=True, null=True, verbose_name ='Secretary course')
    secretary_level = models.CharField(max_length=50, blank=True, null=True, verbose_name ='Secretary Level or program')
    secretary_email = models.EmailField(max_length=254, blank=True, null=True, verbose_name ='Secretary email')
    secretary_phonenumber = models.CharField(max_length=50, blank=True, null=True, verbose_name ='Secretary Phone number')

    # Latest National Program
    nrp_year = models.CharField(max_length=10, blank=True, null=True, verbose_name ='NRP Year', help_text='When (year) was your latest NRP held?')
    nrp_salvation = models.PositiveIntegerField(default=0, blank=True, null=True, verbose_name ='Number of People Saved')
    nrp_sanctification = models.PositiveIntegerField(default=0, blank=True, null=True, verbose_name ='Number of People Sanctified')
    nrp_baptism = models.PositiveIntegerField(default=0, blank=True, null=True, verbose_name ='Number of People Baptised')
    nrp_healing = models.PositiveIntegerField(default=0, blank=True, null=True, verbose_name ='Number of People Healed')
    nrp_reannointing = models.PositiveIntegerField(default=0, blank=True, null=True, verbose_name ='Number of People Reannointed')
    nrp_other_blessing = models.PositiveIntegerField(default=0, blank=True, null=True, verbose_name ='Number of Other Blessing')
    nrp_TotalAttendanceMale = models.PositiveIntegerField(default=0, blank=True, null=True, verbose_name ='Number of Male in attendance')
    nrp_TotalAttendanceFemale = models.PositiveIntegerField(default=0, blank=True, null=True, verbose_name ='Number of Female in attendance')
    nrp_TotalOfficiatingMemeber = models.PositiveIntegerField(default=0, blank=True, null=True, verbose_name ='Number of Officiating Members')
    nrp_TotalAttendance = models.PositiveIntegerField(default=0, blank=True, verbose_name ='Total Number of people in attendance')
    nrp_body = models.TextField(blank=True, null=True, verbose_name ='Note')
    nrp_google_drive_link = models.URLField(blank=True, null=True, verbose_name ='Google Drive link to reports')
    nrp_picture1 = models.FileField(upload_to="report_images/", storage=RawMediaCloudinaryStorage(), blank=True, verbose_name ='Picture (1)')
    nrp_picture2 = models.FileField(upload_to="report_images/", storage=RawMediaCloudinaryStorage(), blank=True, verbose_name ='Picture (2)')
    nrp_picture3 = models.FileField(upload_to="report_images/", storage=RawMediaCloudinaryStorage(), blank=True, verbose_name ='Picture (3)')
    nrp_picture4 = models.FileField(upload_to="report_images/", storage=RawMediaCloudinaryStorage(), blank=True, verbose_name ='Picture (4)')
    nrp_picture5 = models.FileField(upload_to="report_images/", storage=RawMediaCloudinaryStorage(), blank=True, verbose_name ='Picture (5)')
    nrp_picture6 = models.FileField(upload_to="report_images/", storage=RawMediaCloudinaryStorage(), blank=True, verbose_name ='Picture (6)')
    nrp_picture7 = models.FileField(upload_to="report_images/", storage=RawMediaCloudinaryStorage(), blank=True, verbose_name ='Picture (7)')
    nrp_picture8 = models.FileField(upload_to="report_images/", storage=RawMediaCloudinaryStorage(), blank=True, verbose_name ='Picture (8)')

    # Latest National Program
    wlc_year = models.CharField(max_length=10, blank=True, null=True, verbose_name ='Welcome Program Year', help_text='When (year) was your latest Welcome Program held?')
    wlc_salvation = models.PositiveIntegerField(default=0, blank=True, verbose_name ='Number of People Saved')
    wlc_sanctification = models.PositiveIntegerField(default=0, blank=True, verbose_name ='Number of People Sanctified')
    wlc_baptism = models.PositiveIntegerField(default=0, blank=True, verbose_name ='Number of People Baptised')
    wlc_healing = models.PositiveIntegerField(default=0, blank=True, verbose_name ='Number of People Healed')
    wlc_reannointing = models.PositiveIntegerField(default=0, blank=True, null=True, verbose_name ='Number of People Reannointed')
    wlc_other_blessing = models.PositiveIntegerField(default=0, blank=True, null=True, verbose_name ='Number of Other Blessing')
    wlc_TotalAttendanceMale = models.PositiveIntegerField(default=0, blank=True, verbose_name ='Number of Male in attendance')
    wlc_TotalAttendanceFemale = models.PositiveIntegerField(default=0, blank=True, verbose_name ='Number of Female in attendance')
    wlc_TotalOfficiatingMemeber = models.PositiveIntegerField(default=0, blank=True, null=True, verbose_name ='Number of Officiating Members')
    wlc_TotalAttendance = models.PositiveIntegerField(default=0, blank=True, verbose_name ='Total Number of people in attendance')
    wlc_body = models.TextField(blank=True, null=True, verbose_name ='Note')
    wlc_google_drive_link = models.URLField(blank=True, null=True, verbose_name ='Google Drive link to reports')
    wlc_picture1 = models.FileField(upload_to="report_images/", storage=RawMediaCloudinaryStorage(), blank=True, verbose_name ='Picture (1)')
    wlc_picture2 = models.FileField(upload_to="report_images/", storage=RawMediaCloudinaryStorage(), blank=True, verbose_name ='Picture (2)')
    wlc_picture3 = models.FileField(upload_to="report_images/", storage=RawMediaCloudinaryStorage(), blank=True, verbose_name ='Picture (3)')
    wlc_picture4 = models.FileField(upload_to="report_images/", storage=RawMediaCloudinaryStorage(), blank=True, verbose_name ='Picture (4)')
    wlc_picture5 = models.FileField(upload_to="report_images/", storage=RawMediaCloudinaryStorage(), blank=True, verbose_name ='Picture (5)')
    wlc_picture6 = models.FileField(upload_to="report_images/", storage=RawMediaCloudinaryStorage(), blank=True, verbose_name ='Picture (6)')
    wlc_picture7 = models.FileField(upload_to="report_images/", storage=RawMediaCloudinaryStorage(), blank=True, verbose_name ='Picture (7)')
    wlc_picture8 = models.FileField(upload_to="report_images/", storage=RawMediaCloudinaryStorage(), blank=True, verbose_name ='Picture (8)')

    posted = models.DateTimeField(
        auto_now=False, auto_now_add=True)
    last_edited = models.DateTimeField(auto_now=True, auto_now_add=False)


    def __str__(self):
        return self.campusOrSchoolAcronym
    class Meta:
        verbose_name_plural = 'List of Campus AVS'

PROGRAM_CHOICES = (
    ('revival_program','National Revival Program (NRP)'),
    ('welcome_program', "Fresher's Welcome Program")
)

class CampusAVSReport(models.Model):
    campusOrSchoolAcronym = models.CharField(max_length=50)
    program_type = models.CharField(max_length=50, choices=PROGRAM_CHOICES) # welcome_program or revival_program
    year = models.CharField(max_length=50, blank=True)
    salvation = models.CharField(max_length=50, blank=True)
    sanctification = models.CharField(max_length=50, blank=True)
    baptism = models.CharField(max_length=50, blank=True)
    healing = models.CharField(max_length=50, blank=True)
    TotalAttendanceMale = models.CharField(max_length=50, blank=True)
    TotalAttendanceFemale = models.CharField(max_length=50, blank=True)
    TotalAttendance = models.CharField(max_length=50, blank=True)
    body = models.TextField(blank=True, null=True)
    google_drive_link = models.URLField(blank=True, null=True, verbose_name ='Google Drive link to reports')


    def __str__(self):
        return self.campusOrSchoolAcronym
    class Meta:
        verbose_name_plural = 'Campus AVS Report'


# class ReportsImage(models.Model):
#     campusOrSchoolAcronym = models.ForeignKey(CampusAVS, on_delete=models.CASCADE)
#     program_type = models.CharField(max_length=50, choices=PROGRAM_CHOICES, blank=False) # welcome_program or revival_program
#     picture = models.FileField(upload_to="report_images/", storage=RawMediaCloudinaryStorage())


#     def __str__(self):
#         return self.campusOrSchoolAcronym

#     class Meta:
#         verbose_name_plural = 'Campus AVS Report Images'


class HistoryImage(models.Model):
    campusOrSchoolAcronym = models.CharField(max_length=50, blank=False)
    picture = models.FileField(upload_to="history_images/", storage=RawMediaCloudinaryStorage())

    def __str__(self):
        return self.campusOrSchoolAcronym

    class Meta:
        verbose_name_plural = 'Throwback Historical Pictures from Alumni'

