from rest_framework import viewsets, permissions
from authApp.models.canal import Canal
from authApp.serializers.canalSerializer import CanalSerializer

class canalViewSet(viewsets.ModelViewSet):
  queryset = Canal.objects.all()
  serializer_class = CanalSerializer
  permission_classes = [permissions.AllowAny]