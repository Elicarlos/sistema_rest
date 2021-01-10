from django.db import models
from cadastro.precos.models import TabelaPreco
from cadastro.clientes.models import Clientes
from cadastro.representantes.models import Representante
from cadastro.produtos.models import Produto


class Pedido(models.Model):
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    tabela_preco = models.ForeignKey(TabelaPreco, on_delete=models.CASCADE)
    representante = models.ForeignKey(Representante, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
