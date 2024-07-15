from django.contrib import admin
from .models import CampusAVS, CampusAVSReport, ReportImage, HistoryImage
# Register your models here.

admin.site.site_header = 'AFCF AGM PORTAL'


@admin.register(CampusAVS)
class CampusAVSAdmin(admin.ModelAdmin):
    list_display = ['campusOrSchoolAcronym', 'campusName', 'averageNumberOfStudent', 'numberOfWorkforce']

@admin.register(CampusAVSReport)
class CampusAVSReportAdmin(admin.ModelAdmin):
    list_display = ['campusOrSchoolAcronym', 'program_type', 'year']

@admin.register(ReportImage)
class ReportImageAdmin(admin.ModelAdmin):
    list_display = ['campusOrSchoolAcronym', 'program_type']

@admin.register(HistoryImage)
class HistoryImageAdmin(admin.ModelAdmin):
    list_display = ['campusOrSchoolAcronym', 'id']

