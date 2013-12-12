from django.db import models
class Usuario(models.Model):
    nombre = models.CharField(max_length = 30)
    telefono = models.CharField(max_length = 9, primary_key = True)
    documento = models.CharField(max_length = 11)
    espectaculo = models.ManyToManyField('Espectaculo', through = 'Ticket')
    
    
    def __unicode__(self): 
        return '{0} - {1}'.format(self.nombre, self.telefono)
    