from django.db import models

# Create your models here.


# Canvas & Bottle Paintings Class


class Products(models.Model):
    image = models.ImageField(upload_to='prodpics')
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    medium = models.CharField(max_length=100)


class Bottles(models.Model):
    image = models.ImageField(upload_to='prodpics')
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    medium = models.CharField(max_length=100)
    
    
class Gallery(models.Model):
    image = models.ImageField(upload_to='prodpics')