from django.urls import path

from digital.views import HomeView,FacultyAbout,TechView,DepartamentView,TadqiqotlarView,FacultyLifeView

urlpatterns=[
    path("",HomeView,name="home"),
    path("about/",FacultyAbout,name="about"),
    path("tech/",TechView,name="tech"),
    path("kafedra/",DepartamentView,name="departament"),
    path("tadqiqotlar/",TadqiqotlarView,name="tadqiqot"),
    path("tadqiqotlar/",TadqiqotlarView,name="tadqiqot"),
]