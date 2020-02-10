from django.shortcuts import render
from Accounts.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


def Maquettes(request):
      
      # maquette = Maquette.objects.all()
      # uc_stats = EC.objects.all()  
      
      # page = request.GET.get('page', 1)

      # paginator = Paginator(uc_stats, 4)
      # try:
      #       uc_stats = paginator.page(page)
      # except PageNotAnInteger:
      #       uc_stats = paginator.page(1)
      # except EmptyPage:
      #       uc_stats = paginator.page(paginator.num_pages)     
    
      return render(request, "Students/maquette.html", locals())

def PlanningCoursesElements(request):
    
      return render(request, "Students/elements.html")

def PlanningCoursesDetails(request):
    
      return render(request, "Students/course-details.html")