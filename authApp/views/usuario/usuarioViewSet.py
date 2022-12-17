from rest_framework import viewsets, permissions
from authApp.models.usuario import Usuario
from authApp.serializers.usuarioSerializer import UsuarioSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
  queryset = Usuario.objects.all()
  serializer_class = UsuarioSerializer
  permission_classes = [permissions.AllowAny]