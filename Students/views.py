from django.shortcuts import render, redirect
from Accounts.models import *
from Accounts.forms import *
from Students.views import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q


# Create your views here.


def Maquettes(request):
      user_profil=Utilisateur.objects.get(user=request.user)
      
      maquette = Maquette.objects.all().order_by('date').reverse()
      sum_maq = Maquette.objects.count()
      page = request.GET.get('page', 1)

      paginator = Paginator(maquette, 6)
      
      try:
            
            maquette = paginator.page(page)
      
      except PageNotAnInteger:
            maquette = paginator.page(1)
      except EmptyPage:
            maquette = paginator.page(paginator.num_pages)     
    
      return render(request, "Students/maquette.html", locals())


def ECS(request, id):
      user_profil=Utilisateur.objects.get(user=request.user)
      
      maquette = Maquette.objects.get(id=id)
      
      uc_stats = EC.objects.filter(ue__maquette__id=id) 
      
      ue_stats = EC.objects.filter(ue__id=id) 
      
      uc_count =  EC.objects.filter(ue__maquette__id=id).count()
      
     
      
      page = request.GET.get('page', 1)

      paginator = Paginator(uc_stats, 8)
      try:
            uc_stats = paginator.page(page)
      except PageNotAnInteger:
            uc_stats = paginator.page(1)
      except EmptyPage:
            uc_stats = paginator.page(paginator.num_pages)     
    
      return render(request, "Students/courses.html", locals())


def ListeStudent(request):
      user_profil=Utilisateur.objects.get(user=request.user)
      
      
      listeStudent = Utilisateur.objects.select_related("classe").all().filter(Q(fonction = "Eleve") | 
                                       Q(fonction = "Responsable"))
      
      total = listeStudent.count()
      
     
      
      page = request.GET.get('page', 1)

      paginator = Paginator(listeStudent, 15)
      try:
            listeStudent = paginator.page(page)
      except PageNotAnInteger:
            listeStudent = paginator.page(1)
      except EmptyPage:
            listeStudent = paginator.page(paginator.num_pages)     
    
      return render(request, "Students/listeEleve.html", locals())

      

def PlanningCoursesElements(request):
      user_profil=Utilisateur.objects.get(user=request.user)
    
      return render(request, "Students/elements.html")

def PlanningCoursesDetails(request, id):
      user_profil=Utilisateur.objects.get(user=request.user)
      
      ecs = EC.objects.get(id=id)
    
      return render(request, "Students/course-details.html", locals())



def AddMaquette(request):
      user_profil=Utilisateur.objects.get(user=request.user)
      
      classe = Classe.objects.all()
      return render(request, "Students/addmaquette.html", locals())

def AddUE(request):
      user_profil=Utilisateur.objects.get(user=request.user)
      
      maquette = Maquette.objects.all()
      return render(request, "Students/addue.html", locals())

def AddEC(request):
      user_profil=Utilisateur.objects.get(user=request.user)
      
      ue = UE.objects.all()
      return render(request, "Students/addEC.html", locals())


def AddCahierTexte(request):
      user_profil=Utilisateur.objects.get(user=request.user)
      
      classe = Classe.objects.all()
      ec = EC.objects.all()
      utilisateur = Utilisateur.objects.filter(Q(fonction = "Professeur") | 
                                        Q(fonction = "Responsable_pedagogique") |
                                         Q(fonction = "Chef_department"))
      
      if not request.user.utilisateur.fonction.endswith("Responsable"):

            if request.method=="POST":
                  
                  form = CahierTexteForm(request.POST)
      
                  
                  if form.is_valid():
                        form.save()
                        return redirect("ListeCahierTexte")
                  
                  form = CahierTexteForm()
                  return render(request, "Students/addCahierTexte.html", locals())
            
            form = CahierTexteForm()
            return render(request, "Students/addCahierTexte.html", locals())
      
      return redirect("Message")



def CahierDeTexte(request, id):
      user_profil=Utilisateur.objects.get(user=request.user)
      
      cahier = Cahier_De_Texte.objects.get(id=id)
      return render(request, "Students/cahierTexte.html", locals())

def ListeCahierTexte(request):
      user_profil=Utilisateur.objects.get(user=request.user)
      
      cahier = Cahier_De_Texte.objects.all().order_by('date').reverse()
      
      page = request.GET.get('page', 1)

      paginator = Paginator(cahier, 8)
      try:
            cahier = paginator.page(page)
      except PageNotAnInteger:
            cahier = paginator.page(1)
      except EmptyPage:
            cahier = paginator.page(paginator.num_pages)
            
      return render(request, "Students/ListecahierTexte.html", locals())


def Screen(request, id):
      user_profil=Utilisateur.objects.get(user=request.user)
      
      cahier = Cahier_De_Texte.objects.get(id=id)
      return render(request, "Students/screen.html", locals())


def ListeUpdateCahierTexte(request):
      user_profil=Utilisateur.objects.get(user=request.user)
      
      cahier = Cahier_De_Texte.objects.all().order_by('date').reverse()
      
      page = request.GET.get('page', 1)

      paginator = Paginator(cahier, 8)
      try:
            cahier = paginator.page(page)
      except PageNotAnInteger:
            cahier = paginator.page(1)
      except EmptyPage:
            cahier = paginator.page(paginator.num_pages)
            
      return render(request, "Students/ListeUpdateCahierTexte.html", locals())




def UpdateCahierTexte(request, id):
      user_profil=Utilisateur.objects.get(user=request.user)
      
      classe = Classe.objects.all()
      cahier_sel = Cahier_De_Texte.objects.get(id=id)
      ec = EC.objects.all()
      utilisateur = Utilisateur.objects.filter(Q(fonction = "Professeur") | 
                                        Q(fonction = "Responsable_pedagogique") |
                                         Q(fonction = "Chef_department"))
      
      if  request.user.utilisateur.fonction.endswith("Responsable"):

            if request.method=="POST":
                  
                  form = CahierTexteForm(request.POST, instance=cahier_sel)
      
                  
                  if form.is_valid():
                        form.save()
                        return redirect("ListeUpdateCahierTexte")
                  
                  form = CahierTexteForm(request.POST,instance=cahier_sel)
                  return render(request, "Students/UpdateCahierTexte.html", locals())
            
            form = CahierTexteForm(instance=cahier_sel)
            return render(request, "Students/UpdateCahierTexte.html", locals())
      
      return redirect("Message")


def DeleteCahierTexte(request, id):
      user_profil=Utilisateur.objects.get(user=request.user)
      
      classe = Classe.objects.all()
      cahier_sel = Cahier_De_Texte.objects.filter(id=id)
      ec = EC.objects.all()
      utilisateur = Utilisateur.objects.filter(Q(fonction = "Professeur") | 
                                        Q(fonction = "Responsable_pedagogique") |
                                         Q(fonction = "Chef_department"))
      
      if not request.user.utilisateur.fonction.endswith("Responsable"):

    
            cahier_sel.delete()
            return redirect("ListeUpdateCahierTexte")
      
      return redirect("Message")



def DisplayTimeTable(request):
      user_profil=Utilisateur.objects.get(user=request.user)
      
      
      # time = TimeTable.objects.filter(timetableliste__id=id)
      return render(request, "Teachers/DisplayTimeTable.html", locals())
      
      
def DisplayListeTimeTable(request, id):
      user_profil=Utilisateur.objects.get(user=request.user)
      
      emploi = TimeTableListe.objects.get(id=id)
      time = TimeTable.objects.filter(timetableliste__id=id)
      sumtime=time.count()
      return render(request, "Teachers/ListeTimeTable.html", locals())


def Print(request, id):
      user_profil=Utilisateur.objects.get(user=request.user)
      
      emploi = TimeTableListe.objects.get(id=id)
      time = TimeTable.objects.filter(timetableliste__id=id)      
      return render(request, "Students/print.html", locals())


def RemplirListeAbsence(request):
      user_profil=Utilisateur.objects.get(user=request.user)
      
      cours = EC.objects.all()
      # classes = Utilisateur.objects.filter(id=request.user.utilisateur.id)
      classes = Classe.objects.all()
      utilisateur = Utilisateur.objects.all()
      
      
      if  request.user.utilisateur.fonction.endswith("Responsable"):

            if request.method=="POST":
                  
                  form = AbsenceForm(request.POST)
      
                  
                  if form.is_valid():
                        form.save()
                        return redirect("DisplayListeAbsence")
                  
                  form = AbsenceForm()
                  return render(request, "Students/ListeAbsence.html", locals())
            
            form = AbsenceForm()
            return render(request, "Students/ListeAbsence.html", locals())
      
      return redirect("Message")
      
      
      
def DisplayListeAbsence(request):
      user_profil=Utilisateur.objects.get(user=request.user)
      
      absents = Absence.objects.all().order_by('date').reverse()
      
      page = request.GET.get('page', 1)

      paginator = Paginator(absents, 10)
      try:
            absents = paginator.page(page)
      except PageNotAnInteger:
            absents = paginator.page(1)
      except EmptyPage:
            absents = paginator.page(paginator.num_pages)
            
      return render(request, "Students/DisplayListeAbsence.html", locals())


def UpdateListeAbsence(request, id):
      
      user_profil=Utilisateur.objects.get(user=request.user)
      
      absent_sel = Absence.objects.get(id=id)
      
      cours = EC.objects.all()
      classes = Classe.objects.all()
      utilisateur = Utilisateur.objects.all()
      
      
      if  request.user.utilisateur.fonction.endswith("Responsable"):

            if request.method=="POST":
                  
                  form = AbsenceForm(request.POST, instance=absent_sel)
      
                  
                  if form.is_valid():
                        form.save()
                        return redirect("DisplayListeAbsence")
                  
                  form = AbsenceForm(instance=absent_sel)
                  return render(request, "Students/UpdateAbsence.html", locals())
            
            form = AbsenceForm(instance=absent_sel)
            return render(request, "Students/UpdateAbsence.html", locals())
      
      return redirect("Message")
      
      
      
def DeleteAbsence(request, id):
      user_profil=Utilisateur.objects.get(user=request.user)
      
      absent_sel = Absence.objects.get(id=id)
      
      cours = EC.objects.all()
      classes = Classe.objects.all()
      utilisateur = Utilisateur.objects.all()
      
    
      if  request.user.utilisateur.fonction.endswith("Responsable"):

    
            absent_sel.delete()
            return redirect("DisplayListeAbsence")
      
      return redirect("Message")
