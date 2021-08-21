from django.db import models

# Create your models here.
class Product(models.Model): 
    name=models.CharField(max_length=30)
    weight=models.FloatField() 
    price=models.FloatField()
    created_at=models.DateTimeField()
    updated_at=models.DateTimeField()