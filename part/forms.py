from django.db import models  
from django.forms import fields  
from equipment.models import TTD
from django import forms  
  
  
class TTDImage(forms.ModelForm):  
    class meta:  
        # To specify the model to be used to create form  
        models = TTD
        # It includes all the fields of model  
        fields = '__all__'  