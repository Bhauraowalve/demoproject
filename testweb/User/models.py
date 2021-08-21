from django.db import models

# Create your models here.
class User(models.Model): 
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30) 
    email=models.EmailField() 
    password=models.CharField(max_length=32)
    username=models.CharField(max_length=30)


class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    text=models.TextField(max_length=200)
    created_at=models.DateTimeField()
    updated_at=models.DateTimeField()