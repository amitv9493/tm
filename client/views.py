from dal import autocomplete
from django.db.models import Q
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics
from rest_framework.permissions import DjangoModelPermissions, IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication

from client.models import Address, Client, Plant, Reactor, Unit
from client.serializers import (
    AddressCreateSerializers,
    AddressSerializers,
    ClientCreateSerializers,
    ClientSerializers,
    PlantSerializers,
    PlantSerializersupdate,
    ReactorCreateSerializer,
    ReactorSerializer,
    UnitCreateSerializers,
    UnitSerializers,
)
from tm_api.paginator import CustomPagination


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


###############################################################
#                   Client List-View
###############################################################


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

    def paginate_queryset(self, queryset):
        if self.request.query_params.get("paginate", None) == "false":
            return None
        return super().paginate_queryset(queryset)


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
