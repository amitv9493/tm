# import notifications.urls
from django.contrib import admin
from django.urls import path
from tube import views
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.conf.urls.i18n import i18n_patterns
from client.views import (ReactorAutocomplete,UnitAutocomplete,PlantAutocomplete,)
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

    
urlpatterns = static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) +  [
    
    path("", front, name="front"),
    path("admin/", admin.site.urls),
    path("comment/", include("comment.urls")),
    path("projectdetail/<int:pk>/", projectview, name="project-detail"),
    path("reactor-autocomplete/",ReactorAutocomplete.as_view(),name="reactor-autocomplete"),
    path("unit-autocomplete/", UnitAutocomplete.as_view(), name="unit-autocomplete"),
    path("plant-autocomplete/", PlantAutocomplete.as_view(), name="plant-autocomplete"),
    # path('unit-autocomplete/', UnitAutocomplete.as_view(), name='unit-autocomplete'),
    # path('',views.login,name='login'),
    path("logout/", views.logout, name="logout"),
    path("register/", views.register, name="register"),
    path("accounts/", include("django.contrib.auth.urls")),  # new
    path("change-password/",auth_views.PasswordChangeView.as_view(template_name="change-password.html")),
    # path("password_reset", views.password_reset_request, name="password_reset")
    path("password_reset/done/",auth_views.PasswordResetDoneView.as_view(template_name="password_reset_done.html"),name="password_reset_done"),
    path("reset/<uidb64>/<token>/",auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"),name="password_reset_confirm"),
    path("reset/done/",auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"),name="password_reset_complete"),
    # path('change-password/', auth_views.PasswordChangeView.as_view()),
    path("tube/", include("tube.urls")),
    path("users/", views.users, name="users"),
    path("user_profile/", views.user_profile, name="user_profile"),
    path("search_clients/", views.search_clients, name="search_clients"),
    path("search_plants/", views.search_plants, name="search_plants"),
    path("search_units/", views.search_units, name="search_units"),
    path("search_reactors/", views.search_reactors, name="search_reactors"),
    path("search_warehouse/", views.search_warehouse, name="search_warehouse"),
    path("search_ttd/", views.search_ttd, name="search_ttd"),
    path("search_bdd/", views.search_bdd, name="search_bdd"),
    path("search_calstand/", views.search_calstand, name="search_calstand"),
    path("clients/", views.clients, name="clients"),
    path("projects/", views.projects, name="projects"),
    path("client_profile/", views.client_profile, name="client_profile"),
    path("project_detail/", views.project_detail, name="project_detail"),
    path("update/<int:id>", views.update, name="update"),
    path("update/updaterecord/<int:id>", views.updaterecord, name="updaterecord"),
    path("delete/<int:id>", views.delete, name="delete"),
    path("show/<int:client_id>", views.show, name="show"),
    path("warehouse/", views.warehouse, name="warehouse"),
    path("warehouse_detail/", views.warehouse_detail, name="warehouse_detail"),
    path("updatewarehouse/<int:id>", views.updatewarehouse, name="updatewarehouse"),
    path("updatewarehouse/updatewarehouserecord/<int:id>",views.updatewarehouserecord,name="updatewarehouserecord",),
    path("updatettd/<int:id>", views.updatettd, name="updatettd"),
    path("updatettd/updatettdrecord/<int:id>",views.updatettdrecord,name="updatettdrecord"),
    path("updateproject/<int:id>", views.updateproject, name="updateproject"),
    path("updateproject/updateprojectrecord/<int:id>",views.updateprojectrecord,name="updateprojectrecord",),
    path("updatebdd/<int:id>", views.updatebdd, name="updatebdd"),
    path("updatebdd/updatebddrecord/<int:id>",views.updatebddrecord,name="updatebddrecord"),
    path("updatecalstand/<int:id>", views.updatecalstand, name="updatecalstand"),
    path("updatecalstand/updatecalstandrecord/<int:id>",views.updatecalstandrecord,name="updatecalstandrecord"),
    path("deletewarehouse/<int:id>", views.deletewarehouse, name="deletewarehouse"),
    path("showwarehouse/<int:warehouse_id>", views.showwarehouse, name="showwarehouse"),
    path("showproject/<int:project_id>", views.showproject, name="showproject"),
    path("deleteplant/<int:id>", views.deleteplant, name="deleteplant"),
    path("deleteunit/<int:id>", views.deleteunit, name="deleteunit"),
    path("deletereactor/<int:id>", views.deletereactor, name="deletereactor"),
    path("deletettd/<int:id>", views.deletettd, name="deletettd"),
    path("deleteproject/<int:id>", views.deleteproject, name="deleteproject"),
    path("showplant/<int:id>", views.showplant, name="showplant"),
    path("updateplant/<int:id>", views.updateplant, name="updateplant"),
    path("updateplant/updateplantrecord/<int:id>",views.updateplantrecord,name="updateplantrecord"),
    path("updateunit/<int:id>", views.updateunit, name="updateunit"),
    path("updateunit/updateunitrecord/<int:id>",views.updateunitrecord,name="updateunitrecord"),
    path("updatereactor/<int:id>", views.updatereactor, name="updatereactor"),
    path("updatereactor/updatereactorrecord/<int:id>",views.updatereactorrecord,name="updatereactorrecord"),
    path("contacts/", views.contacts, name="contacts"),
    path("equipments/", views.equipments, name="equipments"),
    path("plants/", views.plants, name="plants"),
    path("units/", views.units, name="units"),
    # path('parts/',views.parts,name='parts'),
    path("reactors/", views.reactors, name="reactors"),
    path("index/", views.index, name="index"),
    path("i18n/", include("django.conf.urls.i18n")),
    path("address/", views.address, name="address"),
    path("", include("tube.urls")),
    path("insert/", views.insert, name="insert"),
    # url('^inbox/notifications/', include(notifications.urls, namespace='notifications')),
    # path('inbox/',notification, name='unread-notifications'),
    # url(r'^chaining/', include('smart_selects.urls')),
    # path("select2/", include("django_select2.urls")),
#######################################################################
#                       Project API ENDPOINTS
#######################################################################
    path("api/user/login/", LoginView.as_view(), name="loginview"),
    path("api/get/clientlist/", ClientListView.as_view(), name="clientview"),
    path("api/get/unitlist/", UnitListView.as_view(), name="unitview"),
    # NEW API
    path("api/get/scopeofwork/", ScopeOfWorkView.as_view(), name="scopeofwork"),
    path("api/get/ttd/", TtdView.as_view(), name="ttdview"),
    path("api/get/bdd/", BddView.as_view(), name="BddView"),
    path("api/get/calibrationstand/", CalibrationStandView.as_view(), name="BddView"),
    path("api/get/part/", PartView.as_view(), name="PartView"),
    path("api/get/supplyorifice/", SupplyOrificeView.as_view(), name="SupplyOrificeView"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/get/reactor/", ReactorView.as_view(), name="ReactorView"),
    path("api/get/pressuresensor/",PressureSensorView.as_view(),name="PressureSensorView"),
    path("api/get/calibrationorifice/",CalibrationOrificeView.as_view(),name="CalibrationOrificeView"),
    path("api/get/swabmaster/", SwabMasterView.as_view(), name="SwabMasterView"),
    path("api/get/devicehose/", DeviceHoseView.as_view(), name="DeviceHoseView"),
    path("api/get/airhose/", AirHoseView.as_view(), name="AirHose"),
    # path('show/showrecord/<int:id>', views.showrecord, name='showrecord'),
#######################################################################
#                     Create API ENDPOINTS
#######################################################################
    path("api/listproject/", ProjectAllListView.as_view(), name="listviewproject"),
    path("api/createproject/", ProjectAllCreateView.as_view(), name="createviewproject"),
    path("api/alllist/project/<int:pk>/",AallList_Id_Project.as_view(),name="alllistproject"),
    path("api/get/project/<int:pk>/", getlList_Id_Project.as_view(), name="getproject"),
    path("api/alllist/patchproject/<int:pk>/",AallList_Id_Patch_Project.as_view(),name="alllistproject",),
#######################################################################
#                     Part API ENDPOINTS -- option api endpoint
#######################################################################
    path("api/get/option/supplyorificepart/",SupplyOrificeViewPart.as_view(),name="supplyorificepart"),
    path("api/get/option/pressuresensorpart/",PressureSensorViewPart.as_view(),name="pressuresensorpart",),
    path("api/get/option/ttdtubesealrackpart/",TTDTubeSealRackViewPart.as_view(),name="ttdtubesealrackpart",),
    path("api/get/option/bddtubesealrackpart/",BDDTubeSealRackViewPart.as_view(),name="bddtubesealrackpart",),
    path("api/get/option/swabmastertsrpart/",SwabMasterTSRViewPart.as_view(),name="swabmastertsrpart"),
    path("api/get/option/devicehoserpart/",DeviceHoseRViewPart.as_view(),name="devicehoserpart"),
    path("api/get/option/airhosepart/", AirHoseViewPart.as_view(), name="airhosepart"),
    path("api/get/option/warehouse/", WarehouseOptionListView.as_view(), name="warehouseoptionlistview"),
    path("api/get/option/calibrationorificepart/", CalibrationOrificeViewPart.as_view(), name="calibrationorificeviewpart"),
#######################################################################
#                     Equipment-API ENDPOINTS
#######################################################################

    path("api/eq/listttd/", TTDListView.as_view(), name="ttdlistview"),
    path("api/eq/createttd/", TTDCreateView.as_view(), name="ttdcreateview"),
    path("api/eq/ttdretupddel/<int:pk>/",TTDRetUpdDelView.as_view(),name="ttdretupddelview",),

    path("api/eq/bddlist/", BDDListView.as_view(), name="bddlistview"),
    path("api/eq/bddcreate/", BDDCreateView.as_view(), name="bddcreateview"),
    path("api/eq/bddretupddel/<int:pk>/",BDDRetUpdDelView.as_view(),name="bddretupddelview",),

    path("api/eq/calibrationlist/", CalibrationStandListView.as_view(), name="calibrationlist"), 
    path("api/eq/calibrationcreate/", CalibrationStandCreateView.as_view(), name="calibrationcreate"),
    path("api/eq/calibrationretupddel/<int:pk>/", CalibrationRetUpdDelView.as_view(), name="calibrationretupddel"),

    path("api/eq/swabmasterlist/", SwabMasterListView.as_view(), name = "swabmasterlist"),
    path("api/eq/swabmastercreate/", SwabMasterCreateView.as_view(), name = "swabmastercreate"),
    path("api/eq/swabmasterretupddel/<int:pk>/", SwabMasterRetUpdDelView.as_view(), name = "swabmasterretupddel"),

    

#######################################################################
#                     Client-API ENDPOINTS
#######################################################################

    path("api/cl/clientlist/", ClientListView.as_view(), name = "clientlist"),
    path("api/cl/clientcreate/", ClientCreateView.as_view(), name = "clientcreate"),
    path("api/cl/clientretupddel/<int:pk>/", ClientRetUpddel.as_view(), name="clientretupddel"),

    path("api/cl/addresslist/", AddressListView.as_view(), name = "addresslist"),
    path("api/cl/addresscreate/", AddressCreateView.as_view(), name = "addresscreate"),
    path("api/cl/addressretupddel/<int:pk>/", AddressRetUpdDelView.as_view(), name = "addressretupddel"), 

    path("api/cl/plantlist/", PlantListView.as_view(), name = "plantlistview"),
    path("api/cl/plantcreate/", PlantCreateView.as_view(), name="plantcreate"),
    path("api/cl/plantretupddel/<int:pk>/", PlantRetUpdDelView.as_view(), name="plantretupddel"),

    path("api/cl/reactorlist/", ReactorListView.as_view(), name="reactorlist"),
    path("api/cl/reactorcreate/", ReactorCreateView.as_view(), name = "reactorcreate"),
    path("api/cl/reactorretupddel/<int:pk>/", ReactorRetUpdDelView.as_view(), name="reactorretupddel"),

    path("api/cl/unitlist/", UnitListView.as_view(), name="unitlist"),
    path("api/cl/unitcreate/", UnitCreateView.as_view(), name="unitcreate"),
    path("api/cl/unitretupddel/", UnitRetUpdDelView.as_view(), name="unitretupddel"),
    
#######################################################################
#                     Warehouse-API ENDPOINTS
#######################################################################

    path("api/get/warehouse/", WarehouseListView.as_view(), name="getwarehouse"),
    path("api/get/warehouse/wp", WarehouseListViewWP.as_view(), name="getwarehousewp"),
    path("api/create/warehouse/", WarehouseCreateView.as_view(), name="createwarehouse"),
    path("api/retupddel/warehouse/<int:pk>/", WarehouseRetUpdDelView.as_view(), name="retupddelwarehouse"),
    path("api/lw/<int:pk>/", WarehouseNewListView.as_view()),

#######################################################################
#                     Part-Crud-API ENDPOINTS
#######################################################################

    path("api/part/airhosecreate/", AirHoseCreateView.as_view(), name="airhosecreate"),
    path("api/part/airhoseretupddel/<int:pk>/", AirHoseRetUpdDelView.as_view(), name="airhoseretupddel"),

    path("api/part/devicehoselist/",DeviceHoseRListView.as_view(),name="devicehoselist"),
    path("api/part/devicehosecreate/",DeviceHoseRCreateView.as_view(),name="devicehosecreate"),
    path("api/part/devicehoseretupddel/<int:pk>/",DeviceHoseRetUpdDelView.as_view(),name="devicehoseretupddel"),

    path("api/part/swabmastertsrlist/",SwabMasterTSRListView.as_view(),name="swabmastertsrlist"),
    path("api/part/swabmastertsrcreate/",SwabMasterTSRCreateView.as_view(),name="swabmastertsrcreate"),
    path("api/part/swabmastertsrretupddrl/<int:pk>/",SwabMasterTSRRetUpdDelViewl.as_view(),name="swabmastertsrretupddrl"),

    path("api/part/calibrationorificelist/",CalibrationOrificeListView.as_view(),name="calibrationorificelist"),
    path("api/part/calibrationorificecreate/",CalibrationOrificeCreateView.as_view(),name="calibrationorificecreate"),
    path("api/part/calibrationorificeretupddrl/<int:pk>/",CalibrationOrificeRetUpdDelView.as_view(),name="calibrationorificeretupddrl"),

    path("api/part/bddtubesealracklist/",BddTubesealrackList.as_view(),name="bddtubesealracklist"),
    path("api/part/bddtubesealrackcreate/",BddTubesealrackCreate.as_view(),name="bddtubesealrackcreate"),
    path("api/part/bddtubesealrackretupddrl/<int:pk>/",BddTubesealrackRetUpdDelView.as_view(),name="bddtubesealrackretupddrl"),

    path("api/part/tddtubesealracklist/",TddTubesealrackList.as_view(),name="tddtubesealracklist"),
    path("api/part/tddtubesealrackcreate/",TddTubesealrackCreate.as_view(),name="tddtubesealrackcreate"),
    path("api/part/tddtubesealrackretupddrl/<int:pk>/",TddTubesealrackRetUpdDelView.as_view(),name="tddtubesealrackretupddrl"),

    path("api/part/pressuresensorlist/",PressureSensorListView.as_view(),name="pressuresensorlist"),
    path("api/part/pressuresensorcreate/",PressureSensorCreateView.as_view(),name="pressuresensorcreate"),
    path("api/part/pressuresensorretupddrl/<int:pk>/",PressureSensorRetUpdDelView.as_view(),name="pressuresensorretupddrl"),

    path("api/part/supplyorificelist/",SupplyOrificeListView.as_view(),name="supplyorificelist"),
    path("api/part/supplyorificecreate/",SupplyOrificeCreateView.as_view(),name="supplyorificecreate"),
    path("api/part/supplyorificeretupddrl/<int:pk>/",SupplyOrificeRetUpdDelView.as_view(),name="supplyorificeretupddrl"),

    path("api/part/allgeneralpartlist/",AllGeneralPartListView.as_view(),name="allgeneralpartlist"),
    path("api/part/allgeneralpartcreate/",AllGeneralPartCreateView.as_view(),name="allgeneralpartcreate"),
    path("api/part/allgeneralpartretupddel/<int:pk>/",AllGeneralPartRetUpdDelView.as_view(),name="allgeneralpartretupddel"),

    path('api/wa/',WarehouseAvailabilityView.as_view()),
    # path('api/equip/', WarehouseEquipmentView.as_view()),
    path("api/wef/",warehouse_equipment_view),
    path("api/wp/", warehouse_part_view),
    path("api/task/",TaskView.as_view()),
    
    ##########################################################################
    
                                # '''DASHBOARD ENDPOINTS'''
    
    ##########################################################################
    
    path('api/dashboard/',DashboardView.as_view()),
    

    
]
urlpatterns += i18n_patterns(path("admin/", admin.site.urls))
# if settings.DEBUG:


