from django.db import models
from Accounts.forms import Function
from django.db import models
from django.contrib.auth.models import User


class Utilisateur(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    telephone = models.CharField( max_length=50)
<<<<<<< HEAD
    #avatar = models.ImageField(upload_to="", height_field=None, width_field=None, max_length=None)
    fonction = models.CharField(max_length=50)
=======
    avatar = models.ImageField(upload_to="", height_field=None, width_field=None, max_length=None)
    fonction = models.CharField(max_length=50,choices=Function)

class Time_Table(models.Model):
    date = models.DateTimeField( auto_now=False, auto_now_add=False)
    document = models.FileField( upload_to=None, max_length=100)
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
>>>>>>> 7b94f387d8d3b155a1ba1c2f994b9287c78a0c7d

class Publication(models.Model):
    date = models.DateTimeField( auto_now=False, auto_now_add=False)
    message = models.TextField()
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)

class Classe(models.Model):
    nom = models.CharField(max_length=50)
    annee = models.DateField(auto_now=False, auto_now_add=False)
    

class Cahier_De_Texte(models.Model):
    titre_EC = models.CharField(max_length=50)
    duree_EC = models.IntegerField()
    nom_professeur = models.IntegerField()
    contenu = models.TextField()
    date = models.DateTimeField( auto_now=False, auto_now_add=False)
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)

class Maquette(models.Model):
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateField( auto_now=False, auto_now_add=False)
    description = models.TextField()

class UE(models.Model):
    nom = models.CharField(max_length=50)
    description = models.TextField()
    code = models.CharField( max_length=50)
    avatar = models.ImageField(blank=True, null=True, upload_to="", height_field=None, width_field=None, max_length=None)
    maquette = models.ForeignKey(Maquette, on_delete=models.CASCADE)

class EC(models.Model):
    nom = models.CharField(max_length=50)
    description = models.TextField()
    charge_horaire = models.IntegerField()
    coef = models.IntegerField()
    ue = models.ForeignKey(UE, on_delete=models.CASCADE)
    avatar = models.ImageField(blank=True, null=True, upload_to="", height_field=None, width_field=None, max_length=None)



class Dispenser_Cours(models.Model):
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    uc = models.ForeignKey(EC, on_delete=models.CASCADE)

class Time_Table(models.Model):
    moment = (
        ('Lundi Matin', 'Lundi Matin'),
        ('Lundi Soir', 'Lundi Soir'),
        ('Mardi Matin', 'Mardi Matin'),
        ('Mardi Soir', 'Mardi Soir'),
        ('Mercredi Matin', 'Mercredi Matin'),
        ('Jeudi Matin', 'Jeudi Matin'),
        ('Vendredi Matin', 'Vendredi Matin'),
        ('Samedi Matin', 'Samedi Matin'),
        ('Mercredi Soir', 'Mercredi Soir'),
        ('Jeudi Soir', 'Jeudi Soir'),
        ('Vendredi Soir', 'Vendredi Soir'),
        ('Samedi Soir', 'Samedi Soir'),
    )
    moment = models.CharField(max_length=50, choices=moment, blank=True, null=True)
    heure_debut = models.TimeField(auto_now=False, auto_now_add=False)
    heure_fin = models.TimeField(auto_now=False, auto_now_add=False)
    date = models.DateTimeField( auto_now=False, auto_now_add=False)
    classe = models.CharField(blank=True, null=True, max_length=50)
    ec = models.CharField(blank=True, null=True, max_length=50)
    utilisateur = models.CharField(blank=True, null=True, max_length=50)
 
    

class Meta:
        ordering = ['created_on']
        def __unicode__(self):
            return self.title
