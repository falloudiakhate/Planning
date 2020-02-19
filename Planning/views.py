from django.shortcuts import render, redirect
from Accounts.models import *
from Accounts.forms import *
from Accounts.forms import formInscription
from Accounts.forms import UserForm

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
    
    return render(request, "Planning/about-us.html")

def PlanningBlog(request):
    
    return render(request, "Planning/blog.html")

def PlanningBlogDetails(request):
    
    return render(request, "Planning/single-blog.html")

def PlanningInfo(request):
    return render(request, "Planning/info.html")



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

