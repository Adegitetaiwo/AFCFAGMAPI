
import imp
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import get_campus_avs_list, add_campus_avs_list, add_campus_avs_report, \
    get_campus_avs_report,add_campus_avs_report_images, get_campus_avs_report_images, \
    add_campus_avs_history_images, get_campus_avs_history_images



app_name = "CentralApp"

urlpatterns = [
    # campusAVS path
    path('get-all-campusavs/', get_campus_avs_list, name='get_campusavs_list'),
    path('add-campusavs/', add_campus_avs_list, name='add_campusavs_list'),

    path('add-report/', add_campus_avs_report, name='add_campusavs_report'),
    path('get-report/', get_campus_avs_report, name='get_campusavs_report'),

    path('add-report-images/', add_campus_avs_report_images, name='add_campusavs_report'),
    path('get-report-images/', get_campus_avs_report_images, name='get_campusavs_report'),

    path('add-history-images/', add_campus_avs_history_images, name='get_campusavs_report'),
    path('get-history-images/', get_campus_avs_history_images, name='get_campusavs_report'),


]
