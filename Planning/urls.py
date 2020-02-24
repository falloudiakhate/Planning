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
    path('ListeUpdateTimeTable/',views.ListeUpdateTimeTable, name = "ListeUpdateTimeTable" ),
    path('UpdateTimeTable/<int:id>',views.UpdateTimeTable, name = "UpdateTimeTable" ),
    path('DeleteTimeTable/<int:id>',views.DeleteTimeTable, name = "DeleteTimeTable" ),
    path('Message/',views.Message, name = "Message" ),
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
