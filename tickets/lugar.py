from django.db import models
class Lugar(models.Model):
    nombre = models.CharField(max_length = 50)
    
    
    def __unicode__(self): 
        return self.nombre
    
    class Meta: 
        verbose_name_plural = "Lugares"    