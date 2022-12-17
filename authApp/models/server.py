from django.db import models
from .usuario import Usuario
from .canal import Canal


class Servidor(models.Model):
    nombre = models.CharField(max_length=15)
    ##icono = models.ImageField()
    creador = models.ManyToManyField(Usuario)
    permisos = models.CharField(max_length=100)
    region = models.CharField(max_length=12)
    canales = models.ManyToManyField(Canal)
    

    def __str__(self):
        return self.nombre