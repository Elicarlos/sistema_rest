from django.db import models


class Perfil(models.Model):
    descricao = models.CharField(max_length=50)

    def permissoes(self):
        pass
        ''' Lista de permissoes''