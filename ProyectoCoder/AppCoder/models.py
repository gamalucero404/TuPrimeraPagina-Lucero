from django.db import models

# Create your models here.



class Productos(models.Model):
    nombre = models.CharField(max_length = 40)
    categoria = models.CharField(max_length = 40)

class Tiendas(models.Model):
    tienda = models.CharField(max_length=40)
    caro = models.BooleanField(default=False)
    barato = models.BooleanField(default=False)

class Descuentos(models.Model):
    tiendas = models.CharField(max_length=40)
    productos_desc = models.CharField(max_length=40)