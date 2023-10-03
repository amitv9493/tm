from dal import autocomplete
from django.shortcuts import render

# from notifications.models import Notification
from django.db.models import Q
from rest_framework import generics
from .models import Reactor
from client.models import Unit
from rest_framework.permissions import DjangoModelPermissions, IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import *
from .serializers import *

from rest_framework import filters


class ReactorAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Reactor.objects.none()

        qs = Reactor.objects.all()

        a = self.forwarded.get("client", None)
        b = self.forwarded.get("unit", None)

        if a and b:
            qs = qs.filter(Q(client=a) & Q(unit=b))

        if self.q:
            qs = None

        return qs


def front(request):
    context = {}
    return render(request, "index.html", context)


class UnitAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Unit.objects.none()

        qs = Unit.objects.all()

        a = self.forwarded.get("client", None)

        if a:
            return qs.filter(client=a)

        if self.q:
            qs = None


from client.models import Plant


class PlantAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Plant.objects.none()

        qs = Plant.objects.all()

        a = self.forwarded.get("client", None)
        if a:
            return qs.filter(client=a)

        if self.q:
            qs = None


def notification(request):
    qs = Notification.objects.all()
    qs1 = qs.filter(recipient=request.user)
    qs1 = qs1.unread()
    return render(request, "notification/notify.html", {"notifications": qs1})


###############################################################
#                   Client List-View
###############################################################

from tm_api.paginator import CustomPagination


class ClientListView(generics.ListAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]

    pagination_class = CustomPagination
    queryset = Client.objects.all()
    serializer_class = ClientSerializers

    filter_backends = [filters.SearchFilter]

    search_fields = [
        "official_name",
        "comman_name",
        "parent_company",
        "former_name",
    ]


class ClientListViewWithPagination(generics.ListAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]
    queryset = Client.objects.all()
    serializer_class = ClientSerializers


###############################################################
#                   Client Create-View
###############################################################


class ClientCreateView(generics.ListCreateAPIView):
    serializer_class = ClientCreateSerializers
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]

    queryset = Client.objects.all()
    # serializers_class = ClientSerializers


###############################################################
#                   Client RetUpdDel-View
###############################################################


class ClientRetUpddel(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]

    queryset = Client.objects.all()
    serializer_class = ClientCreateSerializers

    lookup_field = "slug"


###############################################################
#                   Address List-View
###############################################################


class AddressListView(generics.ListAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]

    queryset = Address.objects.all()
    serializer_class = AddressSerializers


###############################################################
#                   Address Create-View
###############################################################


class AddressCreateView(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]

    queryset = Address.objects.all()
    serializer_class = AddressCreateSerializers


###############################################################
#                   Address RetUpdDel-View
###############################################################


class AddressRetUpdDelView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]

    queryset = Address.objects.all()
    serializer_class = AddressCreateSerializers


###############################################################
#                   plant List-View
###############################################################

from django_filters.rest_framework import DjangoFilterBackend


class PlantListView(generics.ListAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]
    pagination_class = CustomPagination
    queryset = Plant.objects.all()
    serializer_class = PlantSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["client"]


###############################################################
#                   plant Create-View
###############################################################


class PlantCreateView(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]

    queryset = Plant.objects.all()
    serializer_class = PlantSerializersupdate


###############################################################
#                   plant RetUpdDel-View
###############################################################


class PlantRetUpdDelView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]

    queryset = Plant.objects.all()
    serializer_class = PlantSerializersupdate


###############################################################
#                   Reactor List-View
###############################################################


class ReactorListView(generics.ListAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]
    pagination_class = CustomPagination
    queryset = Reactor.objects.all()
    serializer_class = ReactorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["client"]


################################################################
#                   Reactor Create-View
################################################################


class ReactorCreateView(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]

    queryset = Reactor.objects.all()
    serializer_class = ReactorCreateSerializer


################################################################
#                   Reactor RetUpdDel-View
################################################################


class ReactorRetUpdDelView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]

    queryset = Reactor.objects.all()
    serializer_class = ReactorCreateSerializer


################################################################
#                   Unit List-View
################################################################


class UnitListView(generics.ListAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]
    pagination_class = CustomPagination
    queryset = Unit.objects.all()
    serializer_class = UnitSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["client"]


################################################################
#                   Unit Create-View
################################################################


class UnitCreateView(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]

    queryset = Unit.objects.all()
    serializer_class = UnitCreateSerializers


################################################################
#                   Unit RetUpdDel-View
################################################################


class UnitRetUpdDelView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]

    queryset = Unit.objects.all()
    serializer_class = UnitCreateSerializers
