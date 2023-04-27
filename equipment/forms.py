from django import forms
from equipment.models import *
from part.models import *
from django.db.models import Q

class TTDForm(forms.ModelForm):
    
    class Meta:
        model = TTD
        fields = "__all__"
    def __init__(self, *args, **kwargs) -> None:
        
        super(TTDForm, self).__init__(*args, **kwargs)
        if self.instance.id and self.instance.supply_orifice_set:
            
            q = Q(id=self.instance.supply_orifice_set.id) | Q(TTD__supply_orifice_set__isnull=True)
            
            self.fields['supply_orifice_set'].queryset =  Supply_orifice.objects.filter(q)

        else:
            self.fields['supply_orifice_set'].queryset =  Supply_orifice.objects.filter(TTD__supply_orifice_set__isnull=True)

        if self.instance.id and self.instance.pressure_sensor:
            q = Q(id=self.instance.pressure_sensor.id) | Q(TTD__pressure_sensor__isnull=True)
            
            self.fields['pressure_sensor'].queryset =  Pressure_sensor.objects.filter(q)
        
        else:
            self.fields['pressure_sensor'].queryset =  Pressure_sensor.objects.filter(TTD__pressure_sensor__isnull=True)
        

        if self.instance.id and self.instance.TTD_tube_seal_rack:
            q = Q(id=self.instance.TTD_tube_seal_rack.id) | Q(TTD__pressure_sensor__isnull=True)
            
            self.fields['TTD_tube_seal_rack'].queryset =  TTD_tube_seal_rack.objects.filter(q)
        
        else:
            self.fields['TTD_tube_seal_rack'].queryset =  TTD_tube_seal_rack.objects.filter(TTD__TTD_tube_seal_rack__isnull=True)
            
            
class BDDForm(forms.ModelForm):
    
    class Meta:
        model = BDD
        fields = "__all__"
        
    def __init__(self, *args, **kwargs):
        super(BDDForm, self).__init__(*args, **kwargs)
        
        if self.instance.id and self.instance.BDD_tube_seal_rack:
            q = Q(id = self.instance.BDD_tube_seal_rack.id) | Q(bdd__BDD_tube_seal_rack__isnull=True)
            self.fields['BDD_tube_seal_rack'].queryset =  BDD_tube_seal_rack.objects.filter(q)
            
        else:
            self.fields['BDD_tube_seal_rack'].queryset =  BDD_tube_seal_rack.objects.filter(bdd__BDD_tube_seal_rack__isnull=True)
            

class SwabMasterForm(forms.ModelForm):
    
    class Meta:
        model = SwabMaster
        fields = "__all__"
        
        
    def __init__(self, *args, **kwargs):
        super(SwabMasterForm, self).__init__(*args, **kwargs)
        
        if self.instance.id and self.instance.Swab_Master_Tube_Seal_Rack:
            q = Q(id = self.instance.Swab_Master_Tube_Seal_Rack.id) | Q(swabmaster__Swab_Master_Tube_Seal_Rack__isnull=True)
            self.fields['Swab_Master_Tube_Seal_Rack'].queryset = SwabMasterTSR.objects.filter(q)
            # SwabMasterTSR.objects.filter(q)
            return None
        
        else:
            self.fields['Swab_Master_Tube_Seal_Rack'].queryset = SwabMasterTSR.objects.filter(swabmaster__Swab_Master_Tube_Seal_Rack__isnull=True)
           
           
class CALIBRATION_STANDForm(forms.ModelForm):
    
    class Meta:
        model = CALIBRATION_STAND
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(CALIBRATION_STANDForm, self).__init__(*args, **kwargs)
        
        if self.instance.id and self.instance.calibration_orifice_set:
            q = Q(id = self.instance.calibration_orifice_set.id) | Q(calibration__calibration_orifice_set__isnull=True)
            self.fields['calibration_orifice_set'].queryset = Calibration_orifice.objects.filter(q)
            # SwabMasterTSR.objects.filter(q)        
        else:
            self.fields['calibration_orifice_set'].queryset = Calibration_orifice.objects.filter(calibration__calibration_orifice_set__isnull=True)

    
 
        