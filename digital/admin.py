from django.contrib import admin
from .models import DepartamentModels, NewsModel, TeachModels, ImageModels, FacultetsModels, SlideModels, GroupModel, DaysModel, ScheduleModel, ImageActiveMOdels, ImageNextMOdels, ImagePrevMOdels

admin.site.register(DepartamentModels)
admin.site.register(NewsModel)
admin.site.register(TeachModels)
admin.site.register(ImageModels)
admin.site.register(ImageActiveMOdels)
admin.site.register(ImageNextMOdels)
admin.site.register(ImagePrevMOdels)
admin.site.register(FacultetsModels)
admin.site.register(SlideModels)
admin.site.register(DaysModel)
admin.site.register(ScheduleModel)
admin.site.register(GroupModel)
