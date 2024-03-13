from django.db import models
from django.contrib.auth.models import User


class Institute(models.Model):
    description = models.TextField(verbose_name="Описание")

class News(models.Model):
    title = models.CharField(verbose_name="Заголовок", max_length=100)
    description = models.TextField(verbose_name="Описание")
    created_at = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(verbose_name="Путь к фото",
                              upload_to="photo_for_news/",
                              blank=True)

class Project(models.Model):
    title = models.CharField(verbose_name="Заголовок", max_length=100)
    description = models.TextField(verbose_name="Описание")
    documents = models.FileField(upload_to="documents/", blank=True)

class Researcher(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    projects = models.ManyToManyField(Project)
    photo = models.ImageField(verbose_name="Путь к фото",
                              upload_to="photo_for_news/",
                              blank=True)

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(Researcher, on_delete=models.CASCADE)
    published_at = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(verbose_name="Путь к фото",
                              upload_to="photo_for_news/",
                              blank=True)

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField()
    photo = models.ImageField(verbose_name="Путь к фото",
                              upload_to="photo_for_news/",
                              blank=True)

class Slide(models.Model):
    photo = models.ImageField(verbose_name="Путь к фото",
                              upload_to="photo_for_news/",
                              blank=True)
    description = models.TextField()

class AboutUs(models.Model):
    title = models.CharField(max_length=100, default='Заголовок')
    text = models.TextField()
    image = models.ImageField(upload_to='photo_for_news/', blank=True, null=True)

