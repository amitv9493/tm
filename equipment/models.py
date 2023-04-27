from django.db import models
from tube.models import Warehouse
from part.models import Supply_orifice
from part.models import Pressure_sensor
from part.models import TTD_tube_seal_rack
from part.models import BDD_tube_seal_rack
from part.models import Calibration_orifice

from django import forms
       
   
       
class TTD(models.Model):
    
    #  name=models.CharField(max_length=128,blank=True)
     abbreviation=models.CharField(max_length=128,blank=True,null=True)
     alternate_name=models.CharField(max_length=128,null=True,blank=True,verbose_name="Alternate Name")
     serial_number=models.CharField(max_length=128,null=True,blank=True,verbose_name="Serial Number")
     asset_number=models.CharField(max_length=128,null=True,blank=True,verbose_name="Asset Number")
     class pm_status(models.TextChoices):
        RED= 'RED', ('RED')
        BLUE= 'BLUE', ('BLUE')
        GREEN= 'GREEN', ('GREEN')
     pm_status = models.CharField(
        max_length=20,
        choices=pm_status.choices,
      verbose_name="PM Status",
      null=True,
      blank=True,
    )
     remarks = models.CharField(blank=True, null=True, max_length=999)
     
     location_for_warehouse=models.ForeignKey("tube.Warehouse",verbose_name="Location For Warehouse",default="",on_delete=models.CASCADE)
     location_for_storage=models.CharField(max_length=128,blank=True,verbose_name="Location For Storage")
     packaging=models.CharField(max_length=128,blank=True)
     class is_this_part_of_set(models.TextChoices):
         YES='YES',('YES')
         NO='NO',('NO')
     
     is_this_part_of_set=models.CharField(max_length=128,choices=is_this_part_of_set.choices,verbose_name="Is This Part Of Set",null=True, blank=True)
     if_yes_how_many_in_a_set=models.CharField(max_length=128,blank=True,verbose_name="If Yes How Many In A Set?")
    #  class  is_it_an_assembly(models.TextChoices):
    #      YES='YES',('YES')
    #      NO='NO',('NO')
    #  is_it_an_assembly=models.CharField(max_length=128,blank=True,choices=is_it_an_assembly.choices,default=is_it_an_assembly.YES)
     
    #  allow_to_add_sub_parts=models.ManyToManyField("Part",verbose_name="Allowed To Add Sub Parts")
    #  TTD_SN = models.CharField(max_length=128,blank=True)
     supply_orifice_set = models.OneToOneField("part.Supply_orifice",verbose_name="Supply Orifice Set",blank=True,null=True,on_delete=models.CASCADE,default="", related_name='TTD')
     pressure_sensor  = models.OneToOneField("part.Pressure_sensor",verbose_name="Pressure Sensor",blank=True,null=True,on_delete=models.CASCADE,default="", related_name='TTD')
     TTD_tube_seal_rack  =models.OneToOneField("part.TTD_tube_seal_rack",verbose_name="TTD Tube Seal Rack",blank=
     True,null=True,on_delete=models.CASCADE,default="", related_name='TTD')
     frame=models.CharField(max_length=128,blank=True)
     image=models.ImageField(upload_to='uploads/ttd/',default="",blank=True)
 
       

     def __str__(self):
      return f"{self.serial_number} - {self.pm_status} - {self.location_for_warehouse}"
     
     class Meta:   
        verbose_name = "TTD"
    
     class ttdChoiceField(forms.ModelChoiceField):
         def label_from_instance(self, obj):
             return f"{obj.serial_number} - {obj.pm_status}"





class BDD(models.Model):
    
    #  name=models.CharField(max_length=128,blank=True)
     abbreviation=models.CharField(max_length=128,blank=True)
     alternate_name=models.CharField(max_length=128,blank=True,verbose_name="Alternate Name")
     serial_number=models.CharField(max_length=128,blank=True,verbose_name="Serial Number")
     asset_number=models.CharField(max_length=128,blank=True,verbose_name="Asset Number")
     class pm_status(models.TextChoices):
        RED= 'RED', ('RED')
        BLUE= 'BLUE', ('BLUE')
        GREEN= 'GREEN', ('GREEN')
     pm_status = models.CharField(
        max_length=20,
        choices=pm_status.choices,
        verbose_name="PM Status",
        null=True,
        blank=True, 
    )
     remarks = models.CharField(blank=True, null=True, max_length=999)
     
    
     location_for_warehouse=models.ForeignKey("tube.Warehouse",verbose_name="Location For Warehouse",default="",on_delete=models.CASCADE,null=True)
     location_for_storage=models.CharField(max_length=128,blank=True,verbose_name="Location For Storage")
     packaging=models.CharField(max_length=128,blank=True)
     class is_this_part_of_set(models.TextChoices):
         YES='YES',('YES')
         NO='NO',('NO')
     
     is_this_part_of_set=models.CharField(max_length=128,choices=is_this_part_of_set.choices,verbose_name="Is This Part Of Set?", null=True,blank=True)
     if_yes_how_many_in_a_set=models.CharField(max_length=128,blank=True,verbose_name="If Yes How Many In A Set?")
    #  class  is_it_an_assembly(models.TextChoices):
    #      YES='YES',('YES')
    #      NO='NO',('NO')
    #  is_it_an_assembly=models.CharField(max_length=128,blank=True,choices=is_it_an_assembly.choices,default=is_it_an_assembly.YES)
    #  allow_to_add_sub_parts=models.ManyToManyField("Part",verbose_name="Allowed To Add Sub Parts")
    #  BDD_SN = models.CharField(max_length=128,blank=True)
     BDD_tube_seal_rack  = models.OneToOneField("part.BDD_tube_seal_rack",verbose_name="BDD Tube Seal Rack",blank=True,null=True,on_delete=models.CASCADE,default="", related_name='bdd')
     frame=models.CharField(max_length=128,blank=True)
     image=models.ImageField(upload_to='uploads/bdd/',default="",blank=True)
     

     def __str__(self):
      return f"{self.serial_number} - {self.pm_status} - {self.location_for_warehouse}"
     
     class Meta:
         verbose_name = "BDD"
         
     class bddChoiceField(forms.ModelChoiceField):
        def label_from_instance(self, obj):
            return f" {obj.serial_number} - {obj.pm_status} "
     
class CALIBRATION_STAND(models.Model):
    
    #  name=models.CharField(max_length=128,blank=True)
     abbreviation=models.CharField(max_length=128,blank=True)
     alternate_name=models.CharField(max_length=128,blank=True,verbose_name="Alternate Name")
     serial_number=models.CharField(max_length=128,blank=True,verbose_name="Serial Number")
     asset_number=models.CharField(max_length=128,blank=True,verbose_name="Asset Number")
     class pm_status(models.TextChoices):
        RED= 'RED', ('RED')
        BLUE= 'BLUE', ('BLUE')
        GREEN= 'GREEN', ('GREEN')
     pm_status = models.CharField(
        max_length=20,
        choices=pm_status.choices,
        verbose_name="PM Status",
        null=True,
        blank=True,
    )
     remarks = models.CharField(blank=True, null=True, max_length=999)
     
     # warehouse_location=models.OneToOneField("Warehouse",verbose_name="Warehouse Location",default="",on_delete=models.SET_NULL,null=True)
     location_for_warehouse=models.ForeignKey("tube.Warehouse",verbose_name="Location For Warehouse",default="",on_delete=models.CASCADE)
     location_for_storage=models.CharField(max_length=128,blank=True,verbose_name="Location For Storage")
     packaging=models.CharField(max_length=128,blank=True)

     class is_this_part_of_set(models.TextChoices):
         YES='YES',('YES')
         NO='NO',('NO')
     
     is_this_part_of_set=models.CharField(max_length=128,choices=is_this_part_of_set.choices,verbose_name="Is This Part Of Set?", default=is_this_part_of_set.YES, blank=True)
     if_yes_how_many_in_a_set=models.CharField(max_length=128,blank=True,verbose_name="If Yes How Many In A Set?")
    #  class  is_it_an_assembly(models.TextChoices):
    #      YES='YES',('YES')
    #      NO='NO',('NO')
    #  is_it_an_assembly=models.CharField(max_length=128,blank=True,choices=is_it_an_assembly.choices,default=is_it_an_assembly.YES)
    #  allow_to_add_sub_parts=models.ManyToManyField("Part",verbose_name="Allowed To Add Sub Parts")
     cal_stand_size = models.CharField(max_length=128,blank=True,verbose_name="Calibration Stand Size")
     calibration_orifice_set  =models.OneToOneField("part.Calibration_orifice",verbose_name="Calibration Orifice Set",blank=True,null=True,on_delete=models.CASCADE,default="", related_name='calibration')
     frame=models.CharField(max_length=128,blank=True)
     image=models.ImageField(upload_to='uploads/cal_stand/',default="",blank=True)
     
       

     def __str__(self):
      return f"{self.serial_number} - {self.pm_status} - {self.location_for_warehouse}"
     
     class Meta:
         verbose_name = 'Calibration Rack'
         
     class calibrationChoiceField(forms.ModelChoiceField):
        def label_from_instance(self, obj):
            return f" {obj.serial_number} - {obj.pm_status} "
       

class SwabMaster(models.Model):
   
    '''Warehouse Info'''

    location_for_warehouse=models.ForeignKey("tube.Warehouse",verbose_name="Location For Warehouse",default="",on_delete=models.CASCADE)
    location_for_storage=models.CharField(max_length=128,blank=True,null=True,verbose_name="Location For Storage")
    packaging=models.CharField(max_length=128,blank=True,null=True)
    class is_this_part_of_set(models.TextChoices):
        YES='YES',('YES')
        NO='NO',('NO')
    
    is_this_part_of_set=models.CharField(max_length=128,choices=is_this_part_of_set.choices,verbose_name="Is This Part Of Set", null=True, blank=True)
    if_yes_how_many_in_a_set=models.CharField(max_length=128,blank=True,verbose_name="If Yes How Many In A Set?")


    abbreviation=models.CharField(max_length=128,blank=True,null=True)
    alternate_name=models.CharField(max_length=128,blank=True,null=True,verbose_name="Alternate Name")
    serial_number=models.CharField(max_length=128,blank=True,null=True,verbose_name="Serial Number")
    asset_number=models.CharField(max_length=128,blank=True,null=True,verbose_name="Asset Number")
    class pm_status(models.TextChoices):
        RED= 'RED', ('RED')
        BLUE= 'BLUE', ('BLUE')
        GREEN= 'GREEN', ('GREEN')

    pm_status = models.CharField(
    max_length=20,
    choices=pm_status.choices,
    verbose_name="PM Status",
    blank=True,
    null=True,
)
    remarks = models.CharField(blank=True, null=True, max_length=999)


    '''specification'''

    Swab_Master_Tube_Seal_Rack =  models.OneToOneField("part.SwabMasterTSR",blank=True, null=True, verbose_name=("SwabMaster Tube Seal Rack"), on_delete=models.CASCADE,related_name="swabmaster")
    Generation_1 = models.CharField(choices= is_this_part_of_set.choices, max_length=3, null=True, blank=True)
    Generation_2 = models.CharField(choices= is_this_part_of_set.choices, max_length=3, null=True, blank=True)

    def __str__(self):
        return f"{self.serial_number} {self.pm_status}"
        
    class Meta:
        verbose_name = "Swab Master"    

