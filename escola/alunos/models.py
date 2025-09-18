from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=200)
    sobrenome = models.CharField(max_length=200)
    data_nascimento = models.CharField(max_length=10)
    curso = models.CharField(max_length=200)
