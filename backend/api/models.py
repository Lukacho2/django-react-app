from django.db import models

# Create your models here.
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    # image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    description = models.TextField()
    price = models.IntegerField()
    #category = models.CharField(max_length=50)
    created_in = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name