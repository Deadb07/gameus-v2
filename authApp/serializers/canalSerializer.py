from authApp.models.canal import Canal
from rest_framework import serializers

class CanalSerializer(serializers.ModelSerializer):
  class Meta:
    model = Canal
    fields = ['nombre','tipo','posicion','permisos','nsfw','limiteusuarios']