from django.db import models
class Precio(models.Model):
    precio = models.IntegerField()
    sector = models.ForeignKey('Sector')
    espectaculo = models.ForeignKey('Espectaculo')
    
