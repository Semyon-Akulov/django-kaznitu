from django.urls import path
from kaznitu.views import *
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('news/', NewsListView.as_view(), name='news-list'),
    path('projects/', ProjectListView.as_view(), name='projects'),
    path('researchers/', ResearcherListView.as_view(), name='researcher-list'),
    path('articles/', ArticleListView.as_view(), name='article-list'),
    path('events/', EventListView.as_view(), name='event-list'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
