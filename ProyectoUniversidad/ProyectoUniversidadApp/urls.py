from django.urls import path

from ProyectoUniversidadApp import views

urlpatterns = [

    path('index',views.index, name="Index"),
    path('credito',views.credito, name="Credito"),
    path('financiero',views.financiero, name="Financiero"),
    path('operacional',views.operacional, name="Operacional"),
]


