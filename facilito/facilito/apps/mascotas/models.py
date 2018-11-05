from django.db import models
from django.utils import timezone

from facilito.apps.adopciones.models import Persona


class Vacuna(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Mascota(models.Model):
    nombre = models.CharField(default='', max_length=50)
    sexo = models.CharField(default='', max_length=10)
    edad_aproximada = models.IntegerField(default=0)
    fecha_rescate = models.DateField(default=timezone.now)
    persona = models.ForeignKey(Persona, null=True, blank=True, on_delete=models.CASCADE)
    vacuna = models.ManyToManyField(Vacuna, blank=True)

    def __str__(self):
        return self.nombre
    