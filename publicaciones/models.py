from django.db import models
from destinos.models import Destino
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.core.exceptions import ValidationError


class Publicacion(models.Model):
    usuario = models.ForeignKey(
        User, on_delete=models.CASCADE)
    destino = models.ForeignKey(
        Destino, on_delete=models.CASCADE)
    texto = models.TextField()
    fecha = models.DateField(default=now)

    def __str__(self):
        return f"{self.usuario} - {self.texto[:20]}"

    def clean(self):
        if len(self.texto) < 10:
            raise ValidationError(
                "El texto debe tener al menos 10 caracteres.")
