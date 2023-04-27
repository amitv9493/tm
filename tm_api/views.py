from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from .serializers import LoginSerializer, UserProfileSerializer
from django.contrib.auth.models import Group
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.generics import ListAPIView


from rest_framework.viewsets import ModelViewSet
# from .persmissions import Mypermission
from rest_framework.permissions import  DjangoModelPermissions, IsAdminUser
from rest_framework import authentication
from django.db.models import Q
from .serializers import *
# from application.models import Application
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics
# from django_filters.rest_framework import DjangoFilterBackend
# from .renderers import UserRenderes
# from .paginator import CustomPagination
# from enquiry.models import Course
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.filters import SearchFilter

from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.filters import OrderingFilter
from .paginator import CustomPagination
from project.models import *
from part.models import *
from equipment.models import *
# Create your views here.

###################################################################################
#            Login API View
################################################################################### 

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class LoginView(APIView):
    
    def post(self,request, format =None ):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # email = serializer.data.get('email')
            username= serializer.data.get('username')
            password= serializer.data.get('password')
            user =authenticate(username=username, password=password)
                                                                    
            if user is not None:
                try:
                    user_group = (Group.objects.get(user=user.id)).name
                except Exception as e:
                    print("No group assigned to user")
                    user_group = "None"
                    
               
                token= get_tokens_for_user(user)
                return Response({"token":token,"msg":"Login Successful","userid":user.id,"user_status":user_group}, status=status.HTTP_200_OK)

            return Response({"errors":{"msg":-1}}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
    

###################################################################################
#            Client API View
################################################################################### 
from .paginator import CustomPagination
class ClientListView(ListAPIView):
    
    # pagination_class = CustomPagination
    # permission_classes = [DjangoModelPermissions, IsAdminUser]
    # authentication_classes= [ JWTAuthentication]
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

###################################################################################
#            Unit API View
################################################################################### 

class UnitListView(ListAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [ JWTAuthentication ]
    
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    
###################################################################################
#            ScopeOfWork API View
################################################################################### 
    
class ScopeOfWorkView(ListAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [ JWTAuthentication ]
    queryset = Scope_of_work.objects.all()
    serializer_class = SOWSerializer 
    
    
###################################################################################
#            Reactor API View
################################################################################### 


class ReactorView(ListAPIView):
    # permission_classes = [DjangoModelPermissions, IsAdminUser]
    # authentication_classes = [ JWTAuthentication ]
    # queryset = Unit.objects.all()
    serializer_class = ReactorSerializer
    def get_queryset(self):
        # qs =  super().get_queryset()
        client_id = self.request.query_params.get('client')
        unit_id = self.request.query_params.get('unit')
        print(client_id)
        print(unit_id)
        queryset = Reactor.objects.filter(client = client_id, unit = unit_id)
        return queryset

    
################################################################################
#                    TTD API View
################################################################################ 


# from django.db import Q

# class TtdView(ListAPIView):
#     permission_classes = [DjangoModelPermissions, IsAdminUser]
#     authentication_classes= [ JWTAuthentication]
#     queryset  = TTD.objects.all()
#     serializer_class = TtdSerializer


#     def get_queryset(self):
#         qs =  super().get_queryset()
        
#         start_date = self.request.query_params.get('start_date')
#         end_date = self.request.query_params.get('end_date')
#         print(start_date)
#         print(end_date)
#         # Q()
#         qs = Project.objects.filter(equipment_prep__gte = start_date ,equipment_delivery_tubemaster__lte = end_date)

#         # print(qs.ttd)
#         ttd  = set()
#         for i in qs:
#             for i in i.ttd.all():
#                 ttd.add(i.id)

#         ttd = list(ttd)
#         ttd_qs = TTD.objects.exclude(id__in = ttd)
#         return (ttd_qs)

class TtdView(ListAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes= [ JWTAuthentication]
    queryset  = TTD.objects.all()
    serializer_class = TtdSerializer
    def get_queryset(self):
        qs =  super().get_queryset()
        
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')
        pro_id = self.request.query_params.get('proid')
        print(start_date)
        print(end_date)
        # Q()
        qs = Project.objects.filter(equipment_prep__gte = start_date ,equipment_delivery_tubemaster__lte = end_date)
        if pro_id:
            qs = qs.exclude(id=pro_id)

        ttd  = set()
        for i in qs:
            for i in i.ttd.all():
                ttd.add(i.id)
        ttd = list(ttd)
        ttd_qs = TTD.objects.exclude(id__in = ttd)
        return (ttd_qs)

################################################################################
#            BDD API View
################################################################################  
    
class BddView(ListAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes= [ JWTAuthentication]
    queryset  = BDD.objects.all()
    serializer_class = BddSerializer


    def get_queryset(self):
        qs =  super().get_queryset()

        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')
        pro_id = self.request.query_params.get('proid')
        print(start_date)
        print(end_date)
        # Q()
        qs = Project.objects.filter(equipment_prep__gte = start_date ,equipment_delivery_tubemaster__lte = end_date)
        if pro_id:
            qs = qs.exclude(id=pro_id)
        # print(qs.ttd)
        bdd  = set()
        for i in qs:
            for i in i.bdd.all():
                bdd.add(i.id)

        bdd = list(bdd)
        bdd_qs = BDD.objects.exclude(id__in = bdd)
        return (bdd_qs)

################################################################################
#            Calibration API View
################################################################################

class CalibrationStandView(ListAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes= [ JWTAuthentication]
    queryset  = CALIBRATION_STAND.objects.all()
    serializer_class = CALIBRATION_STANDSerializer


    def get_queryset(self):
        qs =  super().get_queryset()

        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')
        pro_id = self.request.query_params.get('proid')
        print(start_date)
        print(end_date)
        # Q()
        qs = Project.objects.filter(equipment_prep__gte = start_date ,equipment_delivery_tubemaster__lte = end_date)
        if pro_id:
            qs = qs.exclude(id=pro_id)
        # print(qs.ttd)
        CALIBRATIONSTAND  = set()
        for i in qs:
            for i in i.bdd.all():
                CALIBRATIONSTAND.add(i.id)

        CALIBRATIONSTAND = list(CALIBRATIONSTAND)
        CALIBRATIONSTAND_qs = CALIBRATION_STAND.objects.exclude(id__in = CALIBRATIONSTAND)
        return (CALIBRATIONSTAND_qs)
    
################################################################################
#            Part API View
################################################################################    

class PartView(ListAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes= [ JWTAuthentication]
    queryset  = Part.objects.all()
    serializer_class = PartSerializer


    def get_queryset(self):
        qs =  super().get_queryset()

        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')
        pro_id = self.request.query_params.get('proid')
        # Q()
        qs = Project.objects.filter(equipment_prep__gte = start_date ,equipment_delivery_tubemaster__lte = end_date)
        if pro_id:
            qs = qs.exclude(id=pro_id)
        # print(qs.ttd)
        part  = set()
        for i in qs:
            for i in i.part.all():
                part.add(i.id)

        part = list(part)
        Part_qs = Part.objects.exclude(id__in = part)
        return (Part_qs)

################################################################################
#            SupplyOrifice API View
################################################################################    
    
class SupplyOrificeView(ListAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes= [ JWTAuthentication]
    queryset  = Supply_orifice.objects.all()
    serializer_class = SupplyOrificeSerializer


    def get_queryset(self):
        qs =  super().get_queryset()

        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')
        pro_id = self.request.query_params.get('proid')
        # Q()
        qs = Project.objects.filter(equipment_prep__gte = start_date ,equipment_delivery_tubemaster__lte = end_date)
        if pro_id:
            qs = qs.exclude(id=pro_id)
        # print(qs.ttd)
        supply_orifice_part  = set()
        for i in qs:
            for i in i.supply_orifice_part.all():
                supply_orifice_part.add(i.id)

        supply_orifice_part = list(supply_orifice_part)
        supply_orifice_part_qs = Supply_orifice.objects.exclude(id__in = supply_orifice_part)
        return (supply_orifice_part_qs)


################################################################################
#            Pressure API View
################################################################################ 


class PressureSensorView(ListAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [ JWTAuthentication ]
    queryset  = Pressure_sensor.objects.all()
    serializer_class = PressureSensorSerializer


    def get_queryset(self):
        qs =  super().get_queryset()
    
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')
        pro_id = self.request.query_params.get('proid')
        # Q()
        qs = Project.objects.filter(equipment_prep__gte = start_date ,equipment_delivery_tubemaster__lte = end_date)
        if pro_id:
            qs = qs.exclude(id=pro_id)
        # print(qs.ttd)
        pressure_sensor_part  = set()
        for i in qs:
            for i in i.pressure_sensor_part.all():
                pressure_sensor_part.add(i.id)

        pressure_sensor_part = list(pressure_sensor_part)
        pressure_sensor_part_qs = Pressure_sensor.objects.exclude(id__in = pressure_sensor_part)
        return (pressure_sensor_part_qs)

################################################################################
#            calibrtion orofic API View
################################################################################ 
class CalibrationOrificeView(ListAPIView):
    queryset  = Calibration_orifice.objects.all()
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [ JWTAuthentication ]
    serializer_class = CalibrationOrificeSerializer


    def get_queryset(self):
        qs =  super().get_queryset()

        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')
        pro_id = self.request.query_params.get('proid')
        # Q()
        qs = Project.objects.filter(equipment_prep__gte = start_date ,equipment_delivery_tubemaster__lte = end_date)
        if pro_id:
            qs = qs.exclude(id=pro_id)
        # print(qs.ttd)
        pressure_sensor_part  = set()
        for i in qs:
            for i in i.calibration_orifice_part.all():
                pressure_sensor_part.add(i.id)

        pressure_sensor_part = list(pressure_sensor_part)
        pressure_sensor_part_qs = Calibration_orifice.objects.exclude(id__in = pressure_sensor_part)
        return (pressure_sensor_part_qs)

################################################################################
#            swabmaster API View
################################################################################ 
class SwabMasterView(ListAPIView):
    queryset  = SwabMasterTSR.objects.all()
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [ JWTAuthentication ]
    serializer_class = SwabMasterSerializer


    def get_queryset(self):
        qs =  super().get_queryset()

        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')
        pro_id = self.request.query_params.get('proid')
        # Q()
        qs = Project.objects.filter(equipment_prep__gte = start_date ,equipment_delivery_tubemaster__lte = end_date)
        if pro_id:
            qs = qs.exclude(id=pro_id)
        # print(qs.ttd)
        pressure_sensor_part  = set()
        for i in qs:
            for i in i.swabmaster_part.all():
                pressure_sensor_part.add(i.id)

        pressure_sensor_part = list(pressure_sensor_part)
        pressure_sensor_part_qs = SwabMasterTSR.objects.exclude(id__in = pressure_sensor_part)
        return (pressure_sensor_part_qs)
 
 
################################################################################
#            Devicehose API View
################################################################################   
class DeviceHoseView(ListAPIView):
    queryset  = DeviceHose.objects.all()
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [ JWTAuthentication ]
    serializer_class = DeviceHoseSerializer


    def get_queryset(self):
        qs =  super().get_queryset()

        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')
        pro_id = self.request.query_params.get('proid')
        # Q()
        qs = Project.objects.filter(equipment_prep__gte = start_date ,equipment_delivery_tubemaster__lte = end_date)
        if pro_id:
            qs = qs.exclude(id=pro_id)
        # print(qs.ttd)
        pressure_sensor_part  = set()
        for i in qs:
            for i in i.device_part.all():
                pressure_sensor_part.add(i.id)

        pressure_sensor_part = list(pressure_sensor_part)
        pressure_sensor_part_qs = DeviceHose.objects.exclude(id__in = pressure_sensor_part)
        return (pressure_sensor_part_qs)

################################################################################
#            Airhose API View
################################################################################   
class AirHoseView(ListAPIView):
    queryset  = AirHose.objects.all()
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [ JWTAuthentication ]
    serializer_class = AirHoseSerializer


    def get_queryset(self):
        qs =  super().get_queryset()

        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')
        pro_id = self.request.query_params.get('proid')
        # Q()
        qs = Project.objects.filter(equipment_prep__gte = start_date ,equipment_delivery_tubemaster__lte = end_date)
        if pro_id:
            qs = qs.exclude(id=pro_id)
        # print(qs.ttd)
        pressure_sensor_part  = set()
        for i in qs:
            for i in i.airhose_part.all():
                pressure_sensor_part.add(i.id)

        pressure_sensor_part = list(pressure_sensor_part)
        pressure_sensor_part_qs = AirHose.objects.exclude(id__in = pressure_sensor_part)
        return (pressure_sensor_part_qs)


################################################################################
#                           All List View API Project
################################################################################

from rest_framework import authentication
from rest_framework import filters

class ProjectAllListView(generics.ListAPIView):
    
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['created_at',]
    ordering = ['created_at']
    # permission_classes = [DjangoModelPermissions, IsAdminUser]
    # authentication_classes= [ JWTAuthentication]
    queryset = Project.objects.all()
    serializer_class = Add_Project_serializer
    pagination_class = CustomPagination
    
    

    def perform_create(self, add_project_serializer):
        pass
        # add_project_serializer.save(created_by=self.request.user)
        
################################################################################
#                        All Create View API Project
################################################################################
    
class ProjectAllCreateView(generics.CreateAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes= [ JWTAuthentication]
    queryset = Project.objects.all()
    serializer_class = Create_Project_Serializer
    
    
    # def perform_create(self, Create_Project_Serializer):
    #     Create_Project_Serializer.save(created_by=self.request.user)
    #     return super().perform_create(Create_Project_Serializer)
    
################################################################################
#                           ListAll View API Project
################################################################################

class AallList_Id_Project(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes= [ JWTAuthentication]
    
    serializer_class = Add_Project_serializer
    queryset = Project.objects.all()
    
    
################################################################################
#                           get 1 project with no depth View API Project
################################################################################

class getlList_Id_Project(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [DjangoModelPermissions, IsAdminUser]
    # authentication_classes= [ JWTAuthentication]
    
    serializer_class = GET_Project_serializer
    queryset = Project.objects.all()
         
################################################################################
#                           UpddateAll View API Project
################################################################################
    

class AallList_Id_Patch_Project(generics.RetrieveUpdateAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes= [ JWTAuthentication]

    serializer_class = All_Project_Patch_serializer
    queryset = Project.objects.all()





















