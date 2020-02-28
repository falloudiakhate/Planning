from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Classe(models.Model):
    nom = models.CharField(max_length=50)
    annee = models.DateField(auto_now=False, auto_now_add=False)
    def __str__(self):
        return self.nom

class Utilisateur(models.Model):
    fonction=(
         ('Eleve','Eleve'),
         ('Professeur','Professeur'),
         ('Chef_department','Chef_department'),
         ('Responsable','Responsable'),
         ('Responsable_pedagogique','Responsable_pedagogique')
)
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    telephone = models.CharField( max_length=50)
    avatar = models.ImageField(upload_to="", height_field=None, width_field=None, max_length=None)
    fonction = models.CharField(max_length=50,choices=fonction)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)
    code=models.CharField(max_length=10,default='null')

class Publication(models.Model):
    date = models.DateTimeField( auto_now=False, auto_now_add=False)
    message = models.TextField()
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    
    
class Absence(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    classe = models.CharField(max_length=50)
    cours = models.CharField(max_length=50)
    debut = models.CharField(max_length=50)
    fin = models.CharField(max_length=50)
    date = models.DateTimeField( auto_now=False, auto_now_add=False, blank=True, null=True)


    
    
    

class Cahier_De_Texte(models.Model):
    classe = models.CharField(max_length=50)
    titre_EC = models.CharField(max_length=50)
    date = models.DateTimeField( auto_now=False, auto_now_add=False)
    duree_EC = models.CharField(max_length=50)
    nom_professeur = models.CharField(max_length=50, blank=True, null=True)
    contenu = models.TextField()
    
    

class Maquette(models.Model):
    nom = models.CharField( max_length=50, blank=True, null=True)
    date = models.DateField( auto_now=False, auto_now_add=False)
    description = models.TextField()

class UE(models.Model):
    nom = models.CharField(max_length=50)
    description = models.TextField()
    code = models.CharField( max_length=50)
    maquette = models.ForeignKey(Maquette, on_delete=models.CASCADE)

class EC(models.Model):
    nom = models.CharField(max_length=50)
    description = models.TextField()
    charge_horaire = models.CharField(max_length=50)
    coef = models.CharField(max_length=50)
    ue = models.ForeignKey(UE, on_delete=models.CASCADE)
    avatar = models.ImageField(blank=True, null=True, upload_to="", height_field=None, width_field=None, max_length=None)



class Dispenser_Cours(models.Model):
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    uc = models.ForeignKey(EC, on_delete=models.CASCADE)

class Time_Table(models.Model):
    nom = models.CharField(blank=True, null=True, max_length=50)
    date = models.DateTimeField( auto_now=False, auto_now_add=False)
    classe = models.CharField(blank=True, null=True, max_length=50)
    file = models.FileField(upload_to='', blank=True, null=True)
    
    
class TimeTableListe(models.Model):
    nom = models.CharField(blank=True, null=True, max_length=50)
    date = models.DateTimeField( auto_now=False, auto_now_add=False, blank=True, null=True)
    classe = models.CharField(blank=True, null=True, max_length=50)
    
class TimeTable(models.Model):
    ec =  models.CharField(blank=True, null=True, max_length=50)
    debut = models.TimeField( auto_now=False, auto_now_add=False, blank=True, null=True)
    fin = models.TimeField( auto_now=False, auto_now_add=False, blank=True, null=True)
    prof = models.CharField(blank=True, null=True, max_length=50)
    jour=models.CharField(blank=True, null=True, max_length=50)
    timetableliste = models.ForeignKey(TimeTableListe, on_delete=models.CASCADE,blank=True, null=True)
    
    

    
 
    

class Meta:
        ordering = ['created_on']
        def __unicode__(self):
            return self.title
