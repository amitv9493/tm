from django.shortcuts import render,redirect

from django.http import HttpResponseRedirect

from django.core.files.storage import FileSystemStorage

from django.http import HttpResponse

from tube.models import Warehouse

from project.models import Project

from equipment.models import TTD,BDD,CALIBRATION_STAND

from part.models import Part,Supply_orifice,Pressure_sensor,TTD_tube_seal_rack,BDD_tube_seal_rack,Calibration_orifice

from client.models import Client,Plant,Reactor,Address,Unit

from django.contrib.auth import authenticate, login

from django.template.loader import get_template 

from django.http import HttpResponse, HttpResponseRedirect

from django.template import loader

from django.urls import reverse

from django.shortcuts import get_object_or_404
from django.db.models.query import QuerySet
from django.db.models import Q
from django.contrib import messages #import messages
from django.contrib.auth import login as authlogin






# Create your views here.

def index(request):
    client=Client.objects.all()
    reactor=Reactor.objects.all()
    warehouse=Warehouse.objects.all()
    ttd=TTD.objects.all()
    bdd=BDD.objects.all()
    cal=CALIBRATION_STAND.objects.all()
    part=Part.objects.all()
    project=Project.objects.all()
    info=zip(ttd,bdd,cal,part)
    count= Client.objects.count()
    count2=Warehouse.objects.count()
    count3=Project.objects.count()
    return render(request,'index.html',{'client':client,'reactor':reactor,'warehouse':warehouse,'info':info,'ttd':ttd,'bdd':bdd,'cal':cal,'part':part,'project':project,'count':count,'count2':count2,'count3':count3})
    
def insert(request):
    member = Client(official_name=request.POST['official_name'])
    member.save()
    return redirect('/')
    

    
def search_clients(request):
    if request.method == "POST":
        searched =request.POST['searched']
        clients=Client.objects.filter(official_name__contains=searched)
        return render(request,'search_clients.html',{'searched':searched,'clients':clients})
    else:
        return render(request,'search_clients.html',{'searched':searched,'clients':clients})
        
def search_warehouse(request):
    if request.method == "POST":
        searched =request.POST['searched']
        wares=Warehouse.objects.filter(warehouse_name__contains=searched)
        return render(request,'search_warehouse.html',{'searched':searched,'wares':wares})
    else:
        return render(request,'search_warehouse.html',{'searched':searched,'wares':wares})
        
def search_plants(request):
      
    if request.method == "POST":
        searched =request.POST['searched']
        plants=Plant.objects.filter(plant_location__contains=searched)
        return render(request,'search_plants.html',{'searched':searched,'plants':plants})
      
    else:
        return render(request,'search_plants.html',{'searched':searched,'plants':plants})
        
def search_units(request):
    if request.method == "POST":
        searched =request.POST['searched']
        units=Unit.objects.filter(name_of_unit__contains=searched)
        return render(request,'search_units.html',{'searched':searched,'units':units})
    else:
        return render(request,'search_units.html',{'searched':searched,'units':units})

def search_reactors(request):
    if request.method == "POST":
        searched =request.POST['searched']
        reactors=Reactor.objects.filter(reactor_name__contains=searched)
        return render(request,'search_reactors.html',{'searched':searched,'reactors':reactors})
    else:
        return render(request,'search_reactors.html',{'searched':searched,'reactors':reactors})

def search_ttd(request):
    if request.method == "POST":
        searched =request.POST['searched']
        ttd=TTD.objects.filter(abbreviation__contains=searched)
        return render(request,'search_ttd.html',{'searched':searched,'ttd':ttd})
    else:
        return render(request,'search_ttd.html',{'searched':searched,'ttd':ttd})
       
        
def search_bdd(request):
    if request.method == "POST":
        searched =request.POST['searched']
        bdd=BDD.objects.filter(abbreviation__contains=searched)
        return render(request,'search_bdd.html',{'searched':searched,'bdd':bdd})
    else:
        return render(request,'search_bdd.html',{'searched':searched,'bdd':bdd})
        
def search_calstand(request):
    if request.method == "POST":
        searched =request.POST['searched']
        calstand=CALIBRATION_STAND.objects.filter(abbreviation__contains=searched)
        return render(request,'search_calstand.html',{'searched':searched,'calstand':calstand})
    else:
        return render(request,'search_calstand.html',{'searched':searched,'calstand':calstand})


        

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)     
        
        if user is not None:
            authlogin(request, user)
            return redirect('/tm/index')
        else:
            logout(request)
            return redirect('/tm/logout')
			
    context = {}
    return render(request, 'registration/login.html', context)

 
      
def logout(request):    
    
  
    return render(request,"registration/logout.html")


   

def register(request):

    return render(request,'registration/register.html')

   

def warehouse(request):

    if request.POST.get('warehouse_name') and request.POST.get('warehouse_location') and request.POST.get('warehouse_contact')and request.POST.get('warehouse_email')and request.POST.get('warehouse_manager'):

         app= Warehouse()

         app.warehouse_name=request.POST.get('warehouse_name')
         app.warehouse_location=request.POST.get('warehouse_location')
         app.warehouse_contact=request.POST.get('warehouse_contact')
         app.warehouse_email=request.POST.get('warehouse_email')
         app.warehouse_manager=request.POST.get('warehouse_manager')
         app.save()
         warehouse = Warehouse.objects.all()
         return  render(request,'warehouse.html',{'warehouse':warehouse})

   

    else:
         warehouse = Warehouse.objects.all()
         return  render(request,'warehouse.html',{'warehouse':warehouse})
   

  

def users(request):

    upload = UserForm()

    if request.method == 'POST':

        upload =UserForm(request.POST, request.FILES)

        if upload.is_valid():

            upload.save()

            return redirect('index')

        else:

            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")

    else:

        

        return render(request, 'users.html', {'upload_form':upload})



   

def update_user(request,user_id):

    upload = UserForm()

    if request.method == 'POST':

        upload =UserForm(request.POST, request.FILES)

        if upload.is_valid():

            upload.save()

            return redirect('index')

        else:

            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")

    else:

        return render(request, 'users.html', {'upload_form':upload})

    

def user_profile(request):  

    return render(request,'updateuser.html')  

    

def client_profile(request):  

  

    return render(request,'client-profile.html')
    


def project_detail(request):  

  

    return render(request,'project-detail.html')

def warehouse_detail(request):  

  

    return render(request,'warehouse-detail.html')


    



       

def plants(request):

    if request.POST.get('plant_location') and request.POST.get('plant_contact') and request.POST.get('name_of_unit') and request.POST.get('chemical_being_manufactured_by_this_unit') :

          

             app= Plant()

          

             app.plant_location=request.POST.get('plant_location')

             app.plant_contact=request.POST.get('plant_contact')
             
            #  unitname=request.POST.get('name_of_unit')
            #  chemical_name=request.POST.get('chemical_being_manufactured_by_this_unit')

             
             
          
           

            #  app.save()
             
            #  unit1=Unit.objects.create()

             app.name_of_unit.add(name_of_unit="unit3",chemical_being_manufactured_by_this_unit="benzne")
             app.save()


             plant = Plant.objects.all()

             return render(request,'client-profile.html',{'plant':plant})

   

    else:

            plant = Plant.objects.all()

            return render(request,'client-profile.html',{'plant':plant})



# def parts(request):

    

#             part = Part.objects.all()

          

#             return render(request,'parts.html',{'info':info})





def units(request):

    

         reactor_list=Unit.objects.all().order_by('id')

        #  client=Client.objects.all()

         unit= Unit.objects.all()

         

         info=zip(unit,reactor_list)

         return render(request,'units.html',{'info':info})

                    





           



def reactors(request):

    if request.POST.get('reactor_name') :

             app=Reactor()

             app.reactor_name=request.POST.get('reactor_name')

           

             app.save()

           

             reactor = Reactor.objects.all()

             return redirect('/tm/clients')



    else:

        reactor = Reactor.objects.all()

        return render(request,'reactors.html',{'reactor':reactor})

    

  

def equipments(request):

    if request.POST.get('equipment_name') and request.POST.get('abbreviation') and request.POST.get('alternate_name')and request.POST.get('serial_number')and request.POST.get('asset_number')and request.POST.get('pm_status') and request.POST.get('location_for_warehouse') and request.POST.get('location_for_storage') and request.POST.get('packaging') and request.POST.get('is_this_part_of_set') and request.POST.get('if_yes_how_many_in_a_set') and request.POST.get('is_it_an_assembly') and request.POST.get('allowed_to_add_sub_parts'):

          

             app= Equipment()

           



             app.equipment_name=request.POST.get('equipment_name')

             app.abbreviation=request.POST.get('abbreviation')

             app.alternate_name=request.POST.get('alternate_name')

             app.serial_number=request.POST.get('serial_number')

             app.asset_number=request.POST.get('asset_number')

             app.pm_status=request.POST.get('pm_status')

             app.location_for_warehouse=request.POST.get('location_for_warehouse')

             app.location_for_storage=request.POST.get('location_for_storage')

             app.packaging=request.POST.get('packaging')

             app.is_this_part_of_set=request.POST.get('is_this_part_of_set')

             app.if_yes_how_many_in_a_set=request.POST.get('if_yes_how_many_in_a_set')

             app.is_it_an_assembly=request.POST.get('is_it_an_assembly')

             app.allowed_to_add_sub_parts=request.POST.get('allowed_to_add_sub_parts')

             app.save()

           

            #  equipment = Equipment.objects.all()

             return render(request,'equipments.html')



   

    else:

            # equipment = Equipment.objects.all()

            # part_list=Equipment.objects.all().order_by('id')

            # warehouse_list = Equipment.objects.all().order_by('id')

        

         

        

            # info=zip(equipment,warehouse_list,part_list)

         

            return render(request,'equipments.html')

   

            



def clients(request,pk=id):



    if request.method=='POST' and 'add_client' in request.POST:

      if request.POST.get('official_name') and request.POST.get('comman_name') and request.POST.get('alternate_name')and request.POST.get('parent_company')and request.POST.get('former_name')and request.POST.get('contact_person')and request.POST.get('contact_person_phone')and request.POST.get('contact_person_email'):

             app=Client()

           

             app.official_name=request.POST.get('official_name')

             app.comman_name=request.POST.get('comman_name')

             app.alternate_name=request.POST.get('alternate_name')

            #  app.key_contact=request.POST.get('key_contact')

             app.parent_company=request.POST.get('parent_company')

           
             app.former_name=request.POST.get('former_name')
             app.contact_person=request.POST.get('contact_person')
             app.contact_person_phone=request.POST.get('contact_person_phone')
             app.contact_person_email=request.POST.get('contact_person_email')
            

             app.save()
             p1 = Address(addressline1=request.POST.get('oaddressline1'),addressline2=request.POST.get('oaddressline2'),addressline3=request.POST.get('oaddressline3'),City=request.POST.get('oCity'),Country=request.POST.get('oCountry'),State=request.POST.get('oState'),Zipcode=request.POST.get('oZipcode'))
             p1.save()
             app.official_address.add(p1)
             app.save()
             
             p2 = Address(addressline1=request.POST.get('saddressline1'),addressline2=request.POST.get('saddressline2'),addressline3=request.POST.get('saddressline3'),City=request.POST.get('sCity'),Country=request.POST.get('sCountry'),State=request.POST.get('sState'),Zipcode=request.POST.get('sZipcode'))
             p2.save()
             app.shipping_address.add(p2)
             app.save()
             
             p3 = Address(addressline1=request.POST.get('paddressline1'),addressline2=request.POST.get('paddressline2'),addressline3=request.POST.get('paddressline3'),City=request.POST.get('pCity'),Country=request.POST.get('pCountry'),State=request.POST.get('pState'),Zipcode=request.POST.get('pZipcode'))
             p3.save()
             app.plantentrance_address.add(p3)
             app.save()

             return render(request,'clients.html')
   
    else:
        client=  Client.objects.all()
        return render(request,'clients.html',{'client':client})
    

def projects(request):
    if request.method=='POST' and 'add_project' in request.POST:

        if request.POST.get('client_name') and request.POST.get('chemical_name') and request.POST.get('unit_name') and request.POST.get('reactor_name') and request.POST.get('project_number') and request.POST.get('ttd_name') and request.POST.get('bdd_name')  and request.POST.get('cal_stand_name') and request.POST.get('equipment_prep') and request.POST.get('equipment_ready') and request.POST.get('equipment_ship_client') and  request.POST.get('equipment_delivery_client')and request.POST.get('project_start')and request.POST.get('project_end')and request.POST.get('equipment_return_tubemaster')and request.POST.get('equipment_delivery_tubemaster')and request.POST.get('scope_of_work')and request.POST.get('contract')and request.POST.get('if_subcontract_client_name'):

             app=Project()
             app.client_id=request.POST.get('client_name')
             app.chemical=request.POST.get('chemical_name')
             app.unit_id=request.POST.get('unit_name')
             app.reactor_id=request.POST.get('reactor_name')
             app.ttd_id=request.POST.get('ttd_name')
             app.bdd_id=request.POST.get('bdd_name')
             app.calibration_stand_id=request.POST.get('cal_stand_name')
             app.project_number=request.POST.get('project_number')
             app.equipment_prep=request.POST.get('equipment_prep')
             app.equipment_ready=request.POST.get('equipment_ready')
             app.equipment_ship_client=request.POST.get('equipment_ship_client')
             app.equipment_delivery_client=request.POST.get('equipment_delivery_client')
             app.project_start=request.POST.get('project_start')
             app.project_end=request.POST.get('project_end')
             app.equipment_return_tubemaster=request.POST.get('equipment_return_tubemaster')
             app.equipment_delivery_tubemaster=request.POST.get('equipment_delivery_tubemaster')
             app.scope_of_work=request.POST.get('scope_of_work')
             app.contract=request.POST.get('contract')
             app.if_sub_client_name=request.POST.get('if_subcontract_client_name')
            
             app.save()
             return render(request,'projects.html')
    else:
        client=  Client.objects.all()
        plant=  Plant.objects.all()
        unit=  Unit.objects.all()
        reactor=  Reactor.objects.all()
        project=  Project.objects.all()
        ttd1=TTD.objects.all()
        bdd1=BDD.objects.all()
        cal_stand=CALIBRATION_STAND.objects.all()
        return render(request,'projects.html',{'project':project,'client':client,'plant':plant,'unit':unit,'reactor':reactor,'ttd1':ttd1,'bdd1':bdd1,'cal_stand':cal_stand})
        
    #   if request.POST.get('client_name') and request.POST.get('chemical_name') and request.POST.get('unit_name')and request.POST.get('reactor_name')and request.POST.get('project_number'):
    
         

def update(request, id):

    mymember = Client.objects.get(id=id)
    return render(request,'update.html',{'mymember':mymember})

def updateplant(request, id):

    myplant= Plant.objects.get(id=id)
    return render(request,'updateplant.html',{'myplant':myplant})   

def updateunit(request, id):

    myunit= Unit.objects.get(id=id)
    return render(request,'updateunit.html',{'myunit':myunit})   

def updatereactor(request, id):

    myreactor= Reactor.objects.get(id=id)
    return render(request,'updatereactor.html',{'myreactor':myreactor}) 
    
def updatewarehouse(request, id):

    mywarehouse = Warehouse.objects.get(id=id)
    return render(request,'updatewarehouse.html',{'mywarehouse':mywarehouse})
    
def updateproject(request, id):

    myproject = Project.objects.get(id=id)
    return render(request,'updateproject.html',{'myproject':myproject})
    
def updatettd(request, id):

    myttd= TTD.objects.get(id=id)
    return render(request,'updatettd.html',{'myttd':myttd})

def updatebdd(request, id):

    mybdd= BDD.objects.get(id=id)
    return render(request,'updatebdd.html',{'mybdd':mybdd})
    
def updatecalstand(request, id):

    mycalstand= CALIBRATION_STAND.objects.get(id=id)
    return render(request,'updatecalstand.html',{'mycalstand':mycalstand})


def delete(request, id):

     client = Client.objects.get(id=id)

     client.delete()
     return render(request,'clients.html')   
   

def deleteplant(request, id):

  plant = Plant.objects.get(id=id)
  

  plant.delete()
  return render(request,'clients.html',{'plant':plant}) 
 
def deleteproject(request, id):

  project = Project.objects.get(id=id)
  

  project.delete()
  return render(request,'projects.html',{'project':project}) 


      
def deleteunit(request, id):

  unit = Unit.objects.get(id=id)

  unit.delete()

  return render(request,'clients.html',{'unit':unit})   

def deletereactor(request, id):

  reactor = Reactor.objects.get(id=id)

  reactor.delete()

  return render(request,'clients.html',{'reactor':reactor})  

def deletewarehouse(request, id):

  warehouse=Warehouse.objects.get(id=id)

  warehouse.delete()

  return render(request,'warehouse-detail.html',{'warehouse':warehouse})  
 
def deletettd(request, id):

  ttd=TTD.objects.get(id=id)

  ttd.delete()

  return render(request,'warehouse-detail.html',{'ttd':ttd})   



def show(request,client_id):
    if request.method=='POST' and 'add_plant' in request.POST:
      if  request.POST.get('plant_location') and request.POST.get('plant_contact'):

            app3=Plant()
            app3.client_id=client_id
            
            app3.plant_location=request.POST.get('plant_location')
            app3.plant_contact=request.POST.get('plant_contact')
            app3.save()
       
            next2 = request.POST.get('next2', '/')
            return HttpResponseRedirect(next2)
    
    
    if request.method=='POST' and 'add_unit' in request.POST:
       if request.POST.get('plant_id')and  request.POST.get('name_of_unit') and request.POST.get('chemical_being_manufactured_by_this_unit'):

             app5= Unit()
             app5.client_id=client_id
             app5.plant_id= request.POST.get('plant_id')
          
             app5.name_of_unit=request.POST.get('name_of_unit')

             app5.chemical_being_manufactured_by_this_unit=request.POST.get('chemical_being_manufactured_by_this_unit')
             app5.save()
            
             next = request.POST.get('next', '/')
             return HttpResponseRedirect(next)
    
    if request.method=='POST' and 'add_reactor' in request.POST:
      if  request.POST.get('plant_id')and request.POST.get('unit_id')and request.POST.get('reactor_name') and request.POST.get('tube_id') and request.POST.get('input_tubeid') and request.POST.get('is_there_ferrule_insert_in_tube') and request.POST.get('ferrule_length') and  request.POST.get('input_ferrulelength') and request.POST.get('ferrule_id')and request.POST.get('input_ferruleid')and request.POST.get('tube_material_of_raws')and request.POST.get('tube_material_of_thermo')and request.POST.get('tube_material_of_supports')and request.POST.get('tube_material_of_plugs')and request.POST.get('tube_material_of_coolent_tubes')and request.POST.get('any_projections_on_tube_sheet_describe') and request.POST.get('tube_sheet_material')and request.POST.get('dom_material') and request.POST.get('tube_spacing_or_pitch') and request.POST.get('input_tubespacing') and request.POST.get('total_tube_length') and request.POST.get('input_totaltube') and request.POST.get('top_tube_sheet_thickness')and request.POST.get('input_toptube') and request.POST.get('bottom_tube_sheet_thickness') and request.POST.get('input_bottomtube') and request.POST.get('tube_protude_out_of_top_tube_sheet') and request.POST.get('select_tube_protude_top') and request.POST.get('input_tubeprotude_top') and request.POST.get('tube_protude_out_of_bottom_tube_sheet') and request.POST.get('select_tube_protude_bottom') and request.POST.get('input_tubeprotude_bottom') and request.POST.get('top_dome_removable') and request.POST.get('top_inlet_accessible')and request.POST.get('top_inlet_impingment_plate'):

              app4= Reactor()
              app4.client_id=client_id
              app4.plant_id=request.POST.get('plant_id')
              app4.unit_id=request.POST.get('unit_id')
              app4.reactor_name=request.POST.get('reactor_name')
              app4.tube_id=request.POST.get('tube_id')
              app4.input_tubeid=request.POST.get('input_tubeid')
              app4.is_there_ferrule_insert_in_tube=request.POST.get('is_there_ferrule_insert_in_tube')
              app4.ferrule_length= request.POST.get('ferrule_length')
              app4.input_ferrulelength=request.POST.get('input_ferrulelength')
              app4.ferrule_id= request.POST.get('ferrule_id')
              app4.input_ferruleid=request.POST.get('input_ferruleid')
              app4.tube_material_of_raws=request.POST.get('tube_material_of_raws')
              app4.tube_material_of_thermo=request.POST.get('tube_material_of_thermo')
              app4.tube_material_of_supports=request.POST.get('tube_material_of_supports')
              app4.tube_material_of_plugs=request.POST.get('tube_material_of_plugs')
              app4.tube_material_of_coolent_tubes=request.POST.get('tube_material_of_coolent_tubes')
              app4.any_projections_on_tube_sheet_describe=request.POST.get('any_projections_on_tube_sheet_describe')
              app4.tube_sheet_material= request.POST.get('tube_sheet_material')
              app4.dom_material= request.POST.get('dom_material')
              app4.tube_spacing_or_pitch=request.POST.get('tube_spacing_or_pitch')
              app4.input_tubespacing=request.POST.get('input_tubespacing')
              app4.total_tube_length=request.POST.get('total_tube_length')
              app4.input_totaltube=request.POST.get('input_totaltube')
              app4.top_tube_sheet_thickness=request.POST.get('top_tube_sheet_thickness')
              app4.input_toptube=request.POST.get('input_toptube')
              app4.bottom_tube_sheet_thickness=request.POST.get('bottom_tube_sheet_thickness')
              app4.input_bottomtube=request.POST.get('input_bottomtube')
              app4.tube_protude_out_of_top_tube_sheet=request.POST.get('tube_protude_out_of_top_tube_sheet')
              app4.select_tube_protude_top=request.POST.get('select_tube_protude_top')
              app4.input_tubeprotude_top=request.POST.get('input_tubeprotude_top')
              app4.tube_protude_out_of_bottom_tube_sheet=request.POST.get('tube_protude_out_of_bottom_tube_sheet')
              app4.select_tube_protude_bottom=request.POST.get('select_tube_protude_bottom')
              app4.input_tubeprotude_bottom=request.POST.get('input_tubeprotude_bottom')
              app4.top_dome_removable=request.POST.get('top_dome_removable')
              app4.top_inlet_accessible=request.POST.get('top_inlet_accessible')
              app4.top_inlet_impingment_plate=request.POST.get('top_inlet_impingment_plate')
              app4.tube_spacing_proof_document=request.FILES['tube_spacing_proof_document'] 
              app4.reactor_tube_sheet_drawings=request.FILES['reactor_tube_sheet_drawings'] 
              app4.reactor_elevation_view_drawings=request.FILES['reactor_elevation_view_drawings'] 
              app4.other_drawings=request.FILES['other_drawings'] 
           
              app4.save()
              next3 = request.POST.get('next3', '/')
              return HttpResponseRedirect(next3)
               
             
   
      
              
    else:
   
        client=  Client.objects.get(id=client_id)
        plant1=  Plant.objects.all()
        unit=  Unit.objects.all()
        reactor=  Reactor.objects.all()
        
        info2=zip(unit,plant1)
        info3=zip(reactor,plant1,unit)
        info4=zip(unit,plant1)
        info5=zip(plant1,unit,reactor)
       
       
       
        return render(request,'client-profile.html',{'client':client,'info2':info2,'info3':info3,'info4':info4,'plant1':plant1,'unit1':unit,'reactor1':reactor,'info5':info5})


def showwarehouse(request,warehouse_id):
    if request.method=='POST' and 'add_ttd' in request.POST :
      if   request.POST.get('abbreviation')and  request.POST.get('alternate_name') and request.POST.get('serial_number')and  request.POST.get('asset_number')and request.POST.get('location_for_warehouse')and request.POST.get('location_for_storage')and request.POST.get('packaging')and request.POST.get('is_this_part_of_set')and ('if_yes_how_many_in_a_set') and request.POST.get('size') and request.POST.get('total_sets')and request.POST.get('orifice_in_each_set') and request.POST.get('storage_case') and request.POST.get('notes') and request.POST.get('range') and request.POST.get('quantity') and request.POST.get('size1') and request.POST.get('quantity_rack') and request.POST.get('tube_seal_rack') :

              app4= TTD()
              app4.abbreviation=request.POST.get('abbreviation')
              app4.alternate_name=request.POST.get('alternate_name')
              app4.serial_number=request.POST.get('serial_number')
              app4.asset_number=request.POST.get('asset_number')
              app4.warehouse_name=request.POST.get('location_for_warehouse')
              app4.location_for_storage=request.POST.get('location_for_storage')
              app4.packaging=request.POST.get('packaging')
              app4.is_this_part_of_set=request.POST.get('is_this_part_of_set')
              app4.if_yes_how_many_in_a_set=request.POST.get('if_yes_how_many_in_a_set')
              
     
              app4.save()
          
      
              p1 = Supply_orifice(size=request.POST.get('size'),total_sets=request.POST.get('total_sets'),orifice_in_each_set=request.POST.get('orifice_in_each_set'),storage_case=request.POST.get('storage_case'),notes=request.POST.get('notes'))
              p1.save()
              app4.supply_orifice_set.add(p1)
              app4.save()
             
              p2 = Pressure_sensor(range=request.POST.get('range'),quantity=request.POST.get('quantity'))
              p2.save()
              app4.pressure_sensor.add(p2)
              app4.save()
              
              p3 = TTD_tube_seal_rack(size=request.POST.get('size1'),qty_rack=request.POST.get('quantity_rack'),tube_seal_rack=request.POST.get('tube_seal_rack'))
              p3.save()
              app4.TTD_tube_seal_rack.add(p3)
              app4.save()
           
              app4.image=request.FILES['image1'] 
              
              app4.save()
              
              next3 = request.POST.get('next3', '/')
              return HttpResponseRedirect(next3)
              
    if request.method=='POST' and 'add_bdd' in request.POST:
      if   request.POST.get('bdd_abbreviation')and  request.POST.get('bdd_alternate_name') and request.POST.get('bdd_serial_number')and  request.POST.get('bdd_asset_number')and request.POST.get('bdd_location_for_warehouse')and request.POST.get('bdd_location_for_storage')and request.POST.get('bdd_packaging')and request.POST.get('bdd_is_this_part_of_set') and request.POST.get('bdd_if_yes_how_many_in_a_set') and request.POST.get('size') and request.POST.get('quantity_rack') and request.POST.get('tube_seal_rack') :
 

              app5= BDD()
              app5.abbreviation=request.POST.get('bdd_abbreviation')
              app5.alternate_name=request.POST.get('bdd_alternate_name')
              app5.serial_number=request.POST.get('bdd_serial_number')
              app5.asset_number=request.POST.get('bdd_asset_number')
              app5.warehouse_name=request.POST.get('bdd_location_for_warehouse')
              app5.location_for_storage=request.POST.get('bdd_location_for_storage')
              app5.packaging=request.POST.get('bdd_packaging')
              app5.is_this_part_of_set=request.POST.get('bdd_is_this_part_of_set')
              app5.if_yes_how_many_in_a_set=request.POST.get('bdd_if_yes_how_many_in_a_set')
           
              app5.save()
              
              p1 = BDD_tube_seal_rack(size=request.POST.get('size'),qty_rack=request.POST.get('quantity_rack'),tube_seal_rack=request.POST.get('tube_seal_rack'))
              p1.save()
              app5.BDD_tube_seal_rack.add(p1)
              app5.save()
              
            #   app5.image=request.FILES['bdd_image']
              
            #   app5.save()
         
              next4 = request.POST.get('next4', '/')
              return HttpResponseRedirect(next4)
              
    if request.method=='POST' and 'add_cal_stand' in request.POST:
      if   request.POST.get('cal_abbreviation')and  request.POST.get('cal_alternate_name') and request.POST.get('cal_serial_number')and  request.POST.get('cal_asset_number')and request.POST.get('cal_location_for_warehouse')and request.POST.get('cal_location_for_storage')and request.POST.get('cal_packaging')and request.POST.get('cal_is_this_part_of_set') and request.POST.get('cal_if_yes_how_many_in_a_set') and request.POST.get('cal_stand_size')and request.POST.get('size') and request.POST.get('total_sets') and request.POST.get('in_sets'):
 

              app6= CALIBRATION_STAND()
              app6.abbreviation=request.POST.get('cal_abbreviation')
              app6.alternate_name=request.POST.get('cal_alternate_name')
              app6.serial_number=request.POST.get('cal_serial_number')
              app6.asset_number=request.POST.get('cal_asset_number')
              app6.warehouse_name=request.POST.get('cal_location_for_warehouse')
              app6.location_for_storage=request.POST.get('cal_location_for_storage')
              app6.packaging=request.POST.get('cal_packaging')
              app6.is_this_part_of_set=request.POST.get('cal_is_this_part_of_set')
              app6.if_yes_how_many_in_a_set=request.POST.get('cal_if_yes_how_many_in_a_set')
              app6.cal_stand_size=request.POST.get('cal_stand_size')
              
              app6.save()
              
              p1 = Calibration_orifice(size=request.POST.get('size'),total_sets=request.POST.get('total_sets'),in_sets=request.POST.get('in_sets'))
              p1.save()
              app6.calibration_orifice_set.add(p1)
              app6.save()
              
              app6.image = request.FILES['image3'] 
              app6.save()
         
              next5 = request.POST.get('next5', '/')
              return HttpResponseRedirect(next5)
    else:
    
            warehouse=  Warehouse.objects.get(id=warehouse_id)
            ttd1=TTD.objects.all()
            bdd1=BDD.objects.all()
            cal_stand=CALIBRATION_STAND.objects.all()
            warehouse_all=Warehouse.objects.all()
            supply=Supply_orifice.objects.all()
            pressure=Pressure_sensor.objects.all()
            ttd_tube=TTD_tube_seal_rack.objects.all()
            bdd_tube=BDD_tube_seal_rack.objects.all()
            cal_orifice=Calibration_orifice.objects.all()
            info=zip(ttd1,supply,pressure,ttd_tube)
            info2=zip(bdd1,bdd_tube)
            info3=zip(cal_stand,cal_orifice)
           
    
            return render(request,'warehouse-detail.html',{'warehouse':warehouse,'ttd1':ttd1,'bdd1':bdd1,'cal_stand':cal_stand,'warehouse_all':warehouse_all,'supply':supply,'info':info,'info2':info2,'info3':info3})

   
def showproject(request,project_id):
    # if request.method=='POST' and 'add_project' in request.POST :
    #   if   request.POST.get('abbreviation')and  request.POST.get('alternate_name') and request.POST.get('serial_number')and  request.POST.get('asset_number')and request.POST.get('location_for_warehouse')and request.POST.get('location_for_storage')and request.POST.get('packaging')and request.POST.get('is_this_part_of_set')and ('if_yes_how_many_in_a_set') and request.POST.get('size') and request.POST.get('total_sets')and request.POST.get('orifice_in_each_set') and request.POST.get('storage_case') and request.POST.get('notes') and request.POST.get('range') and request.POST.get('quantity') and request.POST.get('size1') and request.POST.get('quantity_rack') and request.POST.get('tube_seal_rack') :

    #           app4= TTD()
    #           app4.abbreviation=request.POST.get('abbreviation')
    #           app4.alternate_name=request.POST.get('alternate_name')
    #           app4.serial_number=request.POST.get('serial_number')
    #           app4.asset_number=request.POST.get('asset_number')
    #           app4.warehouse_name=request.POST.get('location_for_warehouse')
    #           app4.location_for_storage=request.POST.get('location_for_storage')
    #           app4.packaging=request.POST.get('packaging')
    #           app4.is_this_part_of_set=request.POST.get('is_this_part_of_set')
    #           app4.if_yes_how_many_in_a_set=request.POST.get('if_yes_how_many_in_a_set')
              
     
    #           app4.save()
          
      
    #           p1 = Supply_orifice(size=request.POST.get('size'),total_sets=request.POST.get('total_sets'),orifice_in_each_set=request.POST.get('orifice_in_each_set'),storage_case=request.POST.get('storage_case'),notes=request.POST.get('notes'))
    #           p1.save()
    #           app4.supply_orifice_set.add(p1)
    #           app4.save()
             
    #           p2 = Pressure_sensor(range=request.POST.get('range'),quantity=request.POST.get('quantity'))
    #           p2.save()
    #           app4.pressure_sensor.add(p2)
    #           app4.save()
              
    #           p3 = TTD_tube_seal_rack(size=request.POST.get('size1'),qty_rack=request.POST.get('quantity_rack'),tube_seal_rack=request.POST.get('tube_seal_rack'))
    #           p3.save()
    #           app4.TTD_tube_seal_rack.add(p3)
    #           app4.save()
           
    #           app4.image=request.FILES['image1'] 
              
    #           app4.save()
              
    #           next3 = request.POST.get('next3', '/')
    #           return HttpResponseRedirect(next3)
              
    # else:
        
           
    
          
        project=  Project.objects.get(id=project_id)
        client= Client.objects.all()
        plant1=  Plant.objects.all()
        unit=  Unit.objects.all()
        reactor=  Reactor.objects.all()
        
        info2=zip(unit,plant1)
        info3=zip(reactor,plant1,unit)
        info4=zip(unit,plant1)
        info5=zip(plant1,unit,reactor)
       
       
       
        return render(request,'project-detail.html',{'client':client,'info2':info2,'info3':info3,'info4':info4,'plant1':plant1,'unit1':unit,'reactor1':reactor,'info5':info5,'project':project})

def showplant(request, id):

    myplant  = Plant.objects.get(id=id)
    return render(request,'client-profile.html',{'myplant':myplant})

    

def updateaddress(request, id):

   

    myaddress= Address.objects.get(id=id)

#   template = loader.get_template('update.html')

  

    return render(request,'update.html',{'myaddress':myaddress})

    

    

def updaterecord(request, id):

      official_name = request.GET['official_name']
      comman_name = request.GET['comman_name']
      alternate_name = request.GET['alternate_name']
      parent_company = request.GET['parent_company']
      former_name = request.GET['former_name']
      contact_person = request.GET['contact_person']
      contact_person_phone = request.GET['contact_person_phone']
      contact_person_email = request.GET['contact_person_email']
      

      member = Client.objects.get(id=id)
    
      member.official_name = official_name
      member.comman_name = comman_name
      member.alternate_name = alternate_name
      member.parent_company = parent_company
      member.former_name = former_name
      member.contact_person = contact_person
      member.contact_person_phone = contact_person_phone
      member.contact_person_email = contact_person_email
     
      member.save()

      return redirect('/tm/clients')
      
def updateprojectrecord(request, id):

    #   client = request.POST['client']
    #   chemical_name = request.GET['chemical_name']
    #   unit_name = request.GET['unit_name']
    #   reactor_name= request.GET['reactor_name']
    #   ttd_name = request.GET['ttd_name']
    #   bdd_name =request.GET['bdd_name']
    #   cal_stand_name=request.GET['cal_stand_name']
      equipment_prep=request.GET['equipment_prep']
      equipment_ready=request.GET['equipment_ready']
      equipment_ship_client=request.GET['equipment_ship_client']
      equipment_delivery_client=request.GET['equipment_delivery_client']
      project_start=request.GET['project_start']
      project_end=request.GET['project_end']
      equipment_return_tubemaster=request.GET['equipment_return_tubemaster']
      equipment_delivery_tubemaster=request.GET['equipment_delivery_tubemaster']
      scope_of_work=request.GET['scope_of_work']
      contract=request.GET['contract']
      if_sub_client_name=request.GET['if_sub_client_name']
    
    

      member = Project.objects.get(id=id)
      
    #   member.client = client
    #   member.chemical = chemical_name
    #   member.unit = unit_name
    #   member.reactor=reactor_name
    #   member.ttd=ttd_name
    #   member.bdd=bdd_name
    #   member.calibration_stand=cal_stand_name
      member.equipment_prep=equipment_prep
      member.equipment_ready=equipment_ready
      member.equipment_ship_client=equipment_ship_client
      member.equipment_delivery_master=equipment_delivery_tubemaster
      member.project_start=project_start
      member.project_end=project_end
      member.equipment_return_tubemaster=equipment_return_tubemaster
      member.equipment_delivery_tubemaster=equipment_delivery_tubemaster
      member.scope_of_work=scope_of_work
      member.contract=contract
      member.if_sub_client_name=if_sub_client_name
     
      member.save()

      return redirect('/tm/projects')


def updatewarehouserecord(request, id):

      warehouse_name = request.POST['warehouse_name']
    
      warehouse_location = request.POST['warehouse_location']
    
      warehouse_contact = request.POST['warehouse_contact']
    
      warehouse_email = request.POST['warehouse_email']
    
      warehouse_manager = request.POST['warehouse_manager']
    
    

      member = Warehouse.objects.get(id=id)
    
      member.warehouse_name = warehouse_name
    
      member.warehouse_location = warehouse_location
    
      member.warehouse_contact = warehouse_contact
    
      member.warehouse_email=warehouse_email
    
      member.warehouse_manager=warehouse_manager
    
     
      member.save()

      return redirect('/tm/warehouse')


       

def updateplantrecord(request, id):
    
    

      plant_location = request.POST['plant_location']
    
      plant_contact= request.POST['plant_contact']
    
      member =Plant.objects.get(id=id)
      
     
    
      member.plant_location= plant_location
    
      member.plant_contact = plant_contact

      member.save()
      return redirect('/tm/clients')
   

def updateunitrecord(request, id):

      name_of_unit = request.POST['name_of_unit']
    
      chemical_being_manufactured_by_this_unit= request.POST['chemical_being_manufactured_by_this_unit']
    
      member =Unit.objects.get(id=id)
    
      member.name_of_unit= name_of_unit
    
      member.chemical_being_manufactured_by_this_unit =  chemical_being_manufactured_by_this_unit

      member.save()

      return redirect('/tm/clients')

def updatereactorrecord(request, id):

      reactor_name = request.POST['reactor_name']
      tube_id = request.POST['tube_id']
      inch    = request.POST['inch']
      mm      = request.POST['mm']
      is_there_ferrule_insert_in_tube=request.POST['is_there_ferrule_insert_in_tube']
      ferrule_length=request.POST['ferrule_length']
      inch1 = request.POST['inch1']
      mm1 =request.POST['mm1']
      ferrule_id = request.POST['ferrule_id']
      inch2 =request.POST['inch2']
      mm2 = request.POST['mm2']
      tube_material_of_tubes = request.POST['tube_material_of_tubes']
      tube_material_of_raws = request.POST['tube_material_of_raws']
      tube_material_of_thermo = request.POST['tube_material_of_thermo']
      tube_material_of_supports = request.POST['tube_material_of_supports']
      tube_material_of_plugs  =request.POST['tube_material_of_plugs']
      tube_material_of_coolent_tubes=request.POST['tube_material_of_coolent_tubes']
      tube_spacing_or_pitch=request.POST['tube_spacing_or_pitch']
      inch3 =request.POST['inch3']
      mm3 =request.POST['mm3']
      total_tube_length=request.POST['total_tube_length']
      inch4 =request.POST['inch4']
      mm4 =request.POST['mm4']
      top_tube_sheet_thickness = request.POST['top_tube_sheet_thickness']
      inch5 =request.POST['inch5']
      mm5 = request.POST['mm5']
      bottom_tube_sheet_thickness = request.POST['bottom_tube_sheet_thickness']
      inch6 = request.POST['inch6']
      mm6 =request.POST['mm6']
      tube_protude_out_of_top_tube_sheet = request.POST['tube_protude_out_of_top_tube_sheet']
      inch7=request.POST['inch7']
      mm7 =request.POST['mm7']
      tube_protude_out_of_bottom_tube_sheet=request.POST['tube_protude_out_of_bottom_tube_sheet']
      inch8 =request.POST['inch8']
      mm8 =request.POST['mm8']
      top_dom_removable = request.POST['top_dom_removable']
      top_inlet_accessible = request.POST['top_inlet_accessible']
      top_inlet_impingment_plate =request.POST['top_inlet_impingment_plate']
      any_projections_on_tube_sheet_describe = request.POST['any_projections_on_tube_sheet_describe']
      tube_sheet_material = request.POST['tube_sheet_material']
      dom_material = request.POST['dom_material']
      tube_spacing_proof_document = request.FILES.get('tube_spacing_proof_document')
      reactor_tube_sheet_drawings = request.FILES.get('reactor_tube_sheet_drawings')
      reactor_elevation_view_drawings = request.FILES.get('reactor_elevation_view_drawings')
      other_drawings = request.FILES.get('other_drawings')
      
      
      member =Reactor.objects.get(id=id)
    
      member.reactor_name= reactor_name
      member.tube_id = tube_id
      member.inch = inch
      member.mm = mm
      member.is_there_ferrule_insert_in_tube=is_there_ferrule_insert_in_tube
      member.ferrule_length=ferrule_length
      member.inch1=inch1
      member.mm1 =mm1
      member.ferrule_id=ferrule_id
      member.inch2=inch2
      member.mm2=mm2
      member.tube_material_of_tubes=tube_material_of_tubes
      member.tube_material_of_raws= tube_material_of_raws
      member.tube_material_of_thermo=tube_material_of_thermo
      member.tube_material_of_supports=tube_material_of_supports
      member.tube_material_of_plugs=tube_material_of_plugs
      member.tube_material_of_coolent_tubes=tube_material_of_coolent_tubes
      member.tube_spacing_or_pitch=tube_spacing_or_pitch
      member.inch3=inch3
      member.mm3=mm3
      member.total_tube_length=total_tube_length
      member.inch4=inch4
      member.mm4=mm4
      member.top_tube_sheet_thickness=top_tube_sheet_thickness
      member.inch5=inch5
      member.mm5=mm5
      member.bottom_tube_sheet_thickness=bottom_tube_sheet_thickness
      member.inch6=inch6
      member.mm6=mm6
      member.tube_protude_out_of_top_tube_sheet= tube_protude_out_of_top_tube_sheet
      member.inch7=inch7
      member.mm8 =mm8
      member.tube_protude_out_of_bottom_tube_sheet= tube_protude_out_of_bottom_tube_sheet
      member.inch8=inch8
      member.mm8=mm8
      member.top_dom_removable=top_dom_removable
      member.top_inlet_accessible=top_inlet_accessible
      member.top_inlet_impingment_plate=top_inlet_impingment_plate
      member.any_projections_on_tube_sheet_describe=any_projections_on_tube_sheet_describe
      member.tube_sheet_material=tube_sheet_material
      member.dom_material=dom_material
      member.tube_spacing_proof_document=tube_spacing_proof_document
      member.reactor_tube_sheet_drawings=reactor_tube_sheet_drawings
      member.reactor_elevation_view_drawings=reactor_elevation_view_drawings
      member.other_drawings=other_drawings
      
      
      member.save()

      return redirect('/tm/clients')

def updatettdrecord(request, id):

      abbreviation =  request.GET['abbreviation']
      alternate_name =  request.GET['alternate_name']
      serial_number =  request.GET['serial_number']
      asset_number =  request.GET['asset_number']
      pm_status =  request.GET['pm_status']
      warehouse_name =  request.GET['warehouse_name']
      location_for_storage =  request.GET['location_for_storage']
      packaging =  request.GET['packaging']
      is_this_part_of_set =  request.GET['is_this_part_of_set']
      if_yes_how_many_in_a_set=  request.GET['if_yes_how_many_in_a_set']
      
    
      member =TTD.objects.get(id=id)
    
      member.abbreviation=  abbreviation
      member.alternate_name=  alternate_name
      member.serial_number=  serial_number
      member.asset_number=  asset_number
      member.pm_status=  pm_status
      member.location_for_warehouse=  warehouse_name
      member.location_for_storage=  location_for_storage
      member.packaging=  packaging
      member.is_this_part_of_set=  is_this_part_of_set
      member.if_yes_how_many_in_a_set= if_yes_how_many_in_a_set
           
    
      member.save()

      return redirect('/tm/warehouse')
      
def updatebddrecord(request, id):

      abbreviation =  request.POST['abbreviation']
      alternate_name =  request.POST['alternate_name']
      serial_number =  request.POST['serial_number']
      asset_number =  request.POST['asset_number']
      pm_status =  request.POST['pm_status']
      warehouse_name =  request.POST['warehouse_name']
      location_for_storage =  request.POST['location_for_storage']
      packaging =  request.POST['packaging']
      is_this_part_of_set =  request.POST['is_this_part_of_set']
      if_yes_how_many_in_a_set=  request.POST['if_yes_how_many_in_a_set']
    
      member =BDD.objects.get(id=id)
    
      member.abbreviation=  abbreviation
      member.alternate_name=  alternate_name
      member.serial_number=  serial_number
      member.asset_number=  asset_number
      member.pm_status=  pm_status
      member.location_for_warehouse=  warehouse_name
      member.location_for_storage=  location_for_storage
      member.packaging=  packaging
      member.is_this_part_of_set=  is_this_part_of_set
      member.if_yes_how_many_in_a_set= if_yes_how_many_in_a_set
    
      member.save()

      return redirect('/tm/warehouse')
      
def updatecalstandrecord(request, id):

      abbreviation =  request.POST['abbreviation']
      alternate_name =  request.POST['alternate_name']
      serial_number =  request.POST['serial_number']
      asset_number =  request.POST['asset_number']
      pm_status =  request.POST['pm_status']
      warehouse_name =  request.POST['warehouse_name']
      location_for_storage =  request.POST['location_for_storage']
      packaging =  request.POST['packaging']
      is_this_part_of_set =  request.POST['is_this_part_of_set']
      if_yes_how_many_in_a_set=  request.POST['if_yes_how_many_in_a_set']
    
      member =CALIBRATION_STAND.objects.get(id=id)
    
      member.abbreviation=  abbreviation
      member.alternate_name=  alternate_name
      member.serial_number=  serial_number
      member.asset_number=  asset_number
      member.pm_status=  pm_status
      member.location_for_warehouse=  warehouse_name
      member.location_for_storage=  location_for_storage
      member.packaging=  packaging
      member.is_this_part_of_set=  is_this_part_of_set
      member.if_yes_how_many_in_a_set=if_yes_how_many_in_a_set
    
      member.save()

      return redirect('/tm/warehouse')

       

           

def contacts(request):

     return render(request,'contacts.html')





def address(request):

    # if request.method=='POST' and 'add_official' in request.POST:

    #     if request.POST.get('addressline1') and request.POST.get('addressline2') and request.POST.get('addressline3') and request.POST.get('City') and request.POST.get('State') and request.POST.get('Country') and request.POST.get('Zipcode'):

    #       app1=Address()

           

         

    #       app1.addressline1=request.POST.get('addressline1')

    #       request.session['office_addressline1'] = request.POST['addressline1']

    #       app1.addressline2=request.POST.get('addressline2')

    #       request.session['office_addressline2'] = request.POST['addressline2']

    #       app1.addressline3=request.POST.get('addressline3')

    #       request.session['office_addressline3'] = request.POST['addressline3']

    #       app1.City=request.POST.get('City')

    #       request.session['office_city'] = request.POST['City']

    #       app1.State=request.POST.get('State')

    #       request.session['office_state'] = request.POST['State']

    #       app1.Country=request.POST.get('Country')

    #       request.session['office_country'] = request.POST['Country']

    #       app1.Zipcode=request.POST.get('Zipcode')

    #       request.session['office_zipcode'] = request.POST['Zipcode']

    #       app1.save()

           

    #       address= Address.objects.all()

    #       return redirect('/tm/clients')

           

           

    # if request.method=='POST' and 'add_shipping' in request.POST:

    #     if request.POST.get('addressline1') and request.POST.get('addressline2') and request.POST.get('addressline3') and request.POST.get('City') and request.POST.get('State') and request.POST.get('Country') and request.POST.get('Zipcode'):

    #       app1=Address()

        

    #       app1.addressline1=request.POST.get('addressline1')

    #       request.session['shipping_addressline1'] = request.POST['addressline1']

    #       app1.addressline2=request.POST.get('addressline2')

    #       request.session['shipping_addressline2'] = request.POST['addressline2']

    #       app1.addressline3=request.POST.get('addressline3')

    #       request.session['shipping_addressline3'] = request.POST['addressline2']

    #       app1.City=request.POST.get('City')

    #       request.session['shipping_city'] = request.POST['City']

    #       app1.State=request.POST.get('State')

    #       request.session['shipping_state'] = request.POST['State']

    #       app1.Country=request.POST.get('Country')

    #       request.session['shipping_country'] = request.POST['Country']

    #       app1.Zipcode=request.POST.get('Zipcode')

    #       request.session['shipping_zipcode'] = request.POST['Zipcode']

    #       app1.save()

           

    #       address= Address.objects.all()

    #       return redirect('/tm/clients')

           

    # if request.method=='POST' and 'add_plantentrance' in request.POST:

    #     if request.POST.get('addressline1') and request.POST.get('addressline2') and request.POST.get('addressline3') and request.POST.get('City') and request.POST.get('State') and request.POST.get('Country') and request.POST.get('Zipcode') and request.POST.get('oaddressline1') and request.POST.get('oaddressline2') and request.POST.get('oaddressline3') and request.POST.get('oCity') and request.POST.get('oState') and request.POST.get('oCountry') and request.POST.get('oZipcode') and request.POST.get('saddressline1') and request.POST.get('saddressline2') and request.POST.get('saddressline3') and request.POST.get('sCity') and request.POST.get('sState') and request.POST.get('sCountry') and request.POST.get('sZipcode'):

    #       app1=Address()

          

    #       app1.addressline1=request.POST.get('addressline1')

    #       app1.addressline2=request.POST.get('addressline2')

    #       app1.addressline3=request.POST.get('addressline3')

    #       app1.City=request.POST.get('City')

    #       app1.State=request.POST.get('State')

    #       app1.Country=request.POST.get('Country')

    #       app1.Zipcode=request.POST.get('Zipcode')

    #       app1.save()

           

    #       address= Address.objects.all()

    #       return redirect('/tm/clients')

           

    if request.method=='POST' and 'same_as_official' in request.POST:

    

          app1=Address()

         

          app1.addressline1 = request.session.get('office_addressline1')

          app1.addressline2 = request.session.get('office_addressline2')

          app1.addressline3 =request.session.get('office_addressline3')

          app1.City=request.session.get('office_city')

          app1.State=request.session.get('office_state')

          app1.Country=request.session.get('office_country')

          app1.Zipcode=request.session.get('office_zipcode')

          app1.save()

           

          address= Address.objects.all()

          return redirect('/tm/clients')

           

    if request.method=='POST' and 'same_as_shipping' in request.POST:

    

          app1=Address()

         

          app1.addressline1 = request.session.get('shipping_addressline1')

          app1.addressline2 = request.session.get('shipping_addressline2')

          app1.addressline3 =request.session.get('shipping_addressline3')

          app1.City=request.session.get('shipping_city')

          app1.State=request.session.get('shipping_state')

          app1.Country=request.session.get('shipping_country')

          app1.Zipcode=request.session.get('shipping_zipcode')

          app1.save()

          app1.save()

           

          address= Address.objects.all()

          return redirect('/tm/address')

    else:

   

     address= Address.objects.all()

     return render(request,'address.html',{'address':address})

   





# class IndexView(ListView):

#     template_name='crud/index.html'

#     context_object_name = 'post_list'

 

#     def get_queryset(self):

#         return Post.objects.all()

 

# class PostDetailView(DetailView):

#     model=Post

#     template_name = 'crud/post-detail.html'

 

# def postview(request):

#     if request.method == 'POST':

#         form = PostForm(request.POST)

 

#         if form.is_valid():

#             form.save()

#             return redirect('index')

 

#     form = PostForm()

#     return render(request,'crud/post.html',{'form': form})

 

# def edit(request, pk, template_name='crud/edit.html'):

#     post= get_object_or_404(Post, pk=pk)

#     form = PostForm(request.POST or None, instance=post)

#     if form.is_valid():

#         form.save()

#         return redirect('index')

#     return render(request, template_name, {'form':form})

 

# def delete(request, pk, template_name='crud/confirm_delete.html'):

#     post= get_object_or_404(Post, pk=pk)    

#     if request.method=='POST':

#         post.delete()

#         return redirect('index')

#     return render(request, template_name, {'object':post})

