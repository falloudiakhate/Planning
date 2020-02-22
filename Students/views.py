from django.shortcuts import render
from Accounts.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q


# Create your views here.


def Maquettes(request):
      
      maquette = Maquette.objects.all() 
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
    
      return render(request, "Students/elements.html")

def PlanningCoursesDetails(request, id):
      
      ecs = EC.objects.get(id=id)
    
      return render(request, "Students/course-details.html", locals())



def AddMaquette(request):
      return render(request, "Students/addmaquette.html", locals())