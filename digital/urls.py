from django.urls import path

from .views import HomeView, FacultyAbout, TechView, DepartamentView, TadqiqotlarView, FacultyLifeView, \
    FacultySportView, SocialProjectView, ScoreBallsView,DepartamentAllView

urlpatterns = [
    path("", HomeView, name="home"),
    path("about/", FacultyAbout, name="about"),
    path("tech/", TechView, name="tech"),
    path("kafedra/", DepartamentView, name="departament"),
    path("article/kafedra/<int:pk>/", DepartamentAllView, name="departament_all"),
    path("tadqiqotlar/", TadqiqotlarView, name="tadqiqot"),
    path("facultylife/", FacultyLifeView, name="faculty_life"),
    path("facultysport/", FacultySportView, name="faculty_sport"),
    path("socialproject/", SocialProjectView, name="social_project"),
    path("kirish_ballari/", ScoreBallsView, name="score_ball"),
]
