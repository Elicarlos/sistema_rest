from django.contrib import admin
from caju.core.models import Produto, Categoria, Cliente, Vendedor, Pedido, ItensProdutos, Fornecedor

# Register your models here.
admin.site.register(Produto)
admin.site.register(Categoria)
admin.site.register(Cliente)
admin.site.register(Vendedor)
admin.site.register(Pedido)
admin.site.register(ItensProdutos),
admin.site.register(Fornecedor)
