from django.db import models
class Sector(models.Model):
    lugar = models.ForeignKey('Lugar')
    nombre = models.CharField(max_length = 20)
    asientos = models.IntegerField()
    ocupado = models.BooleanField()
    
    def __unicode__(self):
        return '{0} - {1}'.format(self.nombre, self.lugar.nombre)
    
    
    class Meta: 
        verbose_name_plural = "Sectores"