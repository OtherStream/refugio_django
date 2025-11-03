from rest_framework import serializers
from .models import Solicitud
from animales.models import Animal
from usuarios.models import Usuario

class SolicitudSerializer(serializers.ModelSerializer):
    usuario = serializers.StringRelatedField(read_only=True)
    animal = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Solicitud
        fields = ['id', 'usuario', 'animal', 'aceptado', 'fecha_solicitud']