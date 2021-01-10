from django.db import models
from cadastro.models import Endereco

# Create your models here.


class Classificacao_Clientes(models.Model):
    descricao = models.CharField(max_length=50)


    # Regras 
        """ Não validar limite de crédito ou dívidas vencidas """
        """ Bloquear vendas apartir de [ ] dia de divida vencida """
        """ Bloquear completamente (Venda e Orçamento) """
        """ Cor da etiqueta """


class Cliente(models.Model):
    cpf = models.CharField(max_length=20)
    nome = models.CharField(max_length=80)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    # Criar um select aqui
    sexo = models.CharField(max_length=30)
    aniversario = models.CharField(max_length=30)
    rg = models.CharField(max_length=30)
    inscricao_estadual = models.CharField(max_length=30)
    nome_pai = models.CharField(max_length=30)
    nome_mae = models.CharField(max_length=30)
    naturalidade = models.CharField(max_length=30)
    telefone1 = models.CharField(max_length=30)
    telefone2 = models.CharField(max_length=30)
    email = models.CharField(max_length=30)

    # Comercial
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    tabela_preco = models.ForeignKey(TabelaPreco, on_delete=models.CASCADE)
    # Financeiro
    limite_credito = models.FloatField()
    saldo_disponivel = models.FloatField()

    endereco_cobranca = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    classificacao = models.ForeignKey(Classificacao_Clientes, on_delete=models.CASCADE)
    tipo = models.Choices()
    active = models.BooleanField(default=True)


class Cliente(Usuario):
    pass

class Fornecedor(Usuario):
    pass

class Transportador(Usuario):
    pass

class Funcionari(Usuario):
    pass

class ParceiroComercial(Usuario):
    pass

class Representante(Usuario):
    pass

