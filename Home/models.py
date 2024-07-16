from django.db import models

# Create your models here.


# Canvas & Bottle Paintings Class
    
    
class OtherImages(models.Model):
    image = models.ImageField(upload_to='otherImages')
    
    
class Canvas(models.Model):
    image = models.ImageField(upload_to='prodpics')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    medium = models.CharField(max_length=100)
    size = models.CharField(max_length=50)


class Bottles(models.Model):
    image = models.ImageField(upload_to='prodpics')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    medium = models.CharField(max_length=100)
    
    
class Gallery(models.Model):
    image = models.ImageField(upload_to='prodpics')
    
    
class Testimonials(models.Model):
    image = models.ImageField(upload_to='testimonialpics')
    testimonial = models.TextField()
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    
    
class Artists(models.Model):
    image = models.ImageField(upload_to='artistpics')
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.TextField()
    

class Order(models.Model):
    pass
    
