from django import forms
from tube.models import  User

from tube.models import Client
from tube.models import Login



class LoginForm(forms.Form):
    username = forms.CharField(max_length=63)
    password = forms.CharField(max_length=63, widget=forms.PasswordInput)

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields ='__all__'


class ClientForm(forms.ModelForm):
    class Meta():
        model= Client
        fields='__all__'


        


