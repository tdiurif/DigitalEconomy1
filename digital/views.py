from django.shortcuts import render

from digital.models import ImageModels


def HomeView(request):
    imagemodel = ImageModels.objects.all()
    return render(request, 'index.html', {
        "images": imagemodel
    })


def FacultyAbout(request):
    return render(request, 'twoindex.html')


def TechView(request):
    return render(request, 'threeindex.html')
