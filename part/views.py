from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.permissions import  DjangoModelPermissions, IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import *
from .serializers import *

################################################################################
#                           UpddateAll View API Project
################################################################################
    

class SupplyOrificeViewPart(generics.ListAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes= [ JWTAuthentication]

    serializer_class = SupplyOrificeSerializer
    queryset = Supply_orifice.objects.all()


