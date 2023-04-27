
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib import admin
from django.core.validators import DecimalValidator
from django.core.validators import MaxLengthValidator
from smart_selects.db_fields import ChainedForeignKey
from smart_selects.db_fields import ChainedManyToManyField
from smart_selects.db_fields import GroupedForeignKey
from django_countries.fields import CountryField

class Client(models.Model):
   
    official_name=models.CharField(max_length=128,verbose_name="Client Name", blank=True)
    comman_name=models.CharField(max_length=128,blank=True,verbose_name="Comman Name")
    alternate_name=models.CharField(max_length=128,blank=True,verbose_name="Alternate Name")
   
    parent_company=models.CharField(max_length=128,blank=True,verbose_name="Parent Company")
    former_name=models.CharField(max_length=128,blank=True,verbose_name="Former Name") 
    official_address = models.ManyToManyField("Address",related_name="official_address",verbose_name="Official Adrress", blank=True)
    shipping_address =models.ManyToManyField("Address",related_name="shipping_address",verbose_name="Shipping Address", blank=True)
    plantentrance_address =models.ManyToManyField("Address",related_name="plantentrance_address",verbose_name="Plant Entrance Address", blank=True)
    contact_person=models.CharField(max_length=128,blank=True,verbose_name="Contact Person")
    contact_person_phone=PhoneNumberField(max_length=128,blank=True,verbose_name="Contact Person Phone")
    contact_person_email=models.EmailField(max_length=128,blank=True,verbose_name="Contact Person Email")
    # plant=models.ManyToManyField("Plant",related_name="client Plant+") 
    country = CountryField(null=True, blank=True, default = "")
    def Official_Address(self):
        return ",".join([str(i) for i in self.official_address.all()])
        
    def Shipping_Address(self):
        return ",".join([str(i) for i in self.shipping_address.all()])
        
    def Plantentrance_address(self):
        return ",".join([str(i) for i in self.plantentrance_address.all()])
        
    
    def __str__(self):
       return self.official_name

# class Contact(models.Model):
#    client= models.ForeignKey(Client,on_delete=models.SET_NULL,null=True,related_name="Client Contact+")
#    first_name=models.CharField(max_length=128,blank=True)
#    last_name=models.CharField(max_length=128,blank=True)
#    title=models.CharField(max_length=128,blank=True)
#    company=models.CharField(max_length=128,blank=True)
#    phone_office=PhoneNumberField(max_length=128,blank=True)
#    phone_cell=PhoneNumberField(max_length=128,blank=True)
#    phone_direct=PhoneNumberField(max_length=128,blank=True)
#    fax= PhoneNumberField(max_length=128,blank=True)
#    email=models.CharField(max_length=128,blank=True)
#    def __str__(self):
#       return self.first_name
   
   
class Address(models.Model):
    # client= models.ForeignKey(Client,on_delete=models.SET_NULL,null=True,related_name="Client Address+")
    addressline1=models.CharField(max_length=128,blank=True)
    addressline2=models.CharField(max_length=128,blank=True)
    addressline3=models.CharField(max_length=128,blank=True)
    City=models.CharField(max_length=128,blank=True)
    State=models.CharField(max_length=128,blank=True)
    Country=models.CharField(max_length=128,blank=True)
    Zipcode=models.CharField(max_length=128,blank=True)
   
    
    def __str__(self):
      return f"{self.City} {self.addressline2} {self.addressline3}"
       
CHOICES_TOP_DOME_REMOVABLE = (
    (True, ('yes')),
    (False, ('No'))
)

class Plant(models.Model):

   client= models.ForeignKey(Client,on_delete=models.SET_NULL,null=True,related_name="clientplant+", blank=True)
   plant_location=models.CharField(max_length=128,blank=True,verbose_name="Plant Location")
   plant_contact=PhoneNumberField(max_length=128,blank=True,verbose_name="Plant Contact")
#   name_of_unit=models.ManyToManyField("Unit",related_name="plant Unit+") 
 
   def __str__(self):
       return self.plant_location
       


class Unit(models.Model):
    
    client= models.ForeignKey(Client,on_delete=models.SET_NULL,null=True,blank=True,related_name="clientunit+")
    # plant= models.ForeignKey(Plant,on_delete=models.SET_NULL,null=True,related_name="plantunit+")
    # plant = ChainedForeignKey(
    #     Plant,
    #     chained_field="client",
    #     chained_model_field="client",
    #     related_name="plantunit"
    #     )
    # country = ChainedForeignKey(
    #     Plant,
    #     chained_field="client",
    #     chained_model_field="client",
    #     show_all=False,
    #     auto_choose=True,
    #     sort=True,related_name="unitcountry")
    plant = GroupedForeignKey(Plant, "client",related_name="unitplant",default="",blank=True, null=True)
    name_of_unit=models.CharField(max_length=128,blank=True,verbose_name="Name Of Unit")
    chemical_being_manufactured_by_this_unit=models.CharField(max_length=128,blank=True,verbose_name="Chemical Being Manufactured By This Unit")
    # reactor_per_each_unit=models.ManyToManyField("Reactor",related_name="Unit Reactor+")  
  
    def __str__(self):
       return self.name_of_unit


       
class Reactor(models.Model):
    
    client= models.ForeignKey(Client,on_delete=models.SET_NULL,null=True,blank=True,related_name="reactorclient+")
    
    plant= GroupedForeignKey(Plant,"client",blank=True, null=True,related_name="reactorplant+")
    
    unit= models.ForeignKey(Unit,on_delete=models.CASCADE,null=True,blank=True  ,related_name="reactorunit+")
    
    reactor_name=models.CharField(max_length=128,blank=True,verbose_name="Reactor Name", )
    
    class tube_id(models.TextChoices):
      INCH='INCH',('INCH')
      MM='MM',('MM')
      
     
      
    tube_id=models.CharField(max_length=128,null=True,blank=True,verbose_name="Tube ID unit",choices=tube_id.choices)
    
    input_tubeid =models.DecimalField(blank=True,verbose_name='Tube ID value',null=True, decimal_places=3, max_digits=999)

    # mm=models.PositiveIntegerField(blank=True,verbose_name='MM',null=True)
   
    class CHOICES_FERRULE_INSERT_IN_TUBE(models.TextChoices):
      YES='YES',('YES')
      NO='NO',('NO')
      
    is_there_ferrule_insert_in_tube=models.CharField(max_length=128,null=True,blank=True,verbose_name=('Is There Ferrule Insert In Tube?'),choices=CHOICES_FERRULE_INSERT_IN_TUBE.choices)
    
   
    class ferrule_length(models.TextChoices):
      INCH='INCH',('INCH')
      MM='MM',('MM')
    
    # ferrule_length=models.DecimalField(decimal_places=3,max_digits=10,blank=True,null=True)
    
    ferrule_length =models.CharField(max_length=128,null=True,blank=True,verbose_name="Ferrule length unit",choices=ferrule_length.choices)
    
    input_ferrulelength= models.DecimalField(blank=True,verbose_name='ferrule length value',null=True, decimal_places=3,max_digits=999)
    # mm1 = models.PositiveIntegerField(blank=True,verbose_name='MM',null=True)
    
    class  ferrule_id(models.TextChoices):
      INCH='INCH',('INCH')
      MM='MM',('MM')
    
    # ferrule_id=models.DecimalField(decimal_places=3,max_digits=10,blank=True,null=True)
    ferrule_id =models.CharField(max_length=128,null=True,blank=True,verbose_name="Ferrule ID unit",choices=ferrule_id.choices)
     
    input_ferruleid = models.DecimalField(blank=True,verbose_name='Ferrule ID Value',null=True,decimal_places=3,max_digits=999)
    # mm2 = models.PositiveIntegerField(blank=True,verbose_name='MM',null=True)
    
    tube_material_of_tubes=models.PositiveIntegerField(blank=True,verbose_name='Number of Tubes',null=True)
    tube_material_of_raws=models.PositiveIntegerField(blank=True,verbose_name='Number of Rows',null=True)
    tube_material_of_thermo=models.PositiveIntegerField(blank=True,verbose_name='Number of Thermo',null=True)
    tube_material_of_supports=models.PositiveIntegerField(blank=True,verbose_name='Number of Supports',null=True)
    tube_material_of_plugs=models.PositiveIntegerField(blank=True,verbose_name='Number of Plugs',null=True)
    tube_material_of_coolent_tubes=models.PositiveIntegerField(blank=True,verbose_name='Number of coolant Tubes',null=True)
    
    class tube_spacing_or_pitch(models.TextChoices):
      INCH='INCH',('INCH')
      MM='MM',('MM')
    
    tube_spacing_or_pitch=models.CharField(null=True,blank=True,max_length=128,choices=tube_spacing_or_pitch.choices,verbose_name="Tube Spacing or Pitch Unit")
   
    input_tubespacing= models.DecimalField(max_digits=999,decimal_places=3,blank=True,verbose_name='Tube Spacing or Pitch Value',null=True)
    # mm3 = models.PositiveIntegerField(blank=True,verbose_name='MM',null=True)
    
    class total_tube_length(models.TextChoices):
      INCH='INCH',('INCH')
      MM='MM',('MM')
    
    total_tube_length=models.CharField(null=True,blank=True,max_length=128,verbose_name=('Total Tube Length Unit'),choices=total_tube_length.choices)
    
    input_totaltube = models.DecimalField(blank=True,verbose_name='Total Tube Length Value',null=True, decimal_places=3,max_digits=999)
    # mm4 = models.PositiveIntegerField(blank=True,verbose_name='MM',null=True)
    
    class top_tube_sheet_thickness(models.TextChoices):
      INCH='INCH',('INCH')
      MM='MM',('MM')
    
    top_tube_sheet_thickness=models.CharField(null=True,blank=True,max_length=128,verbose_name=('Top Tube Sheet Thickness Unit'),choices=top_tube_sheet_thickness.choices)
    
    input_toptube = models.DecimalField(blank=True,verbose_name='Top Tube Sheet Thickness Value',null=True, decimal_places=3,max_digits=999)
    # mm5 = models.PositiveIntegerField(blank=True,verbose_name='MM',null=True)
    
    class bottom_tube_sheet_thickness(models.TextChoices):
      INCH='INCH',('INCH')
      MM='MM',('MM')
      
    bottom_tube_sheet_thickness=models.CharField(blank=True, null=True,max_length=128,verbose_name=('Bottom Tube Sheet Thickness Unit'),choices=bottom_tube_sheet_thickness.choices)
    
    input_bottomtube= models.DecimalField(blank=True,verbose_name='Bottom Tube Sheet Thickness Value',null=True,decimal_places=3,max_digits=999)
    # mm6 = models.PositiveIntegerField(blank=True,verbose_name='MM',null=True)
    
    class CHOICES_TUBE_PROTUDE_OUT_OF_TOP_TUBE_SHEET (models.TextChoices):
      YES='YES',('YES')
      NO='NO',('NO')
    
    tube_protude_out_of_top_tube_sheet=models.CharField(blank=True, null=True,max_length=128,verbose_name=('Tube Protude Out Of Top Tube Sheet'),choices=CHOICES_TUBE_PROTUDE_OUT_OF_TOP_TUBE_SHEET.choices)
    
    class select_tube_protude_top(models.TextChoices):
      INCH='INCH',('INCH')
      MM='MM',('MM')
    
    select_tube_protude_top=models.CharField(blank=True, null=True,max_length=128,verbose_name=('Tube Protude Top Unit'),choices=select_tube_protude_top.choices,default="")
    
    input_tubeprotude_top = models.DecimalField(blank=True,verbose_name=('Tube Protude Top Value'),null=True,decimal_places=3,max_digits=999)
    # mm7 = models.PositiveIntegerField(blank=True,verbose_name='MM',null=True)
    
    class CHOICES_TUBE_PROTUDE_OUT_OF_BOTTOM_TUBE_SHEET (models.TextChoices):
      YES='YES',('YES')
      NO='NO',('NO')
    
    tube_protude_out_of_bottom_tube_sheet=models.CharField(blank=True, null=True,max_length=128,verbose_name=('Tube Protude Out Of Bottom Tube Sheet'),choices=CHOICES_TUBE_PROTUDE_OUT_OF_BOTTOM_TUBE_SHEET.choices)
    
    class select_tube_protude_bottom(models.TextChoices):
      INCH='INCH',('INCH')
      MM='MM',('MM')
      
    select_tube_protude_bottom=models.CharField(blank=True, null=True,max_length=128,verbose_name=('Tube Protude Out Of Bottom Tube Sheet Unit'),choices=select_tube_protude_bottom.choices,default="")
    
    
    input_tubeprotude_bottom = models.DecimalField(blank=True,verbose_name='Tube Protude Out Of Bottom Tube Sheet Value',null=True,decimal_places=3,max_digits=999)
    # mm8 =  models.PositiveIntegerField(blank=True,verbose_name='MM',null=True)
    
    class CHOICES_TOP_DOME_REMOVABLE(models.TextChoices):
      YES='YES',('YES')
      NO='NO',('NO')
    
    top_dome_removable=models.CharField(blank=True, null=True,max_length=128,verbose_name=('Top Dome Removable'),choices=CHOICES_TOP_DOME_REMOVABLE.choices)
    
    class CHOICES_TOP_INLET_ACCESSIBLE (models.TextChoices):
      YES='YES',('YES')
      NO='NO',('NO')
    
    top_inlet_accessible=models.CharField(blank=True, null=True,max_length=128,verbose_name=('Top Inlet Accessible'),choices=CHOICES_TOP_INLET_ACCESSIBLE.choices)
    
    class CHOICES_TOP_INLET_IMPINGMENT_PLATE (models.TextChoices):
      YES='YES',('YES')
      NO='NO',('NO')
    
    
    top_inlet_impingment_plate=models.CharField(blank=True, null=True,max_length=128,verbose_name=('Top Inlet Impingment Plate'),choices=CHOICES_TOP_INLET_IMPINGMENT_PLATE.choices)
    
    any_projections_on_tube_sheet_describe=models.CharField(null=True,blank=True,verbose_name="Any projections on tube sheet-describe",max_length=128)
    
    # def validate_geeks_mail(value):
    #  if "text" in value:
    #     return value
    #  else:
    #     raise ValidationError("This field accepts Only Text value.")
 
    tube_sheet_material=models.CharField(max_length=128,blank=True,verbose_name="Tube Sheet Material")
    
    dom_material=models.CharField(validators=[MaxLengthValidator(200)],max_length=128,blank=True,verbose_name="DOME")
    
    tube_spacing_proof_document=models.FileField(upload_to='document/',blank=True,null=True,verbose_name="Tube Spacing Proof Document")
    reactor_tube_sheet_drawings= models.FileField(upload_to='images/',null=True,blank=True,verbose_name="Reactor Tube Sheet Drawings")
    reactor_elevation_view_drawings= models.FileField(upload_to='images/',null=True,blank=True,verbose_name="Reactor Elevation View Drawings")
    other_drawings= models.FileField(upload_to='images/',null=True,blank=True,verbose_name="Other Drawings")
    
    def __str__(self):
       return self.reactor_name
    
    # CATALYST 
    catalyst_name=models.CharField(max_length=128,blank=True)
    model_number=models.CharField(max_length=128,blank=True)
    manufacturer=models.CharField(max_length=128,blank=True)
    class shape(models.TextChoices):
        TQ='TQ',('TQ')
        TABLET='TABLET',('TABLET')
        EXTRADIET='EXTRADIET',('EXTRADIET')
        CYLINDER='CYLINDER',('CYLINDER')
        PENTERING_CYLINDER='PENTERING_CYLINDER',('PENTERING_CYLINDER')
        SPHERE='SPHERE',('SPHERE')
        OTHER='OTHER',('OTHER')
        
    shape=models.CharField(max_length=20,choices=shape.choices,default=shape.TQ, blank=True)

    length=models.CharField(max_length=128,blank=True)
    width=models.CharField(max_length=128,blank=True)
    height=models.CharField(max_length=128,blank=True)
    inner_diameter=models.CharField(max_length=128,blank=True)
    outer_diameter=models.CharField(max_length=128,blank=True)

    crush_strength=models.CharField(max_length=128,blank=True)
    MSDS=models.FileField(upload_to='MSDS_files/',null=True,blank=True)

    CHOICES_TOP_SPRING = (
      (True, ('yes')),
      (False, ('No'))
    )
    
    # LOADING 
    catalyst_to_be_loaded=models.CharField(max_length=128,blank=True)
    layers_of_catalyst=models.CharField(max_length=128,blank=True)
    layers_of_inerts=models.CharField(max_length=128,blank=True)
    tube_loading_profile_drawing=models.FileField(upload_to='tube_loading_profile_drawings/',null=True,verbose_name="Tube Loading Profile Drawings",blank=True)
    loaded_tube_length_in=models.CharField(max_length=128,blank=True)
    loaded_tube_length_mm=models.CharField(max_length=128,blank=True)
    class tube_bottom_retainer(models.TextChoices):
      SPRING='SPRING',('SPRING')
      WIREMESH='WIREMESH',('WIREMESH')
      OTHER='OTHER',('OTHER')
    tube_bottom_retainer=models.CharField(max_length=20,choices=tube_bottom_retainer.choices,default=tube_bottom_retainer.SPRING,blank=True, null=True)
    top_spring=models.BooleanField(verbose_name=('top_spring'),choices=CHOICES_TOP_SPRING,default="True",blank=True)
    spring_height=models.CharField(max_length=128,blank=True)
    spring_drawing=models.FileField(upload_to='spring_drawing/',null=True,blank=True) 
       
# class DropdownModel(models.Model):

#     CHOICES = (
#         ('Today', 'Today'),
#         ('Yesterday', 'Yesterday'),
#         ('Last 7 Days', 'Last 7 Days'),
#         ('Last 14 Days', 'Last 14 Days'),
#         ('Last 30 Days', 'Last 30 Days'),
#         ('Last 60 Days', 'Last 60 Days'),
#         ('Last 90 Days', 'Last 90 Days'),
#         ('This Year', 'This Year'),
#         ('All Time', 'All Time'),
#         ('Custom', 'Custom')
#     )

#     date_range = models.CharField(max_length=15)
#     start_date = models.DateField()
#     end_date = models.DateField()






      
# class CategoryField(models.Model):
    
#     class SELECT_FIELD_CHOICES(models.TextChoices):
#       value1='value1',('value1')
#       value2='value2',('value2')
#       value3='value3',('value3')
      
#     selectfield = models.IntegerField(choices=SELECT_FIELD_CHOICES.choices, default=1)
#     verified = models.BooleanField(default=True, verbose_name='Required?')       
