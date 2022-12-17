from django.db import models
##from .server import Servidor


class Canal(models.Model):
##    servidor = models.ManyToManyField(Servidor)
    nombre = models.CharField(max_length=15)
    tipo = models.CharField(max_length=15)
    posicion = models.CharField(max_length=100)
    permisos = models.CharField(max_length=12)
    nsfw = models.BooleanField()
    limiteusuarios = models.IntegerField()

    def __str__(self):
        return self.nombre