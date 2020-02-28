from django.shortcuts import render, redirect, HttpResponse
from Accounts.forms import *
from Accounts.forms import formInscription
from Accounts.forms import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Max
from django.contrib.auth import login, authenticate,logout



# Create your views here.

def PlanningHomePage(request):
    user_profil=Utilisateur.objects.get(user=request.user)
    return render(request,'Planning/index.html',locals())

def Signup(request):
    
    if request.method=="POST":
        form=UserForm(request.POST)
        # code=request.POST['code']
        if form.is_valid:
            form.save()
            user=User.objects.get(username=request.POST['username'])
            id=user.id
            return redirect('Profil',id)
        
                
    form=UserForm()          
    return render(request,'Planning/signup.html',locals())
       
              
def EditProfil(request,id):
    if request.method=='POST':
        form=formInscription(request.POST,request.FILES)
        if form.is_valid():
            newform=form.save(commit=False)
            newform.user= User.objects.get(id=id)
            newform.save()
            return redirect('Login')

    form=formInscription()
    return render(request, "Planning/profil.html",locals())
        
def Login(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('PlanningInfo')
    form=LoginForm()
    return render(request,"Planning/login.html",locals()) 
def PasswordModif(request):
    if request.method=='POST':
        form=ModifForm(request.POST)
        if form.is_valid():
            password=form.cleaned_data['password']
            email=form.cleaned_data['email']
            user=User.objects.get(email=email)
            user.set_password(password) 
            user.save()  
            messages.success(request,"votre mot de passe a bien été modifié")   
            return redirect('Login')    
        
    form=ModifForm()
    return render(request,"Planning/password.html",locals())  
def Logout(request):
    logout (request)
    return redirect('PlanningHomePage')

def PlanningAboutus(request):
    
    return render(request, "Planning/about-us.html")

def PlanningBlog(request):
    
    return render(request, "Planning/blog.html")

def PlanningBlogDetails(request):
    
    return render(request, "Planning/single-blog.html")

@login_required()
def PlanningInfo(request):
    user_profil=Utilisateur.objects.get(user=request.user)
    return render(request, "Compte/index.html",locals())


def InfoProf(request):
    user_profil=Utilisateur.objects.get(user=request.user)
    
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
    user_profil=Utilisateur.objects.get(user=request.user)
    
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
    user_profil=Utilisateur.objects.get(user=request.user)
    
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
    user_profil=Utilisateur.objects.get(user=request.user)
    
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



            
    
def Message(request):
    user_profil=Utilisateur.objects.get(user=request.user)
    return render(request, "Students/message.html", locals())

def AddTimeTable(request):
    user_profil=Utilisateur.objects.get(user=request.user)
    classe = Classe.objects.all()
    
    if  request.user.utilisateur.fonction.endswith("Eleve"):
    
        if request.method=="POST":
                
                form = TimeTableForm(request.POST, request.FILES)
        
                
                if form.is_valid():
                    form.save()
                    return redirect("TimeTable")
                
                form = TimeTableForm(request.FILES)
                return render(request, "Students/addTimeTable.html", locals())
            
        form = TimeTableForm(request.FILES)
        return render(request, "Students/addTimeTable.html", locals())
    
    return redirect("Message")
            
    
def Message(request):
    user_profil=Utilisateur.objects.get(user=request.user)
    return render(request, "Students/message.html", locals())

    

def ListeUpdateTimeTable(request):
    user_profil=Utilisateur.objects.get(user=request.user)
    
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
    return render(request, "Students/ListeTimeTable.html", locals())



def UpdateTimeTable(request, id):
    user_profil=Utilisateur.objects.get(user=request.user)
    classe = Classe.objects.all()
    time_sel = Time_Table.objects.get(id=id)
    
    if not request.user.utilisateur.fonction.endswith("Eleve"):
    
        if request.method=="POST":
                
                form = TimeTableForm(request.POST, request.FILES, instance=time_sel)
        
                
                if form.is_valid():
                    form.save()
                    return redirect("TimeTable")
                
                form = TimeTableForm()
                return render(request, "Students/updateTimeTable.html", locals())
            
        form = TimeTableForm(request.POST, request.FILES, instance=time_sel)
        return render(request, "Students/updateTimeTable.html", locals())
    
    return redirect("Message")


def DeleteTimeTable(request, id):
    user_profil=Utilisateur.objects.get(user=request.user)
    classe = Classe.objects.all()
    time_sel = Time_Table.objects.filter(id=id)
    
    if not request.user.utilisateur.fonction.endswith("Eleve"):
    
                time_sel.delete()
                return redirect("ListeUpdateTimeTable")
    
    return redirect("Message")



def ListeUpdateMaquette(request):
      user_profil=Utilisateur.objects.get(user=request.user)
      
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
    
      return render(request, "Students/ListeUpdateMaquette.html", locals())
  
  
  
# <---------------------------------------------------------------------------------->


def ListeTimeTable(request):
    user_profil=Utilisateur.objects.get(user=request.user)
    
    classe = Classe.objects.all()
    
    ec = EC.objects.all()
    
    utilisateur = Utilisateur.objects.filter(Q(fonction = "Professeur") | 
                                        Q(fonction = "Responsable_pedagogique") |
                                         Q(fonction = "Chef_department"))
    
    if  request.user.utilisateur.fonction.endswith("Eleve"):

        
                if request.method=="POST":
                        
                        form = ListeTimeTableForm(request.POST)
                
                        
                        if form.is_valid():
                            form.save()
                            return redirect("AddTimeTableBis")
                        
                        form = ListeTimeTableForm()
                        return render(request, "Teachers/TimeTable0.html", locals())
                    
                form = ListeTimeTableForm()
                return render(request, "Teachers/TimeTable0.html", locals())
    return redirect("Message")


def RemplirTimeTable(request):
    user_profil=Utilisateur.objects.get(user=request.user)
    # Liste = TimeTableListe.objects.all().reverse()
    Liste = TimeTableListe.objects.all().order_by('date')
    sumtime=Liste.count()
  
    return render(request, "Teachers/RemplirTimeTable.html", locals())
    


 
def AddTimeTableBis(request):
    user_profil=Utilisateur.objects.get(user=request.user)
    

    
    timetableliste = TimeTableListe.objects.filter().aggregate(max_id=Max('pk'))
    v = int(timetableliste.get("max_id"))

    
    
    classe = Classe.objects.all()
    
    ec = EC.objects.all()
    
    utilisateur = Utilisateur.objects.filter(Q(fonction = "Professeur") | 
                                        Q(fonction = "Responsable_pedagogique") |
                                         Q(fonction = "Chef_department"))
    
    if  request.user.utilisateur.fonction.endswith("Eleve"):

        
                if request.method=="POST":
                        
                        form = TimeTableFormBis(request.POST)
                
                        
                        if form.is_valid():
                            form.save()
                            return redirect("AddTimeTableBis1")
                        
                        form = TimeTableFormBis()
                        return render(request, "Teachers/TimeTable.html", locals())
                    
                form = TimeTableFormBis()
                return render(request, "Teachers/TimeTable.html", locals())
    return redirect("Message")

# <------------------------------------------------------------------------------------------>
# <---------------------------------------------------------------------------------->
 
def AddTimeTableBis1(request):
    user_profil=Utilisateur.objects.get(user=request.user)
    
    classe = Classe.objects.all()
    
    timetableliste = TimeTableListe.objects.filter().aggregate(max_id=Max('pk'))
    v = int(timetableliste.get("max_id"))

    
    ec = EC.objects.all()
    
    utilisateur = Utilisateur.objects.filter(Q(fonction = "Professeur") | 
                                        Q(fonction = "Responsable_pedagogique") |
                                         Q(fonction = "Chef_department"))
    
    if  request.user.utilisateur.fonction.endswith("Eleve"):

        
                if request.method=="POST":
                        
                        form = TimeTableFormBis(request.POST)
                
                        
                        if form.is_valid():
                            form.save()
                            return redirect("AddTimeTableBis2")
                        
                        form = TimeTableFormBis()
                        return render(request, "Teachers/TimeTable1.html", locals())
                    
                form = TimeTableFormBis()
                return render(request, "Teachers/TimeTable1.html", locals())
    return redirect("Message")

# <------------------------------------------------------------------------------------------>


# <---------------------------------------------------------------------------------->
 
def AddTimeTableBis2(request):
    user_profil=Utilisateur.objects.get(user=request.user)
    
    timetableliste = TimeTableListe.objects.filter().aggregate(max_id=Max('pk'))
    v = int(timetableliste.get("max_id"))

    
    classe = Classe.objects.all()
    
    ec = EC.objects.all()
    
    utilisateur = Utilisateur.objects.filter(Q(fonction = "Professeur") | 
                                        Q(fonction = "Responsable_pedagogique") |
                                         Q(fonction = "Chef_department"))
    
    if  request.user.utilisateur.fonction.endswith("Eleve"):

        
                if request.method=="POST":
                        
                        form = TimeTableFormBis(request.POST)
                
                        
                        if form.is_valid():
                            form.save()
                            return redirect("AddTimeTableBis3")
                        
                        form = TimeTableFormBis()
                        return render(request, "Teachers/TimeTable2.html", locals())
                    
                form = TimeTableFormBis()
                return render(request, "Teachers/TimeTable2.html", locals())
    return redirect("Message")

# <------------------------------------------------------------------------------------------>

# <---------------------------------------------------------------------------------->
 
def AddTimeTableBis3(request):
    user_profil=Utilisateur.objects.get(user=request.user)
    
    classe = Classe.objects.all()
    timetableliste = TimeTableListe.objects.filter().aggregate(max_id=Max('pk'))
    v = int(timetableliste.get("max_id"))

    
    ec = EC.objects.all()
    
    utilisateur = Utilisateur.objects.filter(Q(fonction = "Professeur") | 
                                        Q(fonction = "Responsable_pedagogique") |
                                         Q(fonction = "Chef_department"))
    
    if  request.user.utilisateur.fonction.endswith("Eleve"):

        
                if request.method=="POST":
                        
                        form = TimeTableFormBis(request.POST)
                
                        
                        if form.is_valid():
                            form.save()
                            return redirect("AddTimeTableBis4")
                        
                        form = TimeTableFormBis()
                        return render(request, "Teachers/TimeTable3.html", locals())
                    
                form = TimeTableFormBis()
                return render(request, "Teachers/TimeTable3.html", locals())
    return redirect("Message")

# <------------------------------------------------------------------------------------------>

# <---------------------------------------------------------------------------------->
 
def AddTimeTableBis4(request):
    user_profil=Utilisateur.objects.get(user=request.user)
    
    timetableliste = TimeTableListe.objects.filter().aggregate(max_id=Max('pk'))
    v = int(timetableliste.get("max_id"))

    
    classe = Classe.objects.all()
    
    ec = EC.objects.all()
    
    utilisateur = Utilisateur.objects.filter(Q(fonction = "Professeur") | 
                                        Q(fonction = "Responsable_pedagogique") |
                                         Q(fonction = "Chef_department"))
    
    if  request.user.utilisateur.fonction.endswith("Eleve"):

        
                if request.method=="POST":
                        
                        form = TimeTableFormBis(request.POST)
                
                        
                        if form.is_valid():
                            form.save()
                            return redirect("AddTimeTableBis5")
                        
                        form = TimeTableFormBis()
                        return render(request, "Teachers/TimeTable4.html", locals())
                    
                form = TimeTableFormBis()
                return render(request, "Teachers/TimeTable4.html", locals())
    return redirect("Message")

# <------------------------------------------------------------------------------------------>

# <---------------------------------------------------------------------------------->
 
def AddTimeTableBis5(request):
    user_profil=Utilisateur.objects.get(user=request.user)
    
    timetableliste = TimeTableListe.objects.filter().aggregate(max_id=Max('pk'))
    v = int(timetableliste.get("max_id"))

    
    classe = Classe.objects.all()
    
    ec = EC.objects.all()
    
    utilisateur = Utilisateur.objects.filter(Q(fonction = "Professeur") | 
                                        Q(fonction = "Responsable_pedagogique") |
                                         Q(fonction = "Chef_department"))
    
    if  request.user.utilisateur.fonction.endswith("Eleve"):

        
                if request.method=="POST":
                        
                        form = TimeTableFormBis(request.POST)
                
                        
                        if form.is_valid():
                            form.save()
                            return redirect("AddTimeTableBis6")
                        
                        form = TimeTableFormBis()
                        return render(request, "Teachers/TimeTable5.html", locals())
                    
                form = TimeTableFormBis()
                return render(request, "Teachers/TimeTable5.html", locals())
    return redirect("Message")

# <------------------------------------------------------------------------------------------>

# <---------------------------------------------------------------------------------->
 
def AddTimeTableBis6(request):
    user_profil=Utilisateur.objects.get(user=request.user)
    
    timetableliste = TimeTableListe.objects.filter().aggregate(max_id=Max('pk'))
    v = int(timetableliste.get("max_id"))

    
    classe = Classe.objects.all()
    
    ec = EC.objects.all()
    
    utilisateur = Utilisateur.objects.filter(Q(fonction = "Professeur") | 
                                        Q(fonction = "Responsable_pedagogique") |
                                         Q(fonction = "Chef_department"))
    
    if  request.user.utilisateur.fonction.endswith("Eleve"):

        
                if request.method=="POST":
                        
                        form = TimeTableFormBis(request.POST)
                
                        
                        if form.is_valid():
                            form.save()
                            return redirect("AddTimeTableBis7")
                        
                        form = TimeTableFormBis()
                        return render(request, "Teachers/TimeTable6.html", locals())
                    
                form = TimeTableFormBis()
                return render(request, "Teachers/TimeTable6.html", locals())
    return redirect("Message")

# <------------------------------------------------------------------------------------------>



# <---------------------------------------------------------------------------------->
 
def AddTimeTableBis7(request):
    user_profil=Utilisateur.objects.get(user=request.user)
    
    timetableliste = TimeTableListe.objects.filter().aggregate(max_id=Max('pk'))
    v = int(timetableliste.get("max_id"))

    
    classe = Classe.objects.all()
    
    ec = EC.objects.all()
    
    utilisateur = Utilisateur.objects.filter(Q(fonction = "Professeur") | 
                                        Q(fonction = "Responsable_pedagogique") |
                                         Q(fonction = "Chef_department"))
    
    if  request.user.utilisateur.fonction.endswith("Eleve"):

        
                if request.method=="POST":
                        
                        form = TimeTableFormBis(request.POST)
                
                        
                        if form.is_valid():
                            form.save()
                            return redirect("AddTimeTableBis8")
                        
                        form = TimeTableFormBis()
                        return render(request, "Teachers/TimeTable7.html", locals())
                    
                form = TimeTableFormBis()
                return render(request, "Teachers/TimeTable7.html", locals())
    return redirect("Message")

# <------------------------------------------------------------------------------------------>

# <---------------------------------------------------------------------------------->
 
def AddTimeTableBis8(request):
    user_profil=Utilisateur.objects.get(user=request.user)
    
    timetableliste = TimeTableListe.objects.filter().aggregate(max_id=Max('pk'))
    v = int(timetableliste.get("max_id"))

    
    classe = Classe.objects.all()
    
    ec = EC.objects.all()
    
    utilisateur = Utilisateur.objects.filter(Q(fonction = "Professeur") | 
                                        Q(fonction = "Responsable_pedagogique") |
                                         Q(fonction = "Chef_department"))
    
    if  request.user.utilisateur.fonction.endswith("Eleve"):

        
                if request.method=="POST":
                        
                        form = TimeTableFormBis(request.POST)
                
                        
                        if form.is_valid():
                            form.save()
                            return redirect("AddTimeTableBis9")
                        
                        form = TimeTableFormBis()
                        return render(request, "Teachers/TimeTable8.html", locals())
                    
                form = TimeTableFormBis()
                return render(request, "Teachers/TimeTable8.html", locals())
    return redirect("Message")

# <------------------------------------------------------------------------------------------>

# <---------------------------------------------------------------------------------->
 
def AddTimeTableBis9(request):
    user_profil=Utilisateur.objects.get(user=request.user)
    
    
    timetableliste = TimeTableListe.objects.filter().aggregate(max_id=Max('pk'))
    v = int(timetableliste.get("max_id"))

    
    classe = Classe.objects.all()
    
    ec = EC.objects.all()
    
    utilisateur = Utilisateur.objects.filter(Q(fonction = "Professeur") | 
                                        Q(fonction = "Responsable_pedagogique") |
                                         Q(fonction = "Chef_department"))
    
    if  request.user.utilisateur.fonction.endswith("Eleve"):

        
                if request.method=="POST":
                        
                        form = TimeTableFormBis(request.POST)
                
                        
                        if form.is_valid():
                            form.save()
                            return redirect("AddTimeTableBis10")
                        
                        form = TimeTableFormBis()
                        return render(request, "Teachers/TimeTable9.html", locals())
                    
                form = TimeTableFormBis()
                return render(request, "Teachers/TimeTable9.html", locals())
    return redirect("Message")

# <------------------------------------------------------------------------------------------>

# <---------------------------------------------------------------------------------->
 


# <------------------------------------------------------------------------------------------>


# <------------------------------------------------------------------------------------------>
            
    
def Message(request):
    user_profil=Utilisateur.objects.get(user=request.user)
    return render(request, "Students/message.html", locals())




def AddTimeTableBis10(request):
    user_profil=Utilisateur.objects.get(user=request.user)
    
    timetableliste = TimeTableListe.objects.filter().aggregate(max_id=Max('pk'))
    v = int(timetableliste.get("max_id"))

    
    classe = Classe.objects.all()
    
    ec = EC.objects.all()
    
    utilisateur = Utilisateur.objects.filter(Q(fonction = "Professeur") | 
                                        Q(fonction = "Responsable_pedagogique") |
                                         Q(fonction = "Chef_department"))
    
    if  request.user.utilisateur.fonction.endswith("Eleve"):

        
                if request.method=="POST":
                        
                        form = TimeTableFormBis(request.POST)
                
                        
                        if form.is_valid():
                            form.save()
                            return redirect("RemplirTimeTable")
                        
                        form = TimeTableFormBis()
                        return render(request, "Teachers/TimeTable10.html", locals())
                    
                form = TimeTableFormBis()
                return render(request, "Teachers/TimeTable10.html", locals())
    return redirect("Message")