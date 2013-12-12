from django.db import models

class Afiche(models.Model):
    nombre = models.CharField(max_size=100, unique=True)