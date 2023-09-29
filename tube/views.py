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
from tm_api.utils import filter_equipment_by_criteria, get_ids

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




@api_view(["GET"])
def warehouse_equipment_view(request):
    slug =  request.query_params.get("slug")
    pm_status= str(request.query_params.get("pm_status")).upper()
    search= str(request.query_params.get("search"))
    date_str =  request.query_params.get("date")
    
    query = Q()
        
    if slug:
        query &= Q(location_for_warehouse__slug=slug)

    if pm_status != "NONE":
        query &= Q(pm_status=pm_status)

    if search != "None":
        query |= (
            Q(abbreviation__icontains=search)
            | Q(alternate_name__icontains=search)
            | Q(serial_number__icontains=search)
            | Q(asset_number__icontains=search)
            | Q(packaging__icontains=search)
        )
        
    
    p_qs = Project.objects.only("ttd", "bdd", "calibration_stand", "swabmaster_equip", 'equipment_delivery_client')
    
    if date_str:
        p_qs = p_qs.filter(equipment_delivery_client__gt=date_str)
    
    
    params = {
        "p_qs":p_qs,
        "query":query,
        "date_obj":date_str,
    }

    def get_ttd():
        qs = filter_equipment_by_criteria(flags={"ttds": 1},model_class=TTD, **params)
        
        serializer = TTDSerializers(qs, many=True)
        return serializer.data

    def get_bdd():
        qs = filter_equipment_by_criteria(flags={"bdds": 1},model_class=BDD, **params)
        
        serializer = BDDSerializer(qs, many=True)
        return serializer.data

    def get_calibration_stand():
        qs = filter_equipment_by_criteria(flags={"calis": 1},model_class=CALIBRATION_STAND, **params)
        serializer = CalibrationStandSerializer(qs, many=True)
        return serializer.data

    def get_swab_master():
        qs = filter_equipment_by_criteria(flags={"swabs": 1},model_class=SwabMaster, **params)
        serializer = SwabMasterSerializer(qs, many=True)
        return serializer.data

    ttd_data = get_ttd()
    bdd_data = get_bdd()
    calibration_stand_data = get_calibration_stand()
    swab_master_data = get_swab_master()

    ttd_count = len(ttd_data)
    bdd_count = len(bdd_data)
    calibration_stand_count = len(calibration_stand_data)
    swab_master_count = len(swab_master_data)

    merged_data = ttd_data + bdd_data + calibration_stand_data + swab_master_data

    pagination_class = CustomPagination()

    paginated_data = pagination_class.paginate_queryset(merged_data, request)

    paginated_data_with_counts = {
        "ttd_count": ttd_count,
        "bdd_count": bdd_count,
        "calibration_stand_count": calibration_stand_count,
        "swab_master_count": swab_master_count,
        "results": paginated_data,
    }
    return pagination_class.get_paginated_response(paginated_data_with_counts)
