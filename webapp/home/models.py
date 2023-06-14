from django.db import models
from django.contrib.auth.models import User



    
class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField(default='No content')
    designation = models.CharField(max_length=30)
    designationinfo = models.TextField(default='No content')
    collageinfo = models.TextField(default='No content')
    college = models.CharField(max_length=30)

    
    
    