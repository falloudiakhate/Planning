from django.forms import ModelForm
from Accounts.models import *
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

         
class  UserForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","first_name","last_name","email"]
class formInscription(forms.ModelForm): 
    class Meta:
        model = Utilisateur
        fields = ["telephone","fonction", "avatar"]       


class TimeTableForm(ModelForm):
    class Meta:
       model = Time_Table
       fields = ['nom', 'classe', 'date', 'file']
       


