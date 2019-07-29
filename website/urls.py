from django.urls import path, include
from website.views import index, sobre, login, cadastrar_ideia, deletar_ideia

urlpatterns = [
    path('', index),
    path('sobre', sobre),
    path('login', login),
    path('ideias', cadastrar_ideia),
    path('deletar_ideia/<int:id>', deletar_ideia)
]