from django.db import models
class Usuario(models.Model):
    nombre = models.CharField(max_length = 30)
    telefono = models.IntegerField()
    documento = models.CharField(max_length = 11)