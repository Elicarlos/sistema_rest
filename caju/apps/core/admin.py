from django.contrib import admin
from caju.apps.core.models import Produto, Categoria, Cliente, Vendedor, Venda, ItensVendas, Fornecedor

# Register your models here.
admin.site.register(Produto)
admin.site.register(Categoria)
admin.site.register(Cliente)
admin.site.register(Vendedor)
admin.site.register(Venda)
admin.site.register(ItensVendas),
admin.site.register(Fornecedor)
