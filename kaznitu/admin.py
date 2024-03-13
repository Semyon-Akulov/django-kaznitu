from django.contrib import admin
from .models import *


@admin.register(Researcher)
class ResearcherAdmin(admin.ModelAdmin):
    fields = ('name', 'bio', 'photo')
    search_fields = ['name']

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    fields = ('title', 'content', 'author', 'photo')
    autocomplete_fields = ['author']

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    fields = ('title', 'description', 'photo')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
        list_display = ('title', 'date')
        search_fields = ('title', 'description')
        list_filter = ('date',)

@admin.register(Project)
class Project(admin.ModelAdmin):
    fields = ('title', 'description', 'photo')


@admin.register(Slide)
class SlideAdmin(admin.ModelAdmin):
    fields = ('photo', 'description')

@admin.register(AboutUs)
class AboutSectionAdmin(admin.ModelAdmin):
    fields = ('title', 'text', 'image')


