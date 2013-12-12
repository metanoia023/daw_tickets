from django.db import models
class Ticket(models.Model):
    sector = models.ForeignKey('Sector')
    espectaculo = models.ForeignKey('Espectaculo')
    fecha = models.DateTimeField()
    usuario = models.ForeignKey('Usuario')
    imagen = models.FileField(upload_to = 'afiches', blank = True)
    
    