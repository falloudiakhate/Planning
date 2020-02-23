from django.shortcuts import render, redirect, HttpResponse
from Accounts.forms import *
from Accounts.forms import formInscription
from Accounts.forms import *
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
    
    listeProf = Utilisateur.objects.filter(Q(fonction = "Professeur") | 
                                        Q(fonction = "Responsable_pedagogique") |
                                         Q(fonction = "Chef_department"))
    summ =listeProf.count()
     
      
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



def TimeTable(request):
    
    tab = Time_Table.objects.all()
    sumtab = tab.count()
    
    page = request.GET.get('page', 1)

    paginator = Paginator(tab, 8)
    try:
            tab = paginator.page(page)
    except PageNotAnInteger:
            tab = paginator.page(1)
    except EmptyPage:
            tab = paginator.page(paginator.num_pages)
    return render(request, "Teachers/time_table.html", locals())

def AddTimeTable(request):
    classe = Classe.objects.all()
    
    if request.method=="POST":
            
            form = TimeTableForm(request.POST, request.FILES)
    
            
            if form.is_valid():
                form.save()
                return redirect("TimeTable")
            
            form = TimeTableForm()
            return render(request, "Students/addTimeTable.html", locals())
        
    form = TimeTableForm()
    return render(request, "Students/addTimeTable.html", locals())
            
    

    


