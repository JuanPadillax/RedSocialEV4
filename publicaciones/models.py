from django.db import models
from destinos.models import Destino
from django.contrib.auth.models import User
from django.utils.timezone import now


class Publicacion(models.Model):
    usuario = models.ForeignKey(
        User, on_delete=models.CASCADE)  # Relación con User
    destino = models.ForeignKey(
        Destino, on_delete=models.CASCADE)  # Relación con Destino
    texto = models.TextField()
    fecha = models.DateField(default=now)

    def __str__(self):
        return f"{self.usuario} - {self.texto[:20]}"
