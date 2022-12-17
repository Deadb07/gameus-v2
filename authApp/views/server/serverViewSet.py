from rest_framework import viewsets, permissions
from authApp.models.server import Servidor
from authApp.serializers.serverSerializer import serverSerializer

class serverViewSet(viewsets.ModelViewSet):
  queryset = Servidor.objects.all()
  serializer_class = serverSerializer
  permission_classes = [permissions.AllowAny]