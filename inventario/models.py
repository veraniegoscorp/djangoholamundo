from django.db import models

# Create your models here.
class producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField(default=0)
    descripcion = models.CharField(max_length=100, null=True, blank=True)
    stock = models.IntegerField(default=0)