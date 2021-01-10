from django.db import models

class Loja(models.Model):
    cnpj = models.CharField(max_length=50)
    razao_social = models.CharField(max_length=50)
    fantasia = models.CharField(max_length=50)
    data_fundacao = models.DateField()
    suframa = models.CharField(max_length=50)
    inscricao_municipal = models.CharField(max_length=50)
    inscricao_estadual = models.CharField(max_length=50)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)

    


    ativo = models.BooleanField(default=True)
    