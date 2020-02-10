from django.db import models

# Create your models here.
from django.db import models

class Utilisateur(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    pseudo = models.CharField(max_length=50)
    telephone = models.CharField( max_length=50)
    avatar = models.ImageField(upload_to="", height_field=None, width_field=None, max_length=None)
    email = models.EmailField(max_length = 254)


class Professeur(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    pseudo = models.CharField(max_length=50)
    telephone = models.CharField(max_length=50)
    avatar = models.ImageField( upload_to="", width_field=None, max_length=None)
    email = models.EmailField(max_length = 254)
    num_professeur = models.IntegerField()
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)

class Chef_Departement(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    pseudo = models.CharField(max_length=50)
    telephone = models.CharField(max_length=50)
    avatar = models.ImageField( upload_to="", height_field=None, width_field=None, max_length=None)
    email = models.EmailField(max_length = 254)
    num_professeur = models.IntegerField()
    num_chef_departement = models.IntegerField()
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    Professeur = models.ForeignKey(Professeur, on_delete=models.CASCADE)


class Professeur_Pedagogique(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    pseudo = models.CharField(max_length=50)
    telephone = models.CharField(max_length=50)
    avatar = models.ImageField( upload_to="", height_field=None, width_field=None, max_length=None)
    email = models.EmailField(max_length = 254)
    num_professeur = models.IntegerField()
    num_professeur_pedagogique = models.IntegerField()
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    Professeur = models.ForeignKey(Professeur, on_delete=models.CASCADE)

class Time_Table(models.Model):
    date = models.DateTimeField( auto_now=False, auto_now_add=False)
    document = models.FileField( upload_to=None, max_length=100)
    professeur_pedagogique = models.ForeignKey(Professeur_Pedagogique, on_delete=models.CASCADE)

class Publication(models.Model):
    date = models.DateTimeField( auto_now=False, auto_now_add=False)
    message = models.TextField()
    professeur_pedagogique = models.ForeignKey(Professeur_Pedagogique, on_delete=models.CASCADE)

class Classe(models.Model):
    nom = models.CharField(max_length=50)
    annee = models.DateField(auto_now=False, auto_now_add=False)




class Eleve(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    pseudo = models.CharField(max_length=50)
    telephone = models.CharField(max_length=50)
    avatar = models.ImageField( upload_to="", height_field=None, width_field=None, max_length=None)
    email = models.EmailField(max_length = 254)
    num_eleve = models.IntegerField()
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)

class Responsable(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    pseudo = models.CharField(max_length=50)
    telephone = models.CharField(max_length=50)
    avatar = models.ImageField( upload_to="", height_field=None, width_field=None, max_length=None)
    email = models.EmailField(max_length = 254)
    num_eleve = models.IntegerField()
    eleve = models.ForeignKey(Eleve, on_delete=models.CASCADE)

class Cahier_De_Texte(models.Model):
    titre_EC = models.CharField(max_length=50)
    duree_EC = models.IntegerField()
    nom_professeur = models.IntegerField()
    contenu = models.TextField()
    date = models.DateTimeField( auto_now=False, auto_now_add=False)
    responsable = models.ForeignKey(Responsable, on_delete=models.CASCADE)

class Maquette(models.Model):
    nom = models.CharField(max_length=50)
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



class Dispenser_Cours(models.Model):
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)
    professeur= models.ForeignKey(Professeur, on_delete=models.CASCADE)
    uc = models.ForeignKey(EC, on_delete=models.CASCADE)

    

class Meta:
        ordering = ['created_on']
        def __unicode__(self):
            return self.title