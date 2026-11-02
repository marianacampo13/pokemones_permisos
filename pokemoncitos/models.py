
from django.db import models


class Entrenador(models.Model):
    documento = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    medallas = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre + " " + self.apellido


class Gimnasio(models.Model):
    nombre = models.CharField(max_length=100)
    elemento = models.CharField(max_length=30)
    insignia = models.CharField(max_length=50)
    lider = models.ForeignKey(
        Entrenador,
        on_delete=models.CASCADE,
        related_name="gimnasios"
    )

    def __str__(self):
        return self.nombre


class Pokemon(models.Model):
    nombre = models.CharField(max_length=50)
    peso = models.FloatField()
    imagen = models.URLField(blank=True)
    entrenador = models.ForeignKey(
        Entrenador,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    habilidades = models.TextField()
    naturaleza = models.CharField(max_length=50)
    elemento = models.CharField(max_length=30)
    descripcion = models.TextField()
    color_carta = models.CharField(max_length=20, default="amarillo")
    accesorio = models.CharField(max_length=50, default="ninguno")

    def __str__(self):
        return self.nombre
