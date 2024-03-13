from django.views.generic import DetailView, ListView
from django.views.generic import TemplateView
from django.shortcuts import render
from .models import *
class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_news'] = News.objects.all()[:3]
        context['slides'] = Slide.objects.all()
        context['about_us_list'] = AboutUs.objects.all()
        return context
class NewsListView(ListView):
    model = News
    template_name = 'news_list.html'

class ProjectListView(ListView):
    model = Project
    template_name = 'project_list.html'

class ResearcherListView(ListView):
    model = Researcher
    template_name = 'researcher_list.html'

class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'

class EventListView(ListView):
    model = Event
    template_name = 'event_list.html'






