from django.shortcuts import render
from Accounts.models import *
from Accounts.forms import *

# Create your views here.

def PlanningHomePage(request):

      return render(request, "Planning/index.html")


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