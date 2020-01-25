from django.shortcuts import render

# Create your views here.

def PlanningHomePage(request):

      return render(request, "Planning/index.html")
