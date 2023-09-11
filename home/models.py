from django.db import models

# Create your models here.
class Recepie(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.FileField(upload_to='home/food_images')
    
    def __str__(self):
        return self.name
    
