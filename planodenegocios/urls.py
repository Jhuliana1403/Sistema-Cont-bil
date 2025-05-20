from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('analise-setor/', views.analise_setor, name='analise_setor'),
    path('mercado-potencial/', views.mercado_potencial, name='mercado_potencial'),
    path('analise-concorrencia/', views.analise_concorrencia, name='analise_concorrencia'),
]