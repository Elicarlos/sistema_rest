from django.contrib import admin
from caju.core.models import Produto, Categoria, Cliente

# Register your models here.
admin.site.register(Produto)
admin.site.register(Categoria)
admin.site.register(Cliente)
