from django.contrib import admin
from .models import * 

# Register your models here.
admin.site.register(Utilisateur)
admin.site.register(Professeur)
admin.site.register(Eleve)
admin.site.register(UE)
admin.site.register(EC)
admin.site.register(Maquette)
admin.site.register(Time_Table)
admin.site.register(Professeur_Pedagogique)
admin.site.register(Chef_Departement)
admin.site.register(Cahier_De_Texte)
admin.site.register(Dispenser_Cours)
admin.site.register(Publication)
admin.site.register(Responsable)