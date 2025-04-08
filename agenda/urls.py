from django.urls import path
from . import views

urlpatterns = [
    path('api/servicos/', views.read_servicos),
    path('api/servicos/<int:pk>', views.detalhes_servicos),

    path('api/agendamentos/', views.read_agendamentos),
    path('api/agendamentos/<int:pk>', views.detalhes_agendametos),

]
