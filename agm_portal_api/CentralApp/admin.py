from django.contrib import admin
from .models import CampusAVS, CampusAVSReport, HistoryImage, WebPageIndexData
# Register your models here.

admin.site.site_header = 'AFCF AGM PORTAL'


# @admin.register(WebPageIndexData)
# class WebPageIndexDataAdmin(admin.ModelAdmin):
#     list_display = ['event_name', 'event_Live_link', 'posted']


# @admin.register(ProgramSchedule)
# class ProgramScheduleAdmin(admin.ModelAdmin):
#     list_display = ['program_activity_title', 'activity_timeline']


# class ReportsImageInlineAdmin(admin.StackedInline):
#     model = ReportsImage



@admin.register(CampusAVS)
class CampusAVSAdmin(admin.ModelAdmin):
    list_display = ['campusOrSchoolAcronym', 'institutionType', 'active_Inactive', 'campusName', 'averageNumberOfStudent', 'last_edited']
    search_fields = ['campusOrSchoolAcronym', 'campusName', 'institutionType']
    # inlines = [ReportsImageInlineAdmin]
    fieldsets = [
        ('General School Information', {"fields": ["campusOrSchoolAcronym", "campusName",'institutionType']}),
        ("AFCF General Information", {"fields": ['flyer', 'flyer2', 'active_Inactive', 'about', 'fellowship_facebook_link', 'fellowship_instagram_link', 'fellowship_email', 'joinAlumiGroup']}),
        ("Bible Study Details", {"fields": ['bibleStudyDay', "bibleStudyTime", 'bibleStudyVenue']}),
        ("Variety Program Details", {"fields": ['fellowshipDay', "fellowshipTime", 'fellowshipVenue']}),
        ("Other Schedule of service Details", {"fields": ['OtherScheduleOfServiceDetails']}),
        ("Update About Your Campus Fellowship (AFCF)", {"fields": ['UpdateAboutSchool']}),
        ("AFCF Statistics", {"fields": ['averageNumberOfStudent', "numberOfWorkforce"]}),
        ("Meet the Executives", {"fields": ["coordinator_picture", 'coordinator_name', 'coordinator_course','coordinator_level', 'coordinator_email', 'coordinator_phonenumber', 'secretary_picture', 'secretary_name', 'secretary_course', 'secretary_level', 'secretary_email', 'secretary_phonenumber']}),
        ("REPORTS: National Revival Program", {"fields": ["nrp_year", "nrp_salvation", 'nrp_sanctification', 'nrp_baptism','nrp_healing', 'nrp_reannointing', 'nrp_other_blessing', 'nrp_TotalAttendanceMale', 'nrp_TotalAttendanceFemale', 'nrp_TotalOfficiatingMemeber', 'nrp_TotalAttendance', 'nrp_body', 'nrp_google_drive_link', 'nrp_picture1', 'nrp_picture2', 'nrp_picture3', 'nrp_picture4','nrp_picture5','nrp_picture6','nrp_picture7','nrp_picture8']}),
        ("REPORTS: Freshers' Welcome Program", {"fields": ["wlc_year", "wlc_salvation", 'wlc_sanctification', 'wlc_baptism','wlc_healing', 'wlc_reannointing', 'wlc_other_blessing', 'wlc_TotalAttendanceMale', 'wlc_TotalAttendanceFemale', 'wlc_TotalOfficiatingMemeber', 'wlc_TotalAttendance', 'wlc_body', 'wlc_google_drive_link', 'wlc_picture1', 'wlc_picture2', 'wlc_picture3', 'wlc_picture4','wlc_picture5','wlc_picture6','wlc_picture7','wlc_picture8']}),


    ]

# @admin.register(CampusAVSReport)
# class CampusAVSReportAdmin(admin.ModelAdmin):
#     list_display = ['campusOrSchoolAcronym', 'program_type', 'year']
#     search_fields = ['campusOrSchoolAcronym', 'program_type']

# @admin.register(ReportImage)
# class ReportImageAdmin(admin.ModelAdmin):
#     list_display = ['campusOrSchoolAcronym', 'program_type']
#     search_fields = ['campusOrSchoolAcronym', 'program_type']

@admin.register(HistoryImage)
class HistoryImageAdmin(admin.ModelAdmin):
    list_display = ['campusOrSchoolAcronym', 'id', 'picture']
    search_fields = ['campusOrSchoolAcronym',]

