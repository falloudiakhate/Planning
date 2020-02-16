from django import forms
from Accounts.models import Utilisateur
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
Function=(
         (1,'eleve'),
         (2,'professeur'),
         (3,'chef_department'),
         (4,'responsable'),
         (5,'responsable_pedagogique')
)
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
       

