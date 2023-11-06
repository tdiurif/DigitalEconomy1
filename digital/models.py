from django.db import models


class NewsModel(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True)
    image = models.ImageField(upload_to='static/img/news/', blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    date_ad = models.DateTimeField(auto_now_add=True, blank=True, null=True)


class DepartamentModels(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='static/img/departament/', blank=True, null=True)
    body = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.title} | {self.name}'


class TeachModels(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='static/image/teach/', blank=True, null=True)

    def __str__(self):
        return f'Rasm {self.id}'


class ImageModels(models.Model):
    image = models.ImageField(upload_to='static/image/skrol/', blank=True, null=True)


class ImageActiveMOdels(models.Model):
    image = models.ImageField(upload_to='static/image/skrol/', blank=True, null=True)


class ImageNextMOdels(models.Model):
    image = models.ImageField(upload_to='static/image/skrol/', blank=True, null=True)


class ImagePrevMOdels(models.Model):
    image = models.ImageField(upload_to='static/image/skrol/', blank=True, null=True)


class FacultetsModels(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    body = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='static/image/facultets/', blank=True, null=True)

    def __str__(self):
        return f'{self.title}'


class SlideModels(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='static/image/slide/', blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)


class DaysModel(models.Model):
    day = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.day}'


class GroupModel(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'


class ScheduleModel(models.Model):
    day = models.ForeignKey(DaysModel, on_delete=models.CASCADE)
    group = models.ForeignKey(GroupModel, on_delete=models.CASCADE)
    sub1 = models.CharField(max_length=255, null=True, blank=True)
    sub2 = models.CharField(max_length=255, null=True, blank=True)
    sub3 = models.CharField(max_length=255, null=True, blank=True)
    sub4 = models.CharField(max_length=255, null=True, blank=True)
    time1 = models.TimeField(blank=True, null=True)
    time2 = models.TimeField(blank=True, null=True)
    time3 = models.TimeField(blank=True, null=True)
    time4 = models.TimeField(blank=True, null=True)

    def __str__(self):
        return f'{self.group}'


class ProfessorModel(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='static/img/professor/')
    body = models.TextField()
    email = models.EmailField(blank=True, null=True)
    number = models.CharField(max_length=255, blank=True, null=True)
    room = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'


class TeachersModel(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='static/img/professor/')
    body = models.TextField()
    email = models.EmailField(blank=True, null=True)
    number = models.CharField(max_length=255, blank=True, null=True)
    room = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'


class BitiruvchilarModel(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    ball = models.DecimalField()

    def __str__(self):
        return f'{self.name}   |    {self.ball}'
