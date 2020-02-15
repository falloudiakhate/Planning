from django import forms
from Accounts.models import Utilisateur  
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
Function=("eleve","professeur","responsable","responsable_pedagodique","chef_departement")
class  UserForm(UserCreationForm):
    class Meta:
        model=User
        fields=("username","first_name","last_name","email")
class formInscription(forms.ModelForm): 
    class Meta:
        model = Utilisateur
        fields = ("telephone","fonction")       
        widget={
           "fonction": forms.ChoiceField(choices=Function)
        }
       

