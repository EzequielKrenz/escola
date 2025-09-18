from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastrar_aluno, name='cadastrar_aluno'),
    path('lista/', views.listar_alunos, name='listar_alunos'),
]