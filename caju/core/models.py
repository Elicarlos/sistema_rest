from django.db import models

# Create your models here.

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


class Vendedor(models.Model):
    nome = models.CharField(max_length=30)
    def __str__(self):
        return self.nome


class Categoria(models.Model):
    categoria = models.CharField(max_length=50)

    def __str__(self):
        return self.categoria


class Produto(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    descricao = models.CharField(max_length=100, blank=True)
    categoria = models.ForeignKey(Categoria, related_name='categorias', on_delete=models.CASCADE)
    preco_compra = models.FloatField()
    preco_custo = models.FloatField()    
    preco_venda = models.FloatField()
    estoque = models.IntegerField()
    estoque_minimo = models.IntegerField()

    def __str__(self):
        return self.descricao

    class Meta:
        ordering = ['created']  

  

class Pedido(models.Model):   
    cliente = models.ForeignKey(Cliente, related_name='cliente', on_delete=models.CASCADE)
    vendedor = models.ForeignKey(Vendedor, related_name='vendedor', on_delete=models.CASCADE)
    
    data_venda = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.pk)


class ItensProdutos(models.Model):
    pedido_id = models.ForeignKey(Pedido, on_delete=models.CASCADE)   
    produto = models.ForeignKey(Produto, related_name='produtos', on_delete=models.CASCADE)
    quantidade = models.IntegerField()

    def __str__(self):
        # pylint: disable=E1101
        return self.produto.descricao 





    


class Fornecedor(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    razao_social = models.CharField(max_length=50)
    fantasia = models.CharField(max_length=50)
    cnpj = models.CharField(max_length=20)
    inscricao_estadual = models.CharField(max_length=20)
    cep = models.CharField(max_length=30)
    endereco = models.CharField(max_length=20)
    bairro = models.CharField(max_length=30)
    cidade = models.CharField(max_length=30)
    estado = models.CharField(max_length=30)
    