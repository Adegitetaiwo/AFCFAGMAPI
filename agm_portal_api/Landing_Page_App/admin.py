from django.contrib import admin
from .models import WebPageIndexData, ProgramSchedule

# Register your models here.

@admin.register(WebPageIndexData)
class WebPageIndexDataAdmin(admin.ModelAdmin):
    list_display = ['event_name', 'event_Live_link', 'posted']


@admin.register(ProgramSchedule)
class ProgramScheduleAdmin(admin.ModelAdmin):
    list_display = ['program_activity_title', 'activity_timeline']


# @admin.register(HistoryImage)
# class HistoryImageAdmin(admin.ModelAdmin):
#     list_display = ['campusOrSchoolAcronym', 'id', 'picture']
#     search_fields = ['campusOrSchoolAcronym',]