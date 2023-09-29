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


import time
from silk.profiling.profiler import silk_profile

@silk_profile(name='warehouse_equipment_view')
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
        
    
    p_qs = Project.objects.values("ttd", "bdd", "calibration_stand", "swabmaster_equip", 'equipment_delivery_client')
    
    
    if date_str:
        p_qs = p_qs.filter(equipment_delivery_client__gt=date_str)        

    ttd_qs = TTD.objects.filter(query)\
    .select_related("location_for_warehouse",
                    "TTD_tube_seal_rack",
                    "pressure_sensor",
                    "supply_orifice_set",
                    )
    bdd_qs = BDD.objects.filter(query)\
    .select_related("location_for_warehouse",
                    "BDD_tube_seal_rack",
                    )
    cali_qs = CALIBRATION_STAND.objects.filter(query)\
    .select_related("location_for_warehouse",
                    "calibration_orifice_set",
                    )
    swab_qs = SwabMaster.objects.filter(query)\
    .select_related("location_for_warehouse",
                    "Swab_Master_Tube_Seal_Rack",
                    )
    
    if date_str:
        ttd_qs = ttd_qs.exclude(id__in = get_ids(p_qs, ttds= 1))
        bdd_qs = bdd_qs.exclude(id__in = get_ids(p_qs, bdds = 1))
        cali_qs = cali_qs.exclude(id__in =get_ids(p_qs,calis = 1))
        swab_qs = swab_qs.exclude(id__in = get_ids(p_qs, swabs= 1))
        
    ttd_data = TTDSerializers(ttd_qs, many=True).data
    bdd_data = BDDSerializer(bdd_qs, many=True).data
    cali_data = CalibrationStandSerializer(cali_qs, many=True).data
    swab_data = SwabMasterSerializer(swab_qs, many=True).data
    
    ttd_count = (ttd_qs).count()
    bdd_count = (bdd_qs).count()
    calibration_stand_count = (cali_qs).count()
    swab_master_count = swab_qs.count()

    # w =  swab_serializer.data # less time
    # z = cali_serializer.data # less time
    # y =  bdd_serializer.data # more time
    # x = ttd_serializer.data # more time
    # start = time.time()
    # print("time taken", time.time() - start)
        
    merged_data = ttd_data + swab_data + bdd_data + cali_data
    
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
    