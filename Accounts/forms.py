from django.forms import ModelForm
from Accounts.models import *
class Time_TableForm(ModelForm):
    class Meta:
         model = Time_Table
         fields = ['moment', 'heure_debut', 'heure_fin', 'date','classe', 'ec', 'utilisateur']