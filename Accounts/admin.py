from django.contrib import admin
from .models import * 

# Register your models here.
admin.site.register(Utilisateur)
admin.site.register(Classe)
admin.site.register(UE)
admin.site.register(EC)
admin.site.register(Maquette)
admin.site.register(Time_Table)
admin.site.register(TimeTable)
admin.site.register(TimeTableListe)
admin.site.register(Cahier_De_Texte)
admin.site.register(Dispenser_Cours)
admin.site.register(Publication)