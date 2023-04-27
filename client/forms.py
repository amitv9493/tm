# listings/forms.py

from dal import autocomplete

from .models import Reactor, Unit
from django import forms
# from client.models import DropdownModel
# from client.models import Unit
# from client.models import Reactor

# class UnitModelForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['plant'].disabled = True
#         self.fields['plant'].widget.can_change_related = False
        
# class TubeidModelForm(forms.ModelForm):

#     class Meta:
#         model = TubeidModel
#         fields = ('value','value2')
    
#         value= forms.CharField()
 
# class ReactorModelForm(forms.ModelForm):

#     class Meta:
#         model =Reactor
#         fields = ('value1',)
    
#         value1= forms.CharField()      
        
       
        
# class CategoryFieldForm(forms.ModelForm):
    
#     class Meta:
#         model = CategoryField
#         fields = ('selectfield',)
#         widgets = {
#             'selectfield ': forms.Select(choices=SELECT_FIELD_CHOICES.choices)
#         }

class CommentForm(forms.Form):
    name = forms.CharField()
    url = forms.URLField()
    comment = forms.CharField(widget=forms.Textarea)
    
BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]

class SimpleForm(forms.Form):
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    favorite_colors = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=FAVORITE_COLORS_CHOICES,
    )
 

class ContactUsForm(forms.Form):
   name = forms.CharField(required=False)
   email = forms.EmailField()
   message = forms.CharField(max_length=1000)




  
 
class ReactorForm(forms.ModelForm):
    # unit = forms.ModelChoiceField(queryset = Unit.objects.all(),required=False)
    # reactor = None
    class Meta:
        model = Reactor
        fields = ('__all__')
        widgets = {
            
            'plant': autocomplete.ListSelect2(url='plant-autocomplete', forward=['client'],attrs={'data-placeholder': 'Select plant'}),
            'unit': autocomplete.ModelSelect2(url='unit-autocomplete', forward=['client', 'plant'], attrs={'data=placeholder': 'Select unit'})
        }


class UnitForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = "__all__"
        widgets = {
    
            'plant': autocomplete.ListSelect2(url='plant-autocomplete', forward=['client'],attrs={'data-placeholder': 'Select plant'}),
    }
        
