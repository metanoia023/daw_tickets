from django.db import models
class Precio(models.Model):
    precio = models.IntegerField()
    sector = models.ForeignKey('Sector')
    espectaculo = models.ForeignKey('Espectaculo')
    
    def __unicode__(self): 
        return '{0} - {1} - $ {2}'.format(self.espectaculo, self.sector.nombre, self.precio)
