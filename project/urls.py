from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name='home'),
    path('registration', views.registartion),
    path('login', views.login),
]
