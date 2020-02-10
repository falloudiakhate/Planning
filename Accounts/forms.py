from django import forms
from .models import Utilisateur
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):

  email = forms.EmailField()

  class Meta:

        model = Utilisateur
        fields = {"nom", "prenom", "pseudo", "telephone", "email", "avatar"}