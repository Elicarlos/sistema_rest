from django.db import models


class Forncedor(models.Model):
    razao = models.CharField(max_length=50)

