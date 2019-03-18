from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='new-home'),
    path('about', views.about,name='new-about'),
    path('content', views.content,name='new-content'),
]
