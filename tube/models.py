from django.db import models
from django.db.models.fields import CharField
from phonenumber_field.modelfields import PhoneNumberField
from datetime import date, time
from django.db import OperationalError
from django.db.models import Q
from django_countries.fields import CountryField
from django import forms


# Create your models here.




class Warehouse(models.Model):
    warehouse_name=models.CharField(max_length=128,blank=True)
    warehouse_location=models.CharField(max_length=128,blank=True)
    warehouse_contact=PhoneNumberField(max_length=128,blank=True)
    warehouse_email=models.EmailField(max_length=128,blank=True)
    warehouse_manager=models.CharField(max_length=128,blank=True)
    # warehouse_equipments=models.ManyToManyField("Equipment",related_name="warehouse_equipments",default="")
    # warehouse_parts=models.ManyToManyField("Part",related_name="warehouse_parts",default="")
    date_created = models.DateField(auto_now_add=True, null=True, blank=True)
    country = CountryField(null=True, blank=True)

    def __str__(self):
       return self.warehouse_name  
       
class Catalyst(models.Model):
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
#   class size(models.TextChoices):
#       LENGTH='LENGTH',('LENGTH')
#       WIDTH= 'WIDTH',('WIDTH')
#       HEIGHT='HEIGHT',('HEIGHT')
#       INNER_DIAMETER='INNER_DIAMETER',('INNER_DIAMETER')
#       OUTER_DIAMETER='OUTER_DIAMETER',('OUTER_DIAMETER')
#   size=models.CharField(max_length=20,choices=size.choices,default=size.LENGTH)
   
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

class Loading(models.Model):
    catalyst_to_be_loaded=models.CharField(max_length=128,blank=True)
    layers_of_catalyst=models.CharField(max_length=128,blank=True)
    layers_of_inerts=models.CharField(max_length=128,blank=True)
    tube_loading_profile_drawing=models.FileField(upload_to='tube_loading_profile_drawings/',null=True,verbose_name="Tube Loading Profile Drawings",blank=True)
    loaded_tube_length_in=models.CharField(max_length=128,blank=True)
    loaded_tube_length_mm=models.CharField(max_length=128,blank=True)
    # layer1=models.ForeignKey(Catalyst,null=True,on_delete=models.SET_DEFAULT,default="",verbose_name="Layer1",blank=True)   
    # layer2=models.ForeignKey(Catalyst,null=True,on_delete=models.SET_DEFAULT,default="",verbose_name="Layer2")   
    # layer3=models.ForeignKey(Catalyst,null=True,on_delete=models.SET_DEFAULT,default="",verbose_name="Layer3")   
    # layer4=models.ForeignKey(Catalyst,null=True,on_delete=models.SET_DEFAULT,default="",verbose_name="Layer4")  
    class tube_bottom_retainer(models.TextChoices):
      SPRING='SPRING',('SPRING')
      WIREMESH='WIREMESH',('WIREMESH')
      OTHER='OTHER',('OTHER')
    tube_bottom_retainer=models.CharField(max_length=20,choices=tube_bottom_retainer.choices,default=tube_bottom_retainer.SPRING,blank=True, null=True)
    top_spring=models.BooleanField(verbose_name=('top_spring'),choices=CHOICES_TOP_SPRING,default="True",blank=True)
    spring_height=models.CharField(max_length=128,blank=True)
    spring_drawing=models.FileField(upload_to='spring_drawing/',null=True,blank=True) 
    
    def __str__(self):
        return self.catalyst_to_be_loaded


    

   
