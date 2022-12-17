from django.db import models
from authApp.models.usuario import Usuario


class Mensaje(models.Model):
    autor = models.ManyToManyField(Usuario)
    contenido = models.CharField(max_length=300)
    hora_envio = models.DateTimeField()
    reaccion = models.CharField(max_length=12)
    menciones = models.CharField(max_length=12)
    

    def __str__(self):
        return self.autor