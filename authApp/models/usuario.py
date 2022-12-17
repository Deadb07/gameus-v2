from django.db import models

class Usuario(models.Model):
    usuario = models.CharField(max_length=12)
    contraseña = models.CharField(max_length=100)
    correo = models.EmailField()
    celular = models.IntegerField()
    nacimiento = models.DateField()


    def __str__(self):
        return self.usuario