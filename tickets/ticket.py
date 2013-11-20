from django.db import models
class Ticket(models.Model):
    sector = models.ForeignKey('Sector')
    espectaculo = models.ForeignKey('Espectaculo')
    fecha = models.DateTimeField()
    precio = models.DecimalField(max_digits = 6, decimal_places = 2)
    pin = models.IntegerField()
    usuario = models.ForeignKey('Usuario')
    
    