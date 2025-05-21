
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.produtos_add, name='produtos_add'),
    path('estoque/', views.estoque, name='estoque'),
    path('saida/', views.saida, name='saida'),
]