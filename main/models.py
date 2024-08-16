

from django.db import models

class Banner(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='banner_images/')
    
    def __str__(self):
        return self.title
    


class Order(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=20)
    quantity = models.IntegerField()
    
    def __str__(self):
        return self.name



class Food(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='product_images/')
   
    
    def __str__(self):
        return self.title
    
    
    
class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
    
    

    
    
    


    
    
    
    





