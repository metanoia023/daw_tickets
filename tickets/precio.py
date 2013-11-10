from django.db import models
class Precio(models.Model):
    precio = models.DecimalField(max_digits = 6, decimal_places = 2)
    sector = models.ForeignKey('Sector')
    espectaculo = models.ForeignKey('Espectaculo')
    
