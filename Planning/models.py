from django.db import models

class Utilisateur(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    pseudo = models.CharField(max_length=50)
    telephone = models.IntegerField()
    avatar = models.ImageField(_(""), upload_to=None, height_field=None, width_field=None, max_length=None)
    email = models.EmailField(max_length = 254)


class Professeur(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    pseudo = models.CharField(max_length=50)
    telephone = models.IntegerField()
    avatar = models.ImageField(_(""), upload_to=None, height_field=None, width_field=None, max_length=None)
    email = models.EmailField(max_length = 254)
    num_professeur = models.IntegerField()
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)

class Chef_Departement(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    pseudo = models.CharField(max_length=50)
    telephone = models.IntegerField()
    avatar = models.ImageField(_(""), upload_to=None, height_field=None, width_field=None, max_length=None)
    email = models.EmailField(max_length = 254)
    num_professeur = models.IntegerField()
    num_chef_departement = models.IntegerField()
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    Professeur = models.ForeignKey(Professeur, on_delete=models.CASCADE)


class Professeur_Pedagogique(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    pseudo = models.CharField(max_length=50)
    telephone = models.IntegerField()
    avatar = models.ImageField(_(""), upload_to=None, height_field=None, width_field=None, max_length=None)
    email = models.EmailField(max_length = 254)
    num_professeur = models.IntegerField()
    num_professeur_pedagogique = models.IntegerField()
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    Professeur = models.ForeignKey(Professeur, on_delete=models.CASCADE)

class Time_Table(models.Model):
    date = models.DateTimeField(_(""), auto_now=False, auto_now_add=False)
    document = models.FileField(_(""), upload_to=None, max_length=100)
    professeur_pedagogique = models.ForeignKey(Professeur_Pedagogique, on_delete=models.CASCADE)

class Publication(models.Model):
    date = models.DateTimeField(_(""), auto_now=False, auto_now_add=False)
    message = models.TextField()
    professeur_pedagogique = models.ForeignKey(Professeur_Pedagogique, on_delete=models.CASCADE)

class Classe(models.Model):

    def year_choices():
    return [(r,r) for r in range(2012, datetime.date.today().year+1)]

    def current_year():
    return datetime.date.today().year

    year = models.IntegerField(_('year'), choices=year_choices, default=current_year)
    professeur = models.ForeignKey(professeur), on_delete=models.CASCADE)




class Eleve(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    pseudo = models.CharField(max_length=50)
    telephone = models.IntegerField()
    avatar = models.ImageField(_(""), upload_to=None, height_field=None, width_field=None, max_length=None)
    email = models.EmailField(max_length = 254)
    num_eleve = models.IntegerField()
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)

class Responsable(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    pseudo = models.CharField(max_length=50)
    telephone = models.IntegerField()
    avatar = models.ImageField(_(""), upload_to=None, height_field=None, width_field=None, max_length=None)
    email = models.EmailField(max_length = 254)
    num_eleve = models.IntegerField()
    eleve = models.ForeignKey(Eleve, on_delete=models.CASCADE)

class Cahier_De_Texte(models.Model):
    titre_EC = models.CharField(max_length=50)
    duree_EC = models.Integer(max_length=50)
    nom_professeur = models.Integer(max_length=50)
    contenu = models.TextField()
    date = models.DateTimeField(_(""), auto_now=False, auto_now_add=False)
    responsable = models.ForeignKey(Responsable, on_delete=models.CASCADE)

class Maquette(models.Model):
    nom = models.CharField(max_length=50)
    date = models.DateField(_(""), auto_now=False, auto_now_add=False)

class UE(models.Model):
    nom = models.CharField(max_length=50)
    description = models.TextField()
    code = models.CharField(_(""), max_length=50)
    maquette = models.ForeignKey(Maquette, on_delete=models.CASCADE)

class EC(models.Model):
    nom = models.CharField(max_length=50)
    description = models.TextField()
    charge_horaire = models.IntegerField()
    coef = models.IntegerField()
    ue = models.ForeignKey(UE, on_delete=models.CASCADE)



class Dispenser_Cours(models.Model):
    cours = models.ForeignKey(Classe, Professeur, EC, Eleve on_delete=models.CASCADE)
    

    