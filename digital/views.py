from django.shortcuts import render

from digital.models import ImageModels
from .models import NewsModel, TeachModels

def HomeView(request):
    imagemodel = ImageModels.objects.all()
    news = NewsModel.objects.all()
    context = {
        'news': news
    }
    return render(request, 'index.html', {
        "images": imagemodel
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
