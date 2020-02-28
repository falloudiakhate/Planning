"""Planning URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Students import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [

    path('Courses/',views.Maquettes, name = "PlanningCourses" ),
    path('ListeStudent/',views.ListeStudent, name = "ListeStudent" ),
    path('ECS/<int:id>',views.ECS, name = "ECS" ),
    path('CoursesElements/',views.PlanningCoursesElements, name = "PlanningCoursesElements" ),
    path('CoursesDetails/<int:id>',views.PlanningCoursesDetails, name = "PlanningCoursesDetails" ),
    path('AddMaquette/',views.AddMaquette, name = "AddMaquette" ),
    path('AddUE/',views.AddUE, name = "AddUE" ),
    path('AddEC/',views.AddEC, name = "AddEC" ),
    path('AddCahierTexte/',views.AddCahierTexte, name = "AddCahierTexte" ),
    path('CahierDeTexte/<int:id>',views.CahierDeTexte, name = "CahierDeTexte" ),
    path('ListeCahierTexte/',views.ListeCahierTexte, name = "ListeCahierTexte" ),
    path('ListeUpdateCahierTexte/',views.ListeUpdateCahierTexte, name = "ListeUpdateCahierTexte" ),
    path('UpdateCahierTexte/<int:id>',views.UpdateCahierTexte, name = "UpdateCahierTexte" ),
    path('Screen/<int:id>',views.Screen, name = "Screen" ),
    path('Print/<int:id>',views.Print, name = "Print" ),
    path('DeleteCahierTexte/<int:id>',views.DeleteCahierTexte, name = "DeleteCahierTexte" ),
    path('DisplayTimeTable<int:id>',views.DisplayTimeTable, name = "DisplayTimeTable" ),
    path('DisplayListeTimeTable/<int:id>',views.DisplayListeTimeTable, name = "DisplayListeTimeTable" ),
    path('DisplayListeAbsence/',views.DisplayListeAbsence, name = "DisplayListeAbsence" ),
    path('RemplirListeAbsence/',views.RemplirListeAbsence, name = "RemplirListeAbsence" ),
    path('UpdateListeAbsence/<int:id>',views.UpdateListeAbsence, name = "UpdateListeAbsence" ),
    path('DeleteAbsence/<int:id>',views.DeleteAbsence, name = "DeleteAbsence" ),
    
    
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
