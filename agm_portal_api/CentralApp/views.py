from django.shortcuts import render
from .models import CampusAVS, CampusAVSReport, ReportImage, HistoryImage

from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from datetime import datetime
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import generics, status, serializers
# Create your views here.

import io
from PIL import Image
import requests

from .serializers import getCampusAvsListSerializers, getCampusAVSReportSerializers, \
    updateCampusAVSReportSerializers, getCampusAVSReportImageSerializers, CampusAVSHistorySerializers

@api_view(['POST'])
def add_campus_avs_list(request):
    data = request.data or request.query_params
    data_copy = data.copy()
    if data_copy['averageNumberOfStudent'] == '':
        data_copy['averageNumberOfStudent'] = 0
    
    if data_copy['numberOfWorkforce'] == '':
        data_copy['numberOfWorkforce'] = 0

    serializer = getCampusAvsListSerializers(data=data_copy)

    if serializer.is_valid():
        serializer.save()

        return Response({
            'queryset': serializer.data
        }, status=status.HTTP_200_OK)
    else:
        return Response({
            'queryset': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def get_campus_avs_list(request):

    query = request.data or request.query_params
    # campus
    try:
        campus = query['campus']
        # query specific campus AVS in 'CampusAVS' Database
        queryset = CampusAVS.objects.filter(campusOrSchoolAcronym=campus)
        serializer = getCampusAvsListSerializers(queryset, many=True)
    
        return Response({
            'queryset': serializer.data
        }, status=status.HTTP_200_OK)   
    except Exception as e:
        # query all the CAMPUS avs in 'CampusAVS' Database
        queryset = CampusAVS.objects.all().order_by('id')
        serializer = getCampusAvsListSerializers(queryset, many=True)

        return Response({
            'queryset': serializer.data
        }, status=status.HTTP_200_OK)
    

@api_view(['GET'])
def get_campus_avs_report(request):

    query = request.data or request.query_params
    # campus
    try:
        campus = query['campus']
        program = query['program-type']
        # query specific campus AVS in 'CampusAVS' Database
        queryset = ReportImage.objects.filter(campusOrSchoolAcronym=campus, program_type = program)
        serializer = getCampusAVSReportSerializers(queryset, many=True)
    
        return Response({
            'queryset': serializer.data
        }, status=status.HTTP_200_OK)   
    except Exception as e:
        # query all the CAMPUS avs in 'CampusAVS' Database
        queryset = CampusAVSReport.objects.all().order_by('id')
        serializer = getCampusAVSReportSerializers(queryset, many=True)

        return Response({
            'queryset': serializer.data
        }, status=status.HTTP_200_OK)
    
@api_view(['POST'])
def add_campus_avs_report(request):
    data = request.data or request.query_params
    data_copy = data.copy()
    
    try:
    
        obj, created = CampusAVSReport.objects.update_or_create(
        campusOrSchoolAcronym=data_copy['campusOrSchoolAcronym'], program_type=data_copy['program_type'],
        defaults={'year': data_copy['year'],
                  'salvation': data_copy['salvation'],
                  'sanctification': data_copy['sanctification'],
                  'baptism': data_copy['baptism'],
                  'healing': data_copy['healing'],
                  'TotalAttendanceMale': data_copy['TotalAttendanceMale'],
                  'TotalAttendanceFemale': data_copy['TotalAttendanceFemale'],
                  'TotalAttendance': data_copy['TotalAttendance']
                  },
    )
        serializers = getCampusAVSReportSerializers(obj)

        return Response({
                'queryset': serializers.data
                }, status=status.HTTP_200_OK)

        # if CampusAVSReport.objects.filter(campusOrSchoolAcronym=data_copy['campusOrSchoolAcronym'], program_type=data_copy['program_type']).exists():
        #     instance = CampusAVSReport.objects.get(campusOrSchoolAcronym=data_copy['campusOrSchoolAcronym'], program_type=data_copy['program_type'])
        
        #     instance.delete(keep_parents=False)
           
           
        #     serializer = updateCampusAVSReportSerializers(data=data_copy)

        #     if serializer.is_valid():
        #         serializer.save()

        #         return Response({
        #             'queryset': serializer.data
        #         }, status=status.HTTP_200_OK)
        #     else:
        #         return Response({
        #             'queryset': serializer.errors
        #         }, status=status.HTTP_400_BAD_REQUEST)
        # else: 
        #     serializer = getCampusAVSReportSerializers(data=data_copy)
        
        #     if serializer.is_valid():
        #         serializer.save()

        #         return Response({
        #             'queryset': serializer.data
        #         }, status=status.HTTP_200_OK)
        #     else:
        #         return Response({
        #             'queryset': serializer.errors
        #         }, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        print(e)
        return Response({
                'code': 400,
                'status': 'Bad Request',
                'message': 'Internal error occured, check your Internet connection OR the API back-end code'
                }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def add_campus_avs_report_images(request):
    data = request.data or request.query_params
    data_copy = data.copy()
    serializer = getCampusAVSReportImageSerializers(data=data_copy)
    

    if serializer.is_valid():
        serializer.save()

        return Response({
            'queryset': {
                'campusOrSchoolAcronym': serializer.data['campusOrSchoolAcronym'],
                'program_type': serializer.data['program_type'],
            }
        }, status=status.HTTP_200_OK)
    
    else:
        return Response({
            'queryset': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_campus_avs_report_images(request):

    query = request.data or request.query_params
    # campus
    try:
        campus = query['campus']
        program = query['program-type']
        # query specific campus AVS in 'CampusAVS' Database
        queryset = ReportImage.objects.filter(campusOrSchoolAcronym=campus, program_type = program)
        serializer = getCampusAVSReportImageSerializers(queryset, many=True)
    
        return Response({
            'queryset': serializer.data
        }, status=status.HTTP_200_OK)   
    except Exception as e:
        # query all the CAMPUS avs in 'CampusAVS' Database
        queryset = ReportImage.objects.all().order_by('id')
        serializer = getCampusAVSReportImageSerializers(queryset, many=True)

        return Response({
            'queryset': serializer.data
        }, status=status.HTTP_200_OK)


@api_view(['POST'])
def add_campus_avs_history_images(request):
    data = request.data or request.query_params
    data_copy = data.copy()
    serializer = CampusAVSHistorySerializers(data=data_copy)
    

    if serializer.is_valid():
        serializer.save()

        return Response({
            'queryset': {
                'campusOrSchoolAcronym': serializer.data['campusOrSchoolAcronym'],
                'message': 'New Picture, Successfully Uploaded!',
            }
        }, status=status.HTTP_200_OK)
    
    else:
        return Response({
            'queryset': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_campus_avs_history_images(request):

    query = request.data or request.query_params
    # campus
    try:
        campus = query['campus']
        # query specific campus AVS in 'HistoryImage' Database
        queryset = HistoryImage.objects.filter(campusOrSchoolAcronym=campus)
        serializer = CampusAVSHistorySerializers(queryset, many=True)
    
        return Response({
            'queryset': serializer.data
        }, status=status.HTTP_200_OK) 
      
    except Exception as e:
        # query all the CAMPUS avs in 'CampusAVS' Database
        queryset =  HistoryImage.objects.all().order_by('id')
        serializer = CampusAVSHistorySerializers(queryset, many=True)

        return Response({
            'queryset': serializer.data
        }, status=status.HTTP_200_OK)

  



