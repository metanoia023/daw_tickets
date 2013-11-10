from django.db import models
class Sector(models.Model):
    lugar = models.ForeignKey('Lugar')
    nombre = models.CharField(max_length = 20)
    asientos = models.IntegerField()
    ocupado = models.BooleanField()