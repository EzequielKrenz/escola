from django.shortcuts import render
from .models import Aluno

def cadastrar_aluno(request):
    return render(request, 'CadAluno.html')
