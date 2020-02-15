from django.shortcuts import render

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
    
      return render(request, "Teachers/time_table.html")