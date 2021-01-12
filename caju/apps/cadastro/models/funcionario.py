from django.db import models
class Usuario(models.Model):
    pass


class PerfilUsuario(models.Model):
    pass

class Cargo(models.Model):
    cargo = models.CharField(max_length=50)

class Funcionarios(models.Model):
    nome = models.CharField(max_length=50)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    salario = models.FloatField()
    active = models.BooleanField(default=True)
