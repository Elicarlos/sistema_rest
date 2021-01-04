from django.db import models

# Create your models here.

class Categoria(models.Model):
    categoria = models.CharField(max_length=50)

    def __str__(self):
        return self.categoria


class Produto(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    descricao = models.CharField(max_length=100, blank=True)
    categoria = models.ForeignKey(Categoria, related_name='categorias', on_delete=models.CASCADE)
    preco_compra = models.FloatField()
    preco_venda = models.FloatField()

    def __str__(self):
        return self.descricao

    class Meta:
        ordering = ['created']

    
class Cliente(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=100)
    endereco = models.CharField(max_length=30)
    cidade = models.CharField(max_length=30)
    estado = models.CharField(max_length=30)
    telefone = models.CharField(max_length=30)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['created']