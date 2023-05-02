from django.shortcuts import render
from .models import TTD, BDD
from .serializers import TTDSerializers, BDDSerializer
from rest_framework.generics import ListAPIView
from rest_framework import generics
from rest_framework.permissions import DjangoModelPermissions, IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication


##################################################################
#       TTD List-View
##################################################################


class TTDListView(ListAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]

    queryset = TTD.objects.all()
    serializer_class = TTDSerializers


##################################################################
#       TTD Create-View
##################################################################

class TTDCreateView(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]

    queryset = TTD.objects.all()
    serializer_class = TTDSerializers


##################################################################
#       TTD RetrieveUpdateDelete-View
##################################################################

class TTDRetUpdDelView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]

    queryset = TTD.objects.all()
    serializer_class = TTDSerializers


##################################################################
#       BDD List-View
##################################################################

class BDDListView(generics.ListAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes =[JWTAuthentication]

    queryset = BDD.objects.all()
    serializer_class = BDDSerializer

    