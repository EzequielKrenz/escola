from django.db import models

# Create your models here.
class Aluno(models.Model):
    nome = models.CharField(max_length=200)
    sobreno = models.CharField(max_length=200)
    data_nascimento = models.CharField(max_length=10)
    curso = models.CharField(max_length=200)
