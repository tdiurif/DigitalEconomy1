from django.shortcuts import render

from digital.models import ImageModels
from .models import NewsModel, TeachModels, ImageNextMOdels, ImageActiveMOdels, ImagePrevMOdels


def HomeView(request):
    imagemodel = ImageModels.objects.all()
    imgn = ImageNextMOdels.objects.first()
    imga = ImageActiveMOdels.objects.first()
    imgp = ImagePrevMOdels.objects.first()
    news = NewsModel.objects.all()

    return render(request, 'index.html', {
        "images": imagemodel,
        "imgn": imgn,
        "imga": imga,
        "imgp": imgp,
        "news": news
    })


def FacultyAbout(request):
    return render(request, 'twoindex.html')


def TechView(request):
    teach = TeachModels.objects.all()
    context = {
        'teach': teach
    }
    return render(request, 'threeindex.html')


def DepartamentView(request):
    return render(request, 'fiveindex.html')



def TadqiqotlarView(request):
    return render(request, 'sixindex.html')


def FacultyLifeView(request):
    return render(request, 'elevnindex.html')


def FacultySportView(request):
    return render(request, 'tuwelfindex.html')


def SocialProjectView(request):
    return render(request, 'sevenindex.html')
