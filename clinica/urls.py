from django.urls import path
from . import views

urlpatterns = [
    path('medicos/', views.listar_medicos, name='listagem de medicos'),
    path('consultas/nova/', views.criar_consulta, name='agendamento'),
    path('consultas/<int:id>', views.detalhes_consulta,  name='detalhes da consulta'),
    path('filtros/', views.filtro_especialidade,  name='filtro_especialidade')

]