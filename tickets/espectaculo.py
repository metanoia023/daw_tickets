from django.db import models

class Espectaculo(models.Model):
    nombre = models.CharField(max_length = 20) 
    lugar = models.ForeignKey('Lugar')
    categoria = models.ForeignKey('Categoria')
    hora = models.DateTimeField()
    estado = models.BooleanField()
    descripcion = models.CharField(max_length = 300)
    sectores = models.ManyToManyField('Sector', through = 'Precio')
    
    
    def actualizar(self):
        from tickets.espectaculo import Espectaculo
        from tickets.categoria import Categoria
        from tickets.lugar import Lugar
    
        espectaculos = Espectaculo.objects.all()
        categorias = Categoria.objects.all()
        lugares = Lugar.objects.all()
        
    
    
    
    
 