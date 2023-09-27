from tm_api.paginator import CustomPagination
from tube.models import Warehouse
from rest_framework import generics
from .models import Warehouse
from django.http import Http404
from .serializers import WarehouseSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from tube.serializers import *
from rest_framework.permissions import DjangoModelPermissions, IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication


class WarehouseView(generics.ListCreateAPIView):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer


class WarehouseIDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer

    def handle_exception(self, exc):
        if isinstance(exc, Http404):
            if "No Warehouse matches the given query." in exc.args:
                message = "The requested resource was not found."
                return Response({"message": message}, status=204)

        # For all other exceptions, use the default DRF exception handler
        return super().handle_exception(exc)


#######################################################################
#                     WarehouseOptionListView for options
#######################################################################


class WarehouseOptionListView(generics.ListAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseOptionsSerializer


class WarehouseAvailabilityView(generics.ListAPIView):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseAvailableSerializer

    def get_queryset(self):
        qs = super().get_queryset()

        id = self.request.GET.get("id")
        slug = self.request.GET.get("slug")

        if slug:
            return qs.filter(slug=slug)

        if id:
            return qs.filter(slug=id)

        return qs




class WarehouseEquipmentView(generics.ListAPIView):
    serializer_class = WarehouseEquipSerializer
    queryset = Warehouse.objects.all()
    pagination_class = CustomPagination

    def get_queryset(self):
        qs = super().get_queryset()
        id = self.request.GET.get("id")
        if id:
            return qs.filter(id=id)

        return qs


@api_view(["GET"])
def warehouse_equipment_view(request):
    pagination_class = CustomPagination()

    serializer = WarehouseEquipSerializer(context={"request": request})

    ttd_data = serializer.get_ttd(None)
    bdd_data = serializer.get_bdd(None)
    calibration_stand_data = serializer.get_calibration_stand(None)
    swab_master_data = serializer.get_swab_master(None)

    ttd_count = len(ttd_data)
    bdd_count = len(bdd_data)
    calibration_stand_count = len(calibration_stand_data)
    swab_master_count = len(swab_master_data)

    merged_data = ttd_data + bdd_data + calibration_stand_data + swab_master_data

    paginated_data = pagination_class.paginate_queryset(merged_data, request)

    paginated_data_with_counts = {
        "ttd_count": ttd_count,
        "bdd_count": bdd_count,
        "calibration_stand_count": calibration_stand_count,
        "swab_master_count": swab_master_count,
        "results": paginated_data,
    }
    return pagination_class.get_paginated_response(paginated_data_with_counts)
