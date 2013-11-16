from django.db import models
class Espectaculo(models.Model):
   nombre = models.CharField(max_length = 20) 
   lugar = models.ForeignKey('Lugar')
   categoria = models.ForeignKey('Categoria')
   hora = models.DateTimeField()
   estado = models.BooleanField()
   descripcion = models.CharField(max_length = 300)
   sectores = models.ManyToManyField('Sector', through = 'Precio')
   