
import imp
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import get_campus_avs_list, add_campus_avs_list, add_campus_avs_report, \
    get_campus_avs_report, \
    add_campus_avs_history_images, get_campus_avs_history_images, get_index_page, get_program_activities, get_campus_avs_history_images_as_list



app_name = "CentralApp"

urlpatterns = [
    # campusAVS path
    path('get-idex-data/', get_index_page, name='get_index_page'),
    path('get-program-activities/', get_program_activities, name='get_program_activities'),


    path('get-all-campusavs/', get_campus_avs_list, name='get_campusavs_list'),
    path('add-campusavs/', add_campus_avs_list, name='add_campusavs_list'),

    path('add-report/', add_campus_avs_report, name='add_campusavs_report'),
    path('get-report/', get_campus_avs_history_images_as_list, name='get_campusavs_report'),

    path('add-history-images/', add_campus_avs_history_images, name='get_campusavs_report'),
    path('get-history-images/', get_campus_avs_history_images, name='get_campusavs_report'),


]
