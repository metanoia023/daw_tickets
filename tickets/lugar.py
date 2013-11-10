from django.db import models
class Lugar(models.Model):
    nombre = models.CharField(max_length = 50)