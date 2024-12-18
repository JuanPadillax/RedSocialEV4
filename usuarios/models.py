from django.db import models


class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    ubicacion = models.CharField(max_length=100)
