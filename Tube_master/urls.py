# import notifications.urls
from django.contrib import admin
from django.urls import path
from tube import views
from django.conf import settings  
from django.urls import path, include, reverse
from django.conf.urls.static import static  
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from tube.views import index,HttpResponseRedirect
from django.contrib.auth import views as auth_views
from django.urls import re_path as url
from django.conf.urls.i18n import i18n_patterns
from client.views import ReactorAutocomplete, notification, UnitAutocomplete,PlantAutocomplete
from tm_api.views import LoginView

from project.views import projectview
from rest_framework_simplejwt.views import TokenRefreshView
from client.views import front
from tm_api.views import *

urlpatterns = [
    path("",front, name="front"),
    path('admin/', admin.site.urls),
    path('comment/', include('comment.urls')),
    path('projectdetail/<int:pk>/', projectview, name = 'project-detail'),
    path('reactor-autocomplete/', ReactorAutocomplete.as_view(), name='reactor-autocomplete'),
    path('unit-autocomplete/', UnitAutocomplete.as_view(), name='unit-autocomplete'),
    path('plant-autocomplete/', PlantAutocomplete.as_view(), name='plant-autocomplete'),
    
    # path('unit-autocomplete/', UnitAutocomplete.as_view(), name='unit-autocomplete'),
    # path('',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('register/',views.register,name='register'),
    path("accounts/", include("django.contrib.auth.urls")),  # new
    path(
        'change-password/',
        auth_views.PasswordChangeView.as_view(template_name='change-password.html'),
    ),
    # path("password_reset", views.password_reset_request, name="password_reset") 
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),     
    # path('change-password/', auth_views.PasswordChangeView.as_view()),
  
    path('tube/', include('tube.urls')),
    path('users/',views.users,name='users'),
   
    path('user_profile/',views.user_profile,name='user_profile'),
    path('search_clients/',views.search_clients,name='search_clients'),
    path('search_plants/',views.search_plants,name='search_plants'),
    path('search_units/',views.search_units,name='search_units'),
    path('search_reactors/',views.search_reactors,name='search_reactors'),
    path('search_warehouse/',views.search_warehouse,name='search_warehouse'),
    path('search_ttd/',views.search_ttd,name='search_ttd'),
    path('search_bdd/',views.search_bdd,name='search_bdd'),
    path('search_calstand/',views.search_calstand,name='search_calstand'),
    
   
    path('clients/',views.clients,name='clients'),
    path('projects/',views.projects,name='projects'),
    path('client_profile/',views.client_profile,name='client_profile'),
    path('project_detail/',views.project_detail,name='project_detail'),
    path('update/<int:id>', views.update, name='update'),
    path('update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('show/<int:client_id>', views.show, name='show'),
    
    path('warehouse/',views.warehouse,name='warehouse'),
    path('warehouse_detail/',views.warehouse_detail,name='warehouse_detail'),
    path('updatewarehouse/<int:id>', views.updatewarehouse, name='updatewarehouse'),
    path('updatewarehouse/updatewarehouserecord/<int:id>', views.updatewarehouserecord, name='updatewarehouserecord'),
    
    path('updatettd/<int:id>', views.updatettd, name='updatettd'),
    path('updatettd/updatettdrecord/<int:id>', views.updatettdrecord, name='updatettdrecord'),
    path('updateproject/<int:id>', views.updateproject, name='updateproject'),
    path('updateproject/updateprojectrecord/<int:id>', views.updateprojectrecord, name='updateprojectrecord'),
    path('updatebdd/<int:id>', views.updatebdd, name='updatebdd'),
    path('updatebdd/updatebddrecord/<int:id>', views.updatebddrecord, name='updatebddrecord'),
    path('updatecalstand/<int:id>', views.updatecalstand, name='updatecalstand'),
    path('updatecalstand/updatecalstandrecord/<int:id>', views.updatecalstandrecord, name='updatecalstandrecord'),
    
    path('deletewarehouse/<int:id>', views.deletewarehouse, name='deletewarehouse'),
    path('showwarehouse/<int:warehouse_id>', views.showwarehouse, name='showwarehouse'),
    path('showproject/<int:project_id>', views.showproject, name='showproject'),
    
    path('deleteplant/<int:id>', views.deleteplant, name='deleteplant'),
  
    path('deleteunit/<int:id>', views.deleteunit, name='deleteunit'),

    path('deletereactor/<int:id>', views.deletereactor, name='deletereactor'),
    
    path('deletettd/<int:id>', views.deletettd, name='deletettd'),
    path('deleteproject/<int:id>', views.deleteproject, name='deleteproject'),

    path('showplant/<int:id>', views.showplant, name='showplant'),
   
    path('updateplant/<int:id>', views.updateplant, name='updateplant'),
    path('updateplant/updateplantrecord/<int:id>', views.updateplantrecord, name='updateplantrecord'),
    
    path('updateunit/<int:id>', views.updateunit, name='updateunit'),
    path('updateunit/updateunitrecord/<int:id>', views.updateunitrecord, name='updateunitrecord'),
    path('updatereactor/<int:id>', views.updatereactor, name='updatereactor'),
    path('updatereactor/updatereactorrecord/<int:id>', views.updatereactorrecord, name='updatereactorrecord'),
    path('contacts/',views.contacts,name='contacts'),
    path('equipments/',views.equipments,name='equipments'),
    
   
    
    path('plants/',views.plants,name='plants'),
    path('units/',views.units,name='units'),
    # path('parts/',views.parts,name='parts'),
    path('reactors/',views.reactors,name='reactors'),
    path('index/',views.index,name='index'),
   
    path("i18n/", include("django.conf.urls.i18n")),
    path('address/',views.address,name='address'),
    path('',include('tube.urls')),
    path('insert/', views.insert, name='insert'),
    # url('^inbox/notifications/', include(notifications.urls, namespace='notifications')),
    # path('inbox/',notification, name='unread-notifications'),
    # url(r'^chaining/', include('smart_selects.urls')),
    # path("select2/", include("django_select2.urls")),
    
    
    #######################################################################
    #                       API ENDPOINTS
    #######################################################################
    
    path("api/user/login/", LoginView.as_view(), name='loginview'),

    path("api/get/clientlist/", ClientListView.as_view(), name='clientview'),

    path("api/get/unitlist/", UnitListView.as_view(), name='unitview'),
    
    # NEW API
    path("api/get/scopeofwork/", ScopeOfWorkView.as_view(), name='scopeofwork'),

    path("api/get/ttd/", TtdView.as_view(), name='ttdview'),
    
    path("api/get/bdd/", BddView.as_view(), name='BddView'),
    
    path("api/get/calibrationstand/", CalibrationStandView.as_view(), name='BddView'),
    
    path("api/get/part/", PartView.as_view(), name='PartView'),
    
    path("api/get/supplyorifice/", SupplyOrificeView.as_view(), name='SupplyOrificeView'),
    
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path("api/get/reactor/", ReactorView.as_view(), name='ReactorView'),
    
    path("api/get/pressuresensor/", PressureSensorView.as_view(), name='PressureSensorView'),
    
    path("api/get/calibrationorifice/", CalibrationOrificeView.as_view(), name='CalibrationOrificeView'),
    
    path("api/get/swabmaster/", SwabMasterView.as_view(), name='SwabMasterView'),
    
    path("api/get/devicehose/", DeviceHoseView.as_view(), name='DeviceHoseView'),
    
    path("api/get/airhose/", AirHoseView.as_view(), name='AirHose'),
  
    # path('show/showrecord/<int:id>', views.showrecord, name='showrecord'),
    
    
    
#######################################################################
#                     Create API ENDPOINTS
#######################################################################
    
    path("api/listproject/", ProjectAllListView.as_view(), name='listviewproject'),
    
    path("api/createproject/", ProjectAllCreateView.as_view(), name='createviewproject'),
    
    path("api/alllist/project/<int:pk>/", AallList_Id_Project.as_view(), name='alllistproject'),
    
    path("api/get/project/<int:pk>/", getlList_Id_Project.as_view(), name='getproject'),
    
    path("api/alllist/patchproject/<int:pk>/", AallList_Id_Patch_Project.as_view(), name='alllistproject'),
 
] 
urlpatterns += i18n_patterns(path("admin/", admin.site.urls))
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


