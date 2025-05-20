from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('marketing/posicionamento', views.posicionamento, name='posicionamento'),
    path('marketing/focosegmentacao', views.foco, name='foco'),
    path('marketing/plano', views.plano, name='plano'),
    path('marketing/distribuicao', views.distribuicao, name='distribuicao'),
]