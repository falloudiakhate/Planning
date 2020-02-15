from django.shortcuts import render
from Accounts.forms import formInscription
from Accounts.forms import UserForm

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
