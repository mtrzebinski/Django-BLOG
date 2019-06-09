from django.urls import path
from .views import NewsList, NewsCreate
from . import views

urlpatterns=[
    path('', NewsList.as_view(), name='blog-main'),
    path('about/', views.descriptive_page, name='blog-about'),
    path('post/new/', NewsCreate.as_view(), name='news-create'),
]
