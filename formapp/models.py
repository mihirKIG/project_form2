from django.db import models

# Create your models here.

class Register(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    password1 = models.IntegerField()
    password2 = models.IntegerField()
        
    
    
