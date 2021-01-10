from django.db import models


class Endereco(models.Model):
    cep = models.CharField(max_length=20)
    # Criar um modulo de cidades
    cidade = models.CharField(max_length=80)
    endereco = models.CharField(max_length=50)
    numero = models.CharField(max_length=30)
    complemnto = models.CharField(max_length=30)
    bairro = models.CharField(max_length=30)