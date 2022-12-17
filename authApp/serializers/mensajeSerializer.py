from authApp.models.mensaje import Mensaje
from rest_framework import serializers

class MensajeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Mensaje
    fields = ['autor','contenido','hora_envio','reaccion','menciones']