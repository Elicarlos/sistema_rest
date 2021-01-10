from django.db import models




class Produto(models.Model):
    descricao = models.CharField(max_length=50)
    referencia_interna = models.CharField(max_length=50)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    unidade_medida = models.ForeignKey(UnidadeMedida, on_delete=models.CASCADE)
    ncm = models.ForeignKey(Ncm, on_delete=models.CASCADE)
    cest = models.ForeignKey(Cest, on_delete=models.CASCADE)
    preco_fornecedor = models.FloatField()
    preco_custo = models.FloatField()
    preco_venda = models.FloatField()
    preco_minimo_venda = models.FloatField()
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    imagem = models.ImageField()
    active = models.BooleanField(default=True)




class Promocoes(models.Model):
    nome_promocao = models.CharField(max_length=50)
    periodo_inicial = models.DateField()
    periodo_final = models.DateField()

    def desconto_por_categoria():
        pass
        # Nome da categoria X Desconto


    def desconto_por_produto():
        pass
        # Nome do Produto X Preco Promocional
