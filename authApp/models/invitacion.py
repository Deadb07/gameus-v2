from django.db import models
from authApp.models.usuario import Usuario
from .server import Servidor
from .canal import Canal


class Invitacion(models.Model):
    autor = models.ManyToManyField(Usuario)
    server = models.ManyToManyField(Servidor)
    canal = models.ManyToManyField(Canal)
    clicks = models.IntegerField()
    
    

    def __str__(self):
        return self.autor