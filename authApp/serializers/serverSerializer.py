from authApp.models.server import Servidor
from rest_framework import serializers

class serverSerializer(serializers.ModelSerializer):
  class Meta:
    model = Servidor
    fields = ['nombre','creador','permisos','region','canales']