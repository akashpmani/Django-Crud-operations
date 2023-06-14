from django.db import models

# Create your models here.

from home.models import Student

class User(models.Model):
    
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    
    roles = models.ManyToManyField(Student , related_name='user_roles')
