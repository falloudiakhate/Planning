from django.shortcuts import render, redirect
from Accounts.models import *
from Accounts.forms import *
from Accounts.forms import formInscription
from Accounts.forms import UserForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

# Create your views here.

def PlanningHomePage(request):
    return render(request,'Planning/index.html',locals())

def Signup(request):
    
        if request.method=="POST":
            
            form_utilisateur=formInscription(request.POST, request.FILES)
            form_user=UserForm(request.POST)
            
            if form_utilisateur.is_valid() and form_user.is_valid():
                
                user=form_user.save()
                utilisateur=form_utilisateur.save(commit=False)
                utilisateur.user=user
                utilisateur.save()
                
                return redirect("PlanningTimeTable")
                
            form_utilisateur=formInscription()
            form_user=UserForm()
            return render(request,'Planning/signup.html',locals())
    
        return render(request,'Planning/signup.html',locals())
        form_utilisateur=formInscription()
        form_user=UserForm()
        
        
        
def Login(request):
    return render(request, "Planning/login.html")
        
        

def PlanningAboutus(request):
    
    return render(request, "Compte/index.html")

def PlanningBlog(request):
    
    return render(request, "Planning/blog.html")

def PlanningBlogDetails(request):
    
    return render(request, "Planning/single-blog.html")

def PlanningInfo(request):
    return render(request, "Compte/index.html")


def InfoProf(request):
    
    listeProf = Utilisateur.objects.filter(fonction = "Professeur")
    summ = Utilisateur.objects.filter(fonction = "Professeur").count()
     
      
    page = request.GET.get('page', 1)

    paginator = Paginator(listeProf, 8)
    try:
            listeProf = paginator.page(page)
    except PageNotAnInteger:
            listeProf = paginator.page(1)
    except EmptyPage:
            listeProf = paginator.page(paginator.num_pages)
    
    return render(request, "Teachers/prof.html", locals())


def InfoClasses(request):
    
    listeClasses = Classe.objects.all()
    sum = Classe.objects.all().count()
     
      
    page = request.GET.get('page', 1)

    paginator = Paginator(listeClasses, 8)
    try:
            listeProf = paginator.page(page)
    except PageNotAnInteger:
            listeProf = paginator.page(1)
    except EmptyPage:
            listeProf = paginator.page(paginator.num_pages)
    
    return render(request, "Planning/classes.html", locals())


def ListeEleve(request, id):
    
    liste = Utilisateur.objects.filter(Q(classe__id=id), Q(fonction = "Eleve") | 
                                       Q(fonction = "Responsable"))
    
    lister = Utilisateur.objects.filter(Q(classe__id=id), 
                                       Q(fonction = "Responsable"))
    
    listeped = Utilisateur.objects.filter(Q(classe__id=id), 
                                        Q(fonction = "Responsable_pedagogique"))
    
    listep = Utilisateur.objects.filter(Q(classe__id=id), Q(fonction = "Professeur") | 
                                        Q(fonction = "Responsable_pedagogique") |
                                         Q(fonction = "Chef_department"))
    classe = Classe.objects.get(id=id)
    sume = liste.count()
    sumee = listep.count()
    
    return render(request, "Students/eleve.html", locals())



def PlanningTimeTable(request):
      
      ecs = EC.objects.all()
      classes = Classe.objects.all()
      users = Utilisateur.objects.all()
      
      if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            form = Time_TableForm(request.POST)
        # check whether it's valid:
            if form.is_valid():
            # process the data in form.cleaned_data as required
                  form.save()
            # redirect to a new URL:
                  for i in [1, 2]:
                        if i < 2:
                              return render(request, 'Teachers/time_table.html', locals())
                        if i == 2:
                              return render(request, 'Planning/index.html', locals())
                        
                   
            

    # if a GET (or any other method) we'll create a blank form
            else:
                  form = Time_TableForm()
                  return render(request, 'Teachers/time_table.html', locals())
    
      return render(request, 'Teachers/time_table.html', locals())

