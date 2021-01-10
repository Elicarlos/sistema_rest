from django.bd import models


class TabelaPreco(models.Model):
    nome_tabela = models.CharField(max_length=50)


    def tipo_calculo(self):
        '''acrescimo sobre o preco de venda'''
        '''desconto sobre o preco de venda'''
        '''merkup sobre o preco de custo'''
        '''passando percentual em cada 1