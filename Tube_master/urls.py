# import notifications.urls
from django.contrib import admin
from django.urls import path
from tube import views
from django.conf import settings
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from client.views import (
    ReactorAutocomplete,
    UnitAutocomplete,
    PlantAutocomplete,
)
from tm_api.views import LoginView
from project.views import DashboardView
from project.views import projectview
from rest_framework_simplejwt.views import TokenRefreshView
from client.views import front
from tm_api.views import *
from part.views import *
from equipment.views import *
from client.views import *
from tube.views import *
from tm_api.views import UnitListView as tmAPIUnitView
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version="v1",
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


handler404 = "project.views.my_custom_page_not_found_view"
urlpatterns = (
    static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    + [
        path(
            "swagger<format>/",
            schema_view.without_ui(cache_timeout=0),
            name="schema-json",
        ),
        path(
            "swagger/",
            schema_view.with_ui("swagger", cache_timeout=0),
            name="schema-swagger-ui",
        ),
        path(
            "redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
        ),
        path("admin", admin.site.urls),
        path("", front, name="front"),
        #
        path("comment/", include("comment.urls")),
        path("projectdetail/<slug:slug>/", projectview, name="project-detail"),
        path(
            "reactor-autocomplete/",
            ReactorAutocomplete.as_view(),
            name="reactor-autocomplete",
        ),
        path(
            "unit-autocomplete/", UnitAutocomplete.as_view(), name="unit-autocomplete"
        ),
        path(
            "plant-autocomplete/",
            PlantAutocomplete.as_view(),
            name="plant-autocomplete",
        ),
        # path('unit-autocomplete/', UnitAutocomplete.as_view(), name='unit-autocomplete'),
        # path('',views.login,name='login'),
        path("accounts/", include("django.contrib.auth.urls")),  # new
        path(
            "change-password/",
            auth_views.PasswordChangeView.as_view(template_name="change-password.html"),
        ),
        # path("password_reset", views.password_reset_request, name="password_reset")
        path(
            "password_reset/done/",
            auth_views.PasswordResetDoneView.as_view(
                template_name="password_reset_done.html"
            ),
            name="password_reset_done",
        ),
        path(
            "reset/<uidb64>/<token>/",
            auth_views.PasswordResetConfirmView.as_view(
                template_name="password_reset_confirm.html"
            ),
            name="password_reset_confirm",
        ),
        path(
            "reset/done/",
            auth_views.PasswordResetCompleteView.as_view(
                template_name="password_reset_complete.html"
            ),
            name="password_reset_complete",
        ),
        # path('change-password/', auth_views.PasswordChangeView.as_view()),
        path("tube/", include("tube.urls")),
        # url('^inbox/notifications/', include(notifications.urls, namespace='notifications')),
        # path('inbox/',notification, name='unread-notifications'),
        # url(r'^chaining/', include('smart_selects.urls')),
        # path("select2/", include("django_select2.urls")),
        #######################################################################
        #                       Project API ENDPOINTS
        ###########################################`############################
        path("api/user/login/", LoginView.as_view(), name="loginview"),
        path(
            "api/get/clientlist/",
            ClientListViewWithPagination.as_view(),
            name="clientview",
        ),
        path("api/get/unitlist/", tmAPIUnitView.as_view(), name="unitview"),
        # NEW API
        path("api/get/scopeofwork/", ScopeOfWorkView.as_view(), name="scopeofwork"),
        path("api/get/ttd/", TtdView.as_view(), name="ttdview"),
        path("api/get/bdd/", BddView.as_view(), name="BddView"),
        path(
            "api/get/calibrationstand/", CalibrationStandView.as_view(), name="BddView"
        ),
        path("api/get/part/", PartView.as_view(), name="PartView"),
        path(
            "api/get/supplyorifice/",
            SupplyOrificeView.as_view(),
            name="SupplyOrificeView",
        ),
        path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
        path("api/get/reactor/", ReactorView.as_view(), name="ReactorView"),
        path(
            "api/get/pressuresensor/",
            PressureSensorView.as_view(),
            name="PressureSensorView",
        ),
        path(
            "api/get/calibrationorifice/",
            CalibrationOrificeView.as_view(),
            name="CalibrationOrificeView",
        ),
        path("api/get/swabmaster/", SwabMasterView.as_view(), name="SwabMasterView"),
        path("api/get/devicehose/", DeviceHoseView.as_view(), name="DeviceHoseView"),
        path("api/get/airhose/", AirHoseView.as_view(), name="AirHose"),
        # path('show/showrecord/<int:id>', views.showrecord, name='showrecord'),
        #######################################################################
        #                     Create API ENDPOINTS
        #######################################################################
        path("api/listproject/", ProjectAllListView.as_view(), name="listviewproject"),
        path(
            "api/createproject/",
            ProjectAllCreateView.as_view(),
            name="createviewproject",
        ),
        path(
            "api/alllist/project/<slug:slug>/",
            AallList_Id_Project.as_view(),
            name="alllistproject",
        ),
        path(
            "api/get/project/<slug:slug>/",
            getlList_Id_Project.as_view(),
            name="getproject",
        ),
        path(
            "api/update/project/<slug:slug>/",
            updateProject.as_view(),
        ),
        path(
            "api/alllist/patchproject/<slug:slug>/",
            AllList_Id_Patch_Project.as_view(),
            name="alllistproject",
        ),
        #######################################################################
        #                     Part API ENDPOINTS -- option api endpoint
        #######################################################################
        path(
            "api/get/option/supplyorificepart/",
            SupplyOrificeViewPart.as_view(),
            name="supplyorificepart",
        ),
        path(
            "api/get/option/pressuresensorpart/",
            PressureSensorViewPart.as_view(),
            name="pressuresensorpart",
        ),
        path(
            "api/get/option/ttdtubesealrackpart/",
            TTDTubeSealRackViewPart.as_view(),
            name="ttdtubesealrackpart",
        ),
        path(
            "api/get/option/bddtubesealrackpart/",
            BDDTubeSealRackViewPart.as_view(),
            name="bddtubesealrackpart",
        ),
        path(
            "api/get/option/swabmastertsrpart/",
            SwabMasterTSRViewPart.as_view(),
            name="swabmastertsrpart",
        ),
        path(
            "api/get/option/devicehoserpart/",
            DeviceHoseRViewPart.as_view(),
            name="devicehoserpart",
        ),
        path(
            "api/get/option/airhosepart/", AirHoseViewPart.as_view(), name="airhosepart"
        ),
        path(
            "api/get/option/warehouse/",
            WarehouseOptionListView.as_view(),
            name="warehouseoptionlistview",
        ),
        path(
            "api/get/option/calibrationorificepart/",
            CalibrationOrificeViewPart.as_view(),
            name="calibrationorificeviewpart",
        ),
        #######################################################################
        #                     Equipment-API ENDPOINTS
        #######################################################################
        path("api/eq/listttd/", TTDListView.as_view(), name="ttdlistview"),
        path("api/eq/createttd/", TTDCreateView.as_view(), name="ttdcreateview"),
        path(
            "api/eq/ttdretupddel/<slug:slug>/",
            TTDRetUpdDelView.as_view(),
            name="ttdretupddelview",
        ),
        path("api/eq/bddlist/", BDDListView.as_view(), name="bddlistview"),
        path("api/eq/bddcreate/", BDDCreateView.as_view(), name="bddcreateview"),
        path(
            "api/eq/bddretupddel/<slug:slug>/",
            BDDRetUpdDelView.as_view(),
            name="bddretupddelview",
        ),
        path(
            "api/eq/calibrationlist/",
            CalibrationStandListView.as_view(),
            name="calibrationlist",
        ),
        path(
            "api/eq/calibrationcreate/",
            CalibrationStandCreateView.as_view(),
            name="calibrationcreate",
        ),
        path(
            "api/eq/calibrationretupddel/<slug:slug>/",
            CalibrationRetUpdDelView.as_view(),
            name="calibrationretupddel",
        ),
        path(
            "api/eq/swabmasterlist/",
            SwabMasterListView.as_view(),
            name="swabmasterlist",
        ),
        path(
            "api/eq/swabmastercreate/",
            SwabMasterCreateView.as_view(),
            name="swabmastercreate",
        ),
        path(
            "api/eq/swabmasterretupddel/<slug:slug>/",
            SwabMasterRetUpdDelView.as_view(),
            name="swabmasterretupddel",
        ),
        #######################################################################
        #                     Client-API ENDPOINTS
        #######################################################################
        path("api/cl/clientlist/", ClientListView.as_view(), name="clientlist"),
        path("api/cl/clientcreate/", ClientCreateView.as_view(), name="clientcreate"),
        path(
            "api/cl/clientretupddel/<slug:slug>/",
            ClientRetUpddel.as_view(),
            name="clientretupddel",
        ),
        path("api/cl/addresslist/", AddressListView.as_view(), name="addresslist"),
        path(
            "api/cl/addresscreate/", AddressCreateView.as_view(), name="addresscreate"
        ),
        path(
            "api/cl/addressretupddel/<int:pk>/",
            AddressRetUpdDelView.as_view(),
            name="addressretupddel",
        ),
        path("api/cl/plantlist/", PlantListView.as_view(), name="plantlistview"),
        path("api/cl/plantcreate/", PlantCreateView.as_view(), name="plantcreate"),
        path(
            "api/cl/plantretupddel/<int:pk>/",
            PlantRetUpdDelView.as_view(),
            name="plantretupddel",
        ),
        path("api/cl/reactorlist/", ReactorListView.as_view(), name="reactorlist"),
        path(
            "api/cl/reactorcreate/", ReactorCreateView.as_view(), name="reactorcreate"
        ),
        path(
            "api/cl/reactorretupddel/<int:pk>/",
            ReactorRetUpdDelView.as_view(),
            name="reactorretupddel",
        ),
        path("api/cl/unitlist/", UnitListView.as_view(), name="unitlist"),
        path("api/cl/unitcreate/", UnitCreateView.as_view(), name="unitcreate"),
        path(
            "api/cl/unitretupddel/<int:pk>/",
            UnitRetUpdDelView.as_view(),
            name="unitretupddel",
        ),
        #######################################################################
        #                     Warehouse-API ENDPOINTS
        #######################################################################
        path("api/get/warehouse/", WarehouseListView.as_view(), name="getwarehouse"),
        path(
            "api/get/warehouse/wp/",
            WarehouseListViewWP.as_view(),
            name="getwarehousewp",
        ),
        path(
            "api/create/warehouse/",
            WarehouseCreateView.as_view(),
            name="createwarehouse",
        ),
        path(
            "api/retupddel/warehouse/<int:pk>/",
            WarehouseRetUpdDelView.as_view(),
            name="retupddelwarehouse",
        ),
        path("api/lw/<int:pk>/", WarehouseNewListView.as_view()),
        #######################################################################
        #                     Part-Crud-API ENDPOINTS
        #######################################################################
        path(
            "api/part/airhosecreate/", AirHoseCreateView.as_view(), name="airhosecreate"
        ),
        path(
            "api/part/airhoseretupddel/<slug:slug>/",
            AirHoseRetUpdDelView.as_view(),
            name="airhoseretupddel",
        ),
        path(
            "api/part/devicehoselist/",
            DeviceHoseRListView.as_view(),
            name="devicehoselist",
        ),
        path(
            "api/part/devicehosecreate/",
            DeviceHoseRCreateView.as_view(),
            name="devicehosecreate",
        ),
        path(
            "api/part/devicehoseretupddel/<slug:slug>/",
            DeviceHoseRetUpdDelView.as_view(),
            name="devicehoseretupddel",
        ),
        path(
            "api/part/swabmastertsrlist/",
            SwabMasterTSRListView.as_view(),
            name="swabmastertsrlist",
        ),
        path(
            "api/part/swabmastertsrcreate/",
            SwabMasterTSRCreateView.as_view(),
            name="swabmastertsrcreate",
        ),
        path(
            "api/part/swabmastertsrretupddrl/<slug:slug>/",
            SwabMasterTSRRetUpdDelViewl.as_view(),
            name="swabmastertsrretupddrl",
        ),
        path(
            "api/part/calibrationorificelist/",
            CalibrationOrificeListView.as_view(),
            name="calibrationorificelist",
        ),
        path(
            "api/part/calibrationorificecreate/",
            CalibrationOrificeCreateView.as_view(),
            name="calibrationorificecreate",
        ),
        path(
            "api/part/calibrationorificeretupddrl/<slug:slug>/",
            CalibrationOrificeRetUpdDelView.as_view(),
            name="calibrationorificeretupddrl",
        ),
        path(
            "api/part/bddtubesealracklist/",
            BddTubesealrackList.as_view(),
            name="bddtubesealracklist",
        ),
        path(
            "api/part/bddtubesealrackcreate/",
            BddTubesealrackCreate.as_view(),
            name="bddtubesealrackcreate",
        ),
        path(
            "api/part/bddtubesealrackretupddrl/<slug:slug>/",
            BddTubesealrackRetUpdDelView.as_view(),
            name="bddtubesealrackretupddrl",
        ),
        path(
            "api/part/tddtubesealracklist/",
            TddTubesealrackList.as_view(),
            name="tddtubesealracklist",
        ),
        path(
            "api/part/tddtubesealrackcreate/",
            TddTubesealrackCreate.as_view(),
            name="tddtubesealrackcreate",
        ),
        path(
            "api/part/tddtubesealrackretupddrl/<slug:slug>/",
            TddTubesealrackRetUpdDelView.as_view(),
            name="tddtubesealrackretupddrl",
        ),
        path(
            "api/part/pressuresensorlist/",
            PressureSensorListView.as_view(),
            name="pressuresensorlist",
        ),
        path(
            "api/part/pressuresensorcreate/",
            PressureSensorCreateView.as_view(),
            name="pressuresensorcreate",
        ),
        path(
            "api/part/pressuresensorretupddrl/<slug:slug>/",
            PressureSensorRetUpdDelView.as_view(),
            name="pressuresensorretupddrl",
        ),
        path(
            "api/part/supplyorificelist/",
            SupplyOrificeListView.as_view(),
            name="supplyorificelist",
        ),
        path(
            "api/part/supplyorificecreate/",
            SupplyOrificeCreateView.as_view(),
            name="supplyorificecreate",
        ),
        path(
            "api/part/supplyorificeretupddrl/<slug:slug>/",
            SupplyOrificeRetUpdDelView.as_view(),
            name="supplyorificeretupddrl",
        ),
        path(
            "api/part/allgeneralpartlist/",
            AllGeneralPartListView.as_view(),
            name="allgeneralpartlist",
        ),
        path(
            "api/part/allgeneralpartcreate/",
            AllGeneralPartCreateView.as_view(),
            name="allgeneralpartcreate",
        ),
        path(
            "api/part/allgeneralpartretupddel/<slug:slug>/",
            AllGeneralPartRetUpdDelView.as_view(),
            name="allgeneralpartretupddel",
        ),
        path("api/wa/", WarehouseAvailabilityView.as_view()),
        # path('api/equip/', WarehouseEquipmentView.as_view()),
        path("api/wef/", warehouse_equipment_view),
        path("api/wp/", warehouse_part_view),
        path("api/wp/general-parts/", AllGeneralPart.as_view()),
        path("api/task/", TaskView.as_view()),
        # new equipments view
        path("api/get/new/ttd/", TTDNewView.as_view(), name="ttdnewview"),
        path("api/get/new/bdd/", BddNewView.as_view()),
        path("api/get/new/calibrationstand/", CalibrationStandNewView.as_view()),
        path("api/get/new/swabmaster/", SwabMasterEquipmentView.as_view()),
        # path("api/get/new/ttd/swabmaster/",SwabMasterNewView.as_view()),
        # new parts views
        path("api/get/new/supplyorifice/", SupplyOrificeNewView.as_view()),
        path("api/get/new/parts/", PartNewView.as_view()),
        path("api/get/new/pressuresensor/", PressureSensorNewView.as_view()),
        path("api/get/new/swabmastertsr/", SwabMasterNewView.as_view()),
        path("api/get/new/devicehose/", DeviceHoseNewView.as_view()),
        path("api/get/new/airhose/", AirHoseNewView.as_view()),
        path("api/get/new/calibration-orifice/", CalibrationOrificeNewView.as_view()),
        ##########################################################################
        # '''DASHBOARD ENDPOINTS'''
        ##########################################################################""
        path("project-reports/<int:pk>/", ProjectRecordView.as_view()),
        path("api/dashboard/", DashboardView.as_view()),
        path("silk/", include("silk.urls", namespace="silk")),
        re_path(".*", front, name="front"),
        # re_path(r"^.*", front, name="front"),
    ]
)
# if settings.DEBUG:
