from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellido_p = models.CharField(max_length=100)
    apellido_m = models.CharField(max_length = 100)
    sexo = models.CharField(max_length=1)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()

