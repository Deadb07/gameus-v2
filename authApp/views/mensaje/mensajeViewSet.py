from rest_framework import viewsets, permissions
from authApp.models.mensaje import Mensaje
from authApp.serializers.mensajeSerializer import MensajeSerializer

class mensajeViewSet(viewsets.ModelViewSet):
  queryset = Mensaje.objects.all()
  serializer_class = MensajeSerializer
  permission_classes = [permissions.AllowAny]