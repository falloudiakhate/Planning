from django.shortcuts import render
<<<<<<< HEAD
from Accounts.models import *
from Accounts.forms import *
=======
from Accounts.forms import formInscription
from Accounts.forms import UserForm
>>>>>>> 7b94f387d8d3b155a1ba1c2f994b9287c78a0c7d

# Create your views here.

def PlanningHomePage(request):
    if request.method=="POST":
        post_data=request.POST or None
        form_utilisateur=formInscription(post_data)
        form_user=UserForm(post_data)
        if form_utilisateur.is_valid() and form_user.is_valid():
            user=form_user.save()
            utilisateur=form_utilisateur.save(commit=False)
            utilisateur.user=user
            utilisateur.save()
    form_utilisateur=formInscription()
    form_user=UserForm()
            
    return render(request,'Planning/index.html',locals())


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
    
<<<<<<< HEAD
      return render(request, 'Teachers/time_table.html', locals())
=======
      return render(request, "Teachers/time_table.html")
>>>>>>> 7b94f387d8d3b155a1ba1c2f994b9287c78a0c7d
