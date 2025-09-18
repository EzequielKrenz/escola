from django.urls import path
from . import views

urlpatterns = [
    # Quando o usuário acessar http://.../cadastro/
    # o Django vai chamar a função cadastrar_aluno
    path('cadastro/', views.cadastrar_aluno, name='cadastro_aluno'),
]