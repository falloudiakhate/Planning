from django.forms import ModelForm
from Accounts.models import *
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

         
class  UserForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","first_name","last_name","email"]
        
    def __init__(self,*args,**kwargs):
            super(UserCreationForm,self).__init__(*args,**kwargs)
            self.fields['username'].widget.attrs['class']='form-control'
            self.fields['first_name'].widget.attrs['class']='form-control'
            self.fields['last_name'].widget.attrs['class']='form-control'
            self.fields['email'].widget.attrs['class']='form-control'
            self.fields['password1'].widget.attrs['class']='form-control' 
            self.fields['password2'].widget.attrs['class']='form-control' 
                       
            self.fields['username'].help_text=''
            self.fields['password1'].help_text=''
            self.fields['password2'].help_text=''
            
class formInscription(forms.ModelForm): 
    class Meta:
        model = Utilisateur
        fields = ["telephone","fonction", "avatar","classe"]     
          
    def __init__(self,*args,**kwargs):
            super(formInscription,self).__init__(*args,**kwargs)
            self.fields['telephone'].widget.attrs['class']='form-control'
            self.fields['fonction'].widget.attrs['class']='form-control'
            self.fields['avatar'].widget.attrs['class']='form-control'
            self.fields['classe'].widget.attrs['class']='form-control'


class TimeTableForm(ModelForm):
    class Meta:
       model = Time_Table
       fields = ['nom', 'classe', 'date', 'file']
       


class CahierTexteForm(ModelForm):
    class Meta:
       model = Cahier_De_Texte
       fields = ['classe', 'titre_EC', 'date', 'duree_EC', 'nom_professeur', 'contenu']
       
    
    