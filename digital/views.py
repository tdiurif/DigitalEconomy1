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
    lis = [1, 2, 3, 4, 5, 6]
    context = {
        'lis': lis
    }
    return render(request, 'twoindex.html')


def TechView(request):
    teach = TeachModels.objects.all()
    context = {
        'teach': teach
    }
    return render(request, 'threeindex.html')


# def DepartamentAllView(request,pk):
#     departament = DepartamentModels.objects.get(id=pk)
#     context = {
#         'departament': departament,
#     }
#     return render(request, 'yangiikkindex.html', context)


def DepartamentView(request):
    # departaments = DepartamentModels.objects.all()
    # list1 = []
    # for i in range(1, len(departaments) + 1):
    #     if i % 2 == 0:
    #         list1.append(i)

    return render(request, 'fiveindex.html', {
        # "departaments": departaments,
        # "list1": list1
    })


def TadqiqotlarView(request):
    return render(request, 'sixindex.html')


def FacultyLifeView(request):
    return render(request, 'elevnindex.html')


def FacultySportView(request):
    return render(request, 'tuwelfindex.html')


def SocialProjectView(request):
    return render(request, 'sevenindex.html')


def ScoreBallsView(request):
    return render(request, 'nineindex.html')

def StaticaView(request):
    return render(request,'statica.html')
def AIView(request):
    return render(request,'suniy_intelekt.html')
