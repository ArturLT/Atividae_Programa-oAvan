from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', views.lista_tarefas, name='lista_tarefas'),
]
