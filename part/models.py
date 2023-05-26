from django.db import models
from django.utils.translation import gettext as _

class Part(models.Model):
    part_name = models.CharField(max_length=128,blank=True)
    # part_no = models.CharField(max_length=128,blank=True)
    # part_function = models.CharField(max_length=128,blank=True)
    name_of_abbreviation = models.CharField(max_length=128,blank=True, verbose_name = "Abbreviation")
    # alternate_name = models.CharField(max_length = 128,blank=True)
    serial_number=models.CharField(max_length=128,blank=True)
    asset_number=models.CharField(max_length=128,blank=True)   
    # part_image=models.ImageField(upload_to ='uploads/', null=True, blank=True)
    # part_image= models.FileField(upload_to="uploads/", null=True, blank=True)
    class pm_status(models.TextChoices):    
        RED= 'RED', ('RED')
        BLUE= 'BLUE', ('BLUE')
        GREEN= 'GREEN', ('GREEN')
    pm_status = models.CharField(max_length=20,choices=pm_status.choices, null=True, blank=True)
<<<<<<< HEAD
    location_for_warehouse=models.ForeignKey("tube.Warehouse", on_delete=models.CASCADE, null=True, blank=True)
=======
    location_for_warehouse=models.ForeignKey("tube.Warehouse", on_delete=models.CASCADE, null=True, blank=True, related_name='part')
>>>>>>> main
    location_for_storage=models.CharField(max_length=128,blank=True)
    packaging=models.CharField(max_length=128,blank=True)
    notes = models.TextField(blank=True,null=True)

    upload_file = models.FileField(upload_to='media/images/general_parts', null=True, blank=True)
    price  = models.PositiveIntegerField(_("Price"), null=True, blank=True)
    
    class WeightChoices(models.TextChoices):
        KG = 'KG'
        LBS = 'LBS'
    weight_unit = models.CharField(_("Unit for Weight"),null=True,blank=True, max_length=50, choices=WeightChoices.choices)
    weight  = models.PositiveIntegerField(_("Weight"), null=True, blank=True)
    
    # Dimension     
    class LengthDimensionChoices(models.TextChoices):
        CM = 'CM'
        MM = 'MM'
        INCH = 'INCH'
    length = models.PositiveIntegerField(blank=True,null=True,)
    breadth  = models.PositiveIntegerField(blank=True,null=True,)
    height  = models.PositiveIntegerField(blank=True,null=True,)

    dimension_unit = models.CharField(_("Unit for Dimensions"),choices= LengthDimensionChoices.choices,blank=True,null=True, max_length=50)
    
    

    class is_this_part_of_set(models.TextChoices):
         YES='YES',('YES')
         NO='NO',('NO')
     
    # is_this_part_of_set=models.CharField(max_length=128,choices=is_this_part_of_set.choices, null=True, blank=True)
    class it_is_an_assembly(models.TextChoices):
         YES='YES',('YES')
         NO='NO',('NO')
     
    # it_is_an_assembly=models.CharField(max_length=128,choices=it_is_an_assembly.choices,null=True, blank=True)
    
    def __str__(self):
       return f'{self.part_name} -{self.serial_number}'
       
    class Meta:
        verbose_name='All General Part'
       
class Supply_orifice(models.Model):
    serial_number=models.CharField(max_length=128,blank=True, default="", null=True)
    size=models.CharField(max_length=128,blank=True)
    total_sets=models.CharField(max_length=128,blank=True)
    orifice_in_each_set=models.CharField(max_length=128,blank=True)
    storage_case=models.CharField(max_length=128,blank=True)
    location_for_warehouse=models.ForeignKey("tube.Warehouse",verbose_name="Location For Warehouse",default="",on_delete=models.CASCADE,null=True, blank=True, related_name="supply_orifice")
    
    
    # PART FIELDS FROM GENERAL PARTS 
       
# NEW FIELDS FROM ALL GENERAL PARTS 
    part_name = models.CharField(max_length=128,blank=True, null=True)
    name_of_abbreviation = models.CharField(max_length=128,blank=True, verbose_name = "Abbreviation")
    asset_number=models.CharField(max_length=128,blank=True)   
    class pm_status(models.TextChoices):    
        RED= 'RED', ('RED')
        BLUE= 'BLUE', ('BLUE')
        GREEN= 'GREEN', ('GREEN')
    pm_status = models.CharField(max_length=20,choices=pm_status.choices, null=True, blank=True)
    # location_for_warehouse=models.ForeignKey("tube.Warehouse", on_delete=models.CASCADE, null=True, blank=True)
    location_for_storage=models.CharField(max_length=128,blank=True)
    packaging=models.CharField(max_length=128,blank=True)
    notes = models.TextField(blank=True,null=True)
    upload_file = models.FileField(upload_to='media/images/general_parts', null=True, blank=True)
    price  = models.PositiveIntegerField(_("Price"), null=True, blank=True)
    
    class WeightChoices(models.TextChoices):
        KG = 'KG'
        LBS = 'LBS'
    weight_unit = models.CharField(_("Unit for Weight"),null=True,blank=True, max_length=50, choices=WeightChoices.choices)
    weight  = models.PositiveIntegerField(_("Weight"), null=True, blank=True)



    # Dimension     
    class LengthDimensionChoices(models.TextChoices):
        CM = 'CM'
        MM = 'MM'
        INCH = 'INCH'
    length = models.PositiveIntegerField(blank=True,null=True,)
    breadth  = models.PositiveIntegerField(blank=True,null=True,)
    height  = models.PositiveIntegerField(blank=True,null=True,)

    dimension_unit = models.CharField(_("Unit for Dimensions"),choices= LengthDimensionChoices.choices,blank=True,null=True, max_length=50)
    
     
    def __str__(self):
       return str(self.serial_number)

    class Meta:
        verbose_name = 'Supply Orifice'  
       

class Pressure_sensor(models.Model):
    serial_number=models.CharField(max_length=128,blank=True, default="", null=True)
    range=models.CharField(max_length=128,blank=True)
    quantity=models.CharField(max_length=128,blank=True)

    location_for_warehouse=models.ForeignKey("tube.Warehouse",verbose_name="Location For Warehouse",default="",on_delete=models.CASCADE,null=True, blank=True, related_name="pressure_sensor")

# NEW FIELDS FROM ALL GENERAL PARTS 
    part_name = models.CharField(max_length=128,blank=True, null=True)
    name_of_abbreviation = models.CharField(max_length=128,blank=True, verbose_name = "Abbreviation")
    asset_number=models.CharField(max_length=128,blank=True)   
    class pm_status(models.TextChoices):    
        RED= 'RED', ('RED')
        BLUE= 'BLUE', ('BLUE')
        GREEN= 'GREEN', ('GREEN')
    pm_status = models.CharField(max_length=20,choices=pm_status.choices, null=True, blank=True)
    # location_for_warehouse=models.ForeignKey("tube.Warehouse", on_delete=models.CASCADE, null=True, blank=True)
    location_for_storage=models.CharField(max_length=128,blank=True)
    packaging=models.CharField(max_length=128,blank=True)
    notes = models.TextField(blank=True,null=True)
    upload_file = models.FileField(upload_to='media/images/general_parts', null=True, blank=True)
    
    class WeightChoices(models.TextChoices):
        KG = 'KG'
        LBS = 'LBS'
    weight_unit = models.CharField(_("Unit for Weight"),null=True,blank=True, max_length=50, choices=WeightChoices.choices)
    weight  = models.PositiveIntegerField(_("Weight"), null=True, blank=True)
    price  = models.PositiveIntegerField(_("Price"), null=True, blank=True)

    # Dimension     
    class LengthDimensionChoices(models.TextChoices):
        CM = 'CM'
        MM = 'MM'
        INCH = 'INCH'
    length = models.PositiveIntegerField(blank=True,null=True,)
    breadth  = models.PositiveIntegerField(blank=True,null=True,)
    height  = models.PositiveIntegerField(blank=True,null=True,)

    dimension_unit = models.CharField(_("Unit for Dimensions"),choices= LengthDimensionChoices.choices,blank=True,null=True, max_length=50)
    



     
    def __str__(self):
       return str(self.serial_number)  
       
    class Meta:
        verbose_name = 'Pressure Sensor'

class TTD_tube_seal_rack(models.Model):
    serial_number=models.CharField(max_length=128,blank=True, default="", null=True)
    size=models.CharField(max_length=128,blank=True)
    qty_rack=models.CharField(max_length=128,blank=True)
    tube_seal_rack=models.CharField(max_length=128,blank=True)
    location_for_warehouse=models.ForeignKey("tube.Warehouse",verbose_name="Location For Warehouse",default="",on_delete=models.CASCADE,null=True, blank=True, related_name="ttd_rack")

# NEW FIELDS FROM ALL GENERAL PARTS 
    part_name = models.CharField(max_length=128,blank=True, null=True)
    name_of_abbreviation = models.CharField(max_length=128,blank=True, verbose_name = "Abbreviation")
    asset_number=models.CharField(max_length=128,blank=True)   
    class pm_status(models.TextChoices):    
        RED= 'RED', ('RED')
        BLUE= 'BLUE', ('BLUE')
        GREEN= 'GREEN', ('GREEN')
    pm_status = models.CharField(max_length=20,choices=pm_status.choices, null=True, blank=True)
    # location_for_warehouse=models.ForeignKey("tube.Warehouse", on_delete=models.CASCADE, null=True, blank=True)
    location_for_storage=models.CharField(max_length=128,blank=True)
    packaging=models.CharField(max_length=128,blank=True)
    notes = models.TextField(blank=True,null=True)
    upload_file = models.FileField(upload_to='media/images/general_parts', null=True, blank=True)

    price  = models.PositiveIntegerField(_("Price"), null=True, blank=True)
 
    class WeightChoices(models.TextChoices):
        KG = 'KG'
        LBS = 'LBS'
    weight_unit = models.CharField(_("Unit for Weight"),null=True,blank=True, max_length=50, choices=WeightChoices.choices)
    weight  = models.PositiveIntegerField(_("Weight"), null=True, blank=True)
    # Dimension     
    class LengthDimensionChoices(models.TextChoices):
        CM = 'CM'
        MM = 'MM'
        INCH = 'INCH'
    length = models.PositiveIntegerField(blank=True,null=True,)
    breadth  = models.PositiveIntegerField(blank=True,null=True,)
    height  = models.PositiveIntegerField(blank=True,null=True,)

    dimension_unit = models.CharField(_("Unit for Dimensions"),choices= LengthDimensionChoices.choices,blank=True,null=True, max_length=50)
    



    def __str__(self):
       return str(self.serial_number)  
    
    class Meta:
        verbose_name = 'TDD Tube Seal Rack'
       
    
class BDD_tube_seal_rack(models.Model):
    serial_number=models.CharField(max_length=128,blank=True, default="", null=True)
    size=models.CharField(max_length=128,blank=True)
    number_of_tubes = models.PositiveIntegerField(null=True, blank=True)
    location_for_warehouse=models.ForeignKey("tube.Warehouse",verbose_name="Location For Warehouse",default="",on_delete=models.CASCADE,null=True, blank=True, related_name="bdd_rack")

# NEW FIELDS FROM ALL GENERAL PARTS 
    part_name = models.CharField(max_length=128,blank=True, null=True)
    name_of_abbreviation = models.CharField(max_length=128,blank=True, verbose_name = "Abbreviation")
    asset_number=models.CharField(max_length=128,blank=True)   
    class pm_status(models.TextChoices):    
        RED= 'RED', ('RED')
        BLUE= 'BLUE', ('BLUE')
        GREEN= 'GREEN', ('GREEN')
    pm_status = models.CharField(max_length=20,choices=pm_status.choices, null=True, blank=True)
    # location_for_warehouse=models.ForeignKey("tube.Warehouse", on_delete=models.CASCADE, null=True, blank=True)
    location_for_storage=models.CharField(max_length=128,blank=True)
    packaging=models.CharField(max_length=128,blank=True)
    notes = models.TextField(blank=True,null=True)
    upload_file = models.FileField(upload_to='media/images/general_parts', null=True, blank=True)

    price  = models.PositiveIntegerField(_("Price"), null=True, blank=True)

    # Dimension     
    class LengthDimensionChoices(models.TextChoices):
        CM = 'CM'
        MM = 'MM'
        INCH = 'INCH'
    length = models.PositiveIntegerField(blank=True,null=True,)
    breadth  = models.PositiveIntegerField(blank=True,null=True,)
    height  = models.PositiveIntegerField(blank=True,null=True,)

    dimension_unit = models.CharField(_("Unit for Dimensions"),choices= LengthDimensionChoices.choices,blank=True,null=True, max_length=50)
 
    class WeightChoices(models.TextChoices):
        KG = 'KG'
        LBS = 'LBS'
    weight_unit = models.CharField(_("Unit for Weight"),null=True,blank=True, max_length=50, choices=WeightChoices.choices)
    weight  = models.PositiveIntegerField(_("Weight"), null=True, blank=True)



    def __str__(self):
       return str(self.serial_number)  
    
    class Meta:
        verbose_name = 'BDD Tube Seal Rack'
       
    
class Calibration_orifice(models.Model):
    serial_number=models.CharField(max_length=128,blank=True, default="", null=True)
    size=models.CharField(max_length=128,blank=True)
    total_sets=models.CharField(max_length=128,blank=True)
    in_sets=models.CharField(max_length=128,blank=True)
    location_for_warehouse=models.ForeignKey("tube.Warehouse",verbose_name="Location For Warehouse",default="",on_delete=models.CASCADE,null=True, blank=True, related_name="calibration_orifice")

# NEW FIELDS FROM ALL GENERAL PARTS 
    part_name = models.CharField(max_length=128,blank=True, null=True)
    name_of_abbreviation = models.CharField(max_length=128,blank=True, verbose_name = "Abbreviation")
    asset_number=models.CharField(max_length=128,blank=True)   
    class pm_status(models.TextChoices):    
        RED= 'RED', ('RED')
        BLUE= 'BLUE', ('BLUE')
        GREEN= 'GREEN', ('GREEN')
    pm_status = models.CharField(max_length=20,choices=pm_status.choices, null=True, blank=True)
    # location_for_warehouse=models.ForeignKey("tube.Warehouse", on_delete=models.CASCADE, null=True, blank=True)
    location_for_storage=models.CharField(max_length=128,blank=True)
    packaging=models.CharField(max_length=128,blank=True)
    notes = models.TextField(blank=True,null=True)
    upload_file = models.FileField(upload_to='media/images/general_parts', null=True, blank=True)

    price  = models.PositiveIntegerField(_("Price"), null=True, blank=True)

    # Dimension     
    class LengthDimensionChoices(models.TextChoices):
        CM = 'CM'
        MM = 'MM'
        INCH = 'INCH'
    length = models.PositiveIntegerField(blank=True,null=True,)
    breadth  = models.PositiveIntegerField(blank=True,null=True,)
    height  = models.PositiveIntegerField(blank=True,null=True,)

    dimension_unit = models.CharField(_("Unit for Dimensions"),choices= LengthDimensionChoices.choices,blank=True,null=True, max_length=50)
    

 
    class WeightChoices(models.TextChoices):
        KG = 'KG'
        LBS = 'LBS'
    weight_unit = models.CharField(_("Unit for Weight"),null=True,blank=True, max_length=50, choices=WeightChoices.choices)
    weight  = models.PositiveIntegerField(_("Weight"), null=True, blank=True)

    def __str__(self):
       return str(self.serial_number)  
    
    class Meta:
        verbose_name = 'Calibration Orifice'
    
class SwabMasterTSR(models.Model):
    serial_number=models.CharField(max_length=128,blank=True, default="", null=True)
    size=models.CharField(max_length=128,blank=True)
    qty_rack=models.CharField(max_length=128,blank=True)
    tube_seal_rack=models.CharField(max_length=128,blank=True)
    location_for_warehouse=models.ForeignKey("tube.Warehouse",verbose_name="Location For Warehouse",default="",on_delete=models.CASCADE,null=True, blank=True, related_name="swabmasterTSR")

# NEW FIELDS FROM ALL GENERAL PARTS 
    part_name = models.CharField(max_length=128,blank=True, null=True)
    name_of_abbreviation = models.CharField(max_length=128,blank=True, verbose_name = "Abbreviation")
    asset_number=models.CharField(max_length=128,blank=True)   
    class pm_status(models.TextChoices):    
        RED= 'RED', ('RED')
        BLUE= 'BLUE', ('BLUE')
        GREEN= 'GREEN', ('GREEN')
    pm_status = models.CharField(max_length=20,choices=pm_status.choices, null=True, blank=True)
    # location_for_warehouse=models.ForeignKey("tube.Warehouse", on_delete=models.CASCADE, null=True, blank=True)
    location_for_storage=models.CharField(max_length=128,blank=True)
    packaging=models.CharField(max_length=128,blank=True)
    notes = models.TextField(blank=True,null=True)
    upload_file = models.FileField(upload_to='media/images/general_parts', null=True, blank=True)
    price  = models.PositiveIntegerField(_("Price"), null=True, blank=True)

    # Dimension     
    class LengthDimensionChoices(models.TextChoices):
        CM = 'CM'
        MM = 'MM'
        INCH = 'INCH'
    length = models.PositiveIntegerField(blank=True,null=True,)
    breadth  = models.PositiveIntegerField(blank=True,null=True,)
    height  = models.PositiveIntegerField(blank=True,null=True,)

    dimension_unit = models.CharField(_("Unit for Dimensions"),choices= LengthDimensionChoices.choices,blank=True,null=True, max_length=50)
    
 
    class WeightChoices(models.TextChoices):
        KG = 'KG'
        LBS = 'LBS'
    weight_unit = models.CharField(_("Unit for Weight"),null=True,blank=True, max_length=50, choices=WeightChoices.choices)
    weight  = models.PositiveIntegerField(_("Weight"), null=True, blank=True)


    def __str__(self):
       return str(self.serial_number)

    class Meta:
        verbose_name= 'SwabMaster Tube Seal Rack'


class DeviceHose(models.Model):
    serial_number = models.CharField(max_length=999,null=True, blank=True)
    length = models.DecimalField(max_digits=999, decimal_places=3,null=True, blank=True)
    colour_code = models.CharField( max_length=50,null=True, blank=True)
    warehouse = models.ForeignKey("tube.Warehouse", on_delete=models.CASCADE,null=True, blank=True, related_name="devicehose")

# NEW FIELDS FROM ALL GENERAL PARTS 
    part_name = models.CharField(max_length=128,blank=True, null=True)
    name_of_abbreviation = models.CharField(max_length=128,blank=True, verbose_name = "Abbreviation")
    asset_number=models.CharField(max_length=128,blank=True)   
    class pm_status(models.TextChoices):    
        RED= 'RED', ('RED')
        BLUE= 'BLUE', ('BLUE')
        GREEN= 'GREEN', ('GREEN')
    pm_status = models.CharField(max_length=20,choices=pm_status.choices, null=True, blank=True)
    # location_for_warehouse=models.ForeignKey("tube.Warehouse", on_delete=models.CASCADE, null=True, blank=True)
    location_for_storage=models.CharField(max_length=128,blank=True)
    packaging=models.CharField(max_length=128,blank=True)
    notes = models.TextField(blank=True,null=True)
    upload_file = models.FileField(upload_to='media/images/general_parts', null=True, blank=True)

    price  = models.PositiveIntegerField(_("Price"), null=True, blank=True)

    # Dimension     
    class LengthDimensionChoices(models.TextChoices):
        CM = 'CM'
        MM = 'MM'
        INCH = 'INCH'
    length = models.PositiveIntegerField(blank=True,null=True,)
    breadth  = models.PositiveIntegerField(blank=True,null=True,)
    height  = models.PositiveIntegerField(blank=True,null=True,)

    dimension_unit = models.CharField(_("Unit for Dimensions"),choices= LengthDimensionChoices.choices,blank=True,null=True, max_length=50)
    
 
    class WeightChoices(models.TextChoices):
        KG = 'KG'
        LBS = 'LBS'
    weight_unit = models.CharField(_("Unit for Weight"),null=True,blank=True, max_length=50, choices=WeightChoices.choices)
    weight  = models.PositiveIntegerField(_("Weight"), null=True, blank=True)


    def __str__(self) -> str:
        
        return str(self.serial_number)
    
    class Meta:
        verbose_name = 'Device Hose'

class AirHose(models.Model):
    serial_number =  models.CharField(max_length=999,null=True, blank=True)
    colour_code = models.CharField(max_length=50,null=True, blank=True)
    warehouse = models.ForeignKey("tube.Warehouse", on_delete=models.CASCADE,null=True, blank=True, related_name="airhose")
    
    def __str__(self):
        return f'{self.length} Ft'
    
    class Meta:
        verbose_name = "Air Hose"
        
# NEW FIELDS FROM ALL GENERAL PARTS 
    part_name = models.CharField(max_length=128,blank=True, null=True)
    name_of_abbreviation = models.CharField(max_length=128,blank=True, verbose_name = "Abbreviation")
    asset_number=models.CharField(max_length=128,blank=True)   
    class pm_status(models.TextChoices):    
        RED= 'RED', ('RED')
        BLUE= 'BLUE', ('BLUE')
        GREEN= 'GREEN', ('GREEN')
    pm_status = models.CharField(max_length=20,choices=pm_status.choices, null=True, blank=True)
    # location_for_warehouse=models.ForeignKey("tube.Warehouse", on_delete=models.CASCADE, null=True, blank=True)
    location_for_storage=models.CharField(max_length=128,blank=True)
    packaging=models.CharField(max_length=128,blank=True)
    notes = models.TextField(blank=True,null=True)
    upload_file = models.FileField(upload_to='media/images/general_parts', null=True, blank=True)

    price  = models.PositiveIntegerField(_("Price"), null=True, blank=True)

    # Dimension     
    class LengthDimensionChoices(models.TextChoices):
        CM = 'CM'
        MM = 'MM'
        INCH = 'INCH'
    length = models.PositiveIntegerField(blank=True,null=True,)
    breadth  = models.PositiveIntegerField(blank=True,null=True,)
    height  = models.PositiveIntegerField(blank=True,null=True,)

    dimension_unit = models.CharField(_("Unit for Dimensions"),choices= LengthDimensionChoices.choices,blank=True,null=True, max_length=50)
    


 
    class WeightChoices(models.TextChoices):
        KG = 'KG'
        LBS = 'LBS'
    weight_unit = models.CharField(_("Unit for Weight"),null=True,blank=True, max_length=50, choices=WeightChoices.choices)
    weight  = models.PositiveIntegerField(_("Weight"), null=True, blank=True)