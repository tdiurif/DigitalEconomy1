from django.urls import path

from digital.views import HomeView,FacultyAbout,TechView

urlpatterns=[
    path("",HomeView,name="home"),
    path("about/",FacultyAbout,name="about"),
    path("tech/",TechView,name="tech"),
]