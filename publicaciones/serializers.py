from rest_framework import serializers
from .models import Publicacion
from django.contrib.auth.models import User


class PublicacionSerializer(serializers.ModelSerializer):
    # Mostrar el nombre del usuario
    usuario = serializers.CharField(source='usuario.username', read_only=True)
    destino = serializers.SerializerMethodField()  # Personalizar el campo destino

    class Meta:
        model = Publicacion
        fields = ['id', 'usuario', 'destino', 'texto', 'fecha']

    def get_destino(self, obj):
        # Concatenar ciudad y país del destino
        return f"{obj.destino.ciudad}, {obj.destino.pais}"
