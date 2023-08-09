from django.db import models

# Create your models here.

# Creo el modelo de la Tarea
class Tarea( models.Model ):

    # Creo los campos que se van a usar
    titulo = models.CharField( max_length= 255 )
    texto = models.TextField()
    estado = models.CharField( max_length = 30 )