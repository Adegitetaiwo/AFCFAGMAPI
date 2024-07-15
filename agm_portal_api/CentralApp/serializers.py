from rest_framework import serializers
from .models import CampusAVS, CampusAVSReport, ReportImage, HistoryImage

from rest_framework import status

# serializer to randomly query n number of quiz questions


class getCampusAvsListSerializers(serializers.ModelSerializer):

    def save(self):
        if CampusAVS.objects.filter(campusOrSchoolAcronym=self.validated_data['campusOrSchoolAcronym']).exists():
            updated_campusavs_list = CampusAVS.objects.filter(campusOrSchoolAcronym=self.validated_data['campusOrSchoolAcronym']).update(
            campusName=self.validated_data['campusName'],
            about=self.validated_data['about'],
            bibleStudyTime=self.validated_data['bibleStudyTime'],
            bibleStudyVenue=self.validated_data['bibleStudyVenue'],
            fellowshipTime=self.validated_data['fellowshipTime'],
            fellowshipVenue=self.validated_data['fellowshipVenue'],
            OtherScheduleOfServiceDetails=self.validated_data['OtherScheduleOfServiceDetails'],
            averageNumberOfStudent=self.validated_data['averageNumberOfStudent'],
            numberOfWorkforce=self.validated_data['numberOfWorkforce'],
                                                                
            coordinator_name = self.validated_data['coordinator_name'],
            coordinator_course = self.validated_data['coordinator_course'],
            coordinator_level = self.validated_data['coordinator_level'],
            coordinator_email = self.validated_data['coordinator_email'],
            coordinator_phonenumber = self.validated_data['coordinator_phonenumber'],
                                                                
            secretary_name = self.validated_data['secretary_name'],
            secretary_course = self.validated_data['secretary_course'],
            secretary_level = self.validated_data['secretary_level'],
            secretary_email = self.validated_data['secretary_email'],
            secretary_phonenumber = self.validated_data['secretary_phonenumber'],
        )
            return updated_campusavs_list
        
        else:

            campusavs_list = CampusAVS.objects.create(
                
                campusOrSchoolAcronym=self.validated_data['campusOrSchoolAcronym'],
                campusName=self.validated_data['campusName'],
                about=self.validated_data['about'],
                bibleStudyTime=self.validated_data['bibleStudyTime'],
                bibleStudyVenue=self.validated_data['bibleStudyVenue'],
                fellowshipTime=self.validated_data['fellowshipTime'],
                fellowshipVenue=self.validated_data['fellowshipVenue'],
                OtherScheduleOfServiceDetails=self.validated_data['OtherScheduleOfServiceDetails'],
                averageNumberOfStudent=self.validated_data['averageNumberOfStudent'],
                numberOfWorkforce=self.validated_data['numberOfWorkforce'],

                coordinator_name = self.validated_data['coordinator_name'],
                coordinator_course = self.validated_data['coordinator_course'],
                coordinator_level = self.validated_data['coordinator_level'],
                coordinator_email = self.validated_data['coordinator_email'],
                coordinator_phonenumber = self.validated_data['coordinator_phonenumber'],

                secretary_name = self.validated_data['secretary_name'],
                secretary_course = self.validated_data['secretary_course'],
                secretary_level = self.validated_data['secretary_level'],
                secretary_email = self.validated_data['secretary_email'],
                secretary_phonenumber = self.validated_data['secretary_phonenumber'],
                )
            return campusavs_list
        
    class Meta:
        model = CampusAVS
        fields = '__all__'
        
class getCampusAVSReportImageSerializers(serializers.ModelSerializer):
    
    def save(self):

        if ReportImage.objects.filter(campusOrSchoolAcronym=self.validated_data['campusOrSchoolAcronym'], program_type = self.validated_data['program_type']).exists():
            instance = ReportImage.objects.filter(campusOrSchoolAcronym=self.validated_data['campusOrSchoolAcronym'], program_type = self.validated_data['program_type']).update(
                campusOrSchoolAcronym = self.validated_data['campusOrSchoolAcronym'],
                program_type = self.validated_data['program_type'],
                picture1 = self.validated_data['picture1'],
                picture2 = self.validated_data['picture2'],
                picture3 = self.validated_data['picture3'],
                picture4 = self.validated_data['picture4'],
            )

            return instance
        else:
            instance = ReportImage.objects.create(
                campusOrSchoolAcronym = self.validated_data['campusOrSchoolAcronym'],
                program_type = self.validated_data['program_type'],
                picture1 = self.validated_data['picture1'],
                picture2 = self.validated_data['picture2'],
                picture3 = self.validated_data['picture3'],
                picture4 = self.validated_data['picture4'],
            )
            return instance
    
    class Meta:
        model = ReportImage
        fields = '__all__'


class getCampusAVSReportSerializers(serializers.ModelSerializer):

    class Meta:
        model = CampusAVSReport
        fields = '__all__'


class CampusAVSHistorySerializers(serializers.ModelSerializer):
    
    class Meta:
        model = HistoryImage
        fields = '__all__'


class updateCampusAVSReportSerializers(serializers.ModelSerializer):

    # def save(self):
    #     instance = CampusAVSReport.objects.get(campusOrSchoolAcronym=self.validated_data['campusOrSchoolAcronym'], program_type=self.validated_data['program_type']).update(
    #         year = self.validated_data['year'],
    #         salvation = self.validated_data['salvation'],
    #         sanctification = self.validated_data['sanctification'],
    #         baptism = self.validated_data['baptism'],
    #         healing = self.validated_data['healing'],
    #         TotalAttendanceMale = self.validated_data['TotalAttendanceMale'],
    #         TotalAttendanceFemale = self.validated_data['TotalAttendanceFemale'],
    #         TotalAttendance = self.validated_data['TotalAttendance'],

    #     )

    #     return instance
    class Meta:
        model = CampusAVSReport
        fields = '__all__'