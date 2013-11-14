from django.db import models

class Pin(models.Model):

    numero = models.IntegerField()
    telefono = models.ForeignKey('Usuario')