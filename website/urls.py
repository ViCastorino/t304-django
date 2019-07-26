(from django.urls import path, include
from . import views, sobre, login

urlpatterns = [
    path('', views.index),
    path('sobre', views.sobre)
    path('login',login)
]