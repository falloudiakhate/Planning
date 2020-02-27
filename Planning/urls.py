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
from django.urls import path, include
from Planning import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    
    path('admin/', admin.site.urls),
    
    path('Students/', include('Students.urls')),
    path('Planning/',views.PlanningHomePage, name = "PlanningHomePage" ),
    path('CoursesAboutus/',views.PlanningAboutus, name = "PlanningAboutus" ),
    path('Blog/',views.PlanningBlog, name = "PlanningBlog" ),
    path('BlogDetails/',views.PlanningBlogDetails, name = "PlanningBlogDetails" ),
    path('Account/',views.PlanningInfo, name = "PlanningInfo" ),
    path('TimeTable/',views.TimeTable, name = "TimeTable" ),
    path('Signup/',views.Signup, name = "Signup" ),
    path('Login/',views.Login, name = "Login" ),
    path('InfoProf/',views.InfoProf, name = "InfoProf" ),
    path('InfoClasses/',views.InfoClasses, name = "InfoClasses" ),
    path('ListeEleve/<int:id>',views.ListeEleve, name = "ListeEleve" ),
    path('AddTimeTable/',views.AddTimeTable, name = "AddTimeTable" ),
    path('AddTimeTableBis/',views.AddTimeTableBis, name = "AddTimeTableBis" ),
    path('ListeUpdateTimeTable/',views.ListeUpdateTimeTable, name = "ListeUpdateTimeTable" ),
    path('ListeUpdateMaquette/',views.ListeUpdateMaquette, name = "ListeUpdateMaquette" ),
    path('UpdateTimeTable/<int:id>',views.UpdateTimeTable, name = "UpdateTimeTable" ),
    path('DeleteTimeTable/<int:id>',views.DeleteTimeTable, name = "DeleteTimeTable" ),
    path('Message/',views.Message, name = "Message" ),
    
    path('ListeTimeTable/',views.ListeTimeTable, name = "ListeTimeTable" ),
    path('RemplirTimeTable/',views.RemplirTimeTable, name = "RemplirTimeTable" ),
    path('AddTimeTableBis1/',views.AddTimeTableBis1, name = "AddTimeTableBis1" ),
    path('AddTimeTableBis2/',views.AddTimeTableBis2, name = "AddTimeTableBis2" ),
    path('AddTimeTableBis3/',views.AddTimeTableBis3, name = "AddTimeTableBis3" ),
    path('AddTimeTableBis4/',views.AddTimeTableBis4, name = "AddTimeTableBis4" ),
    path('AddTimeTableBis5/',views.AddTimeTableBis5, name = "AddTimeTableBis5" ),
    path('AddTimeTableBis6/',views.AddTimeTableBis6, name = "AddTimeTableBis6" ),
    path('AddTimeTableBis7/',views.AddTimeTableBis7, name = "AddTimeTableBis7" ),
    path('AddTimeTableBis8/',views.AddTimeTableBis8, name = "AddTimeTableBis8" ),
    path('AddTimeTableBis9/',views.AddTimeTableBis9, name = "AddTimeTableBis9" ),
    path('AddTimeTableBis10/',views.AddTimeTableBis10, name = "AddTimeTableBis10" ),
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
