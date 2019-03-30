from django.urls import path
from . import views

urlpatterns=[
    path('', views.main_page, name='blog-main'),
    path('about/', views.descriptive_page, name='blog-about'),
]
