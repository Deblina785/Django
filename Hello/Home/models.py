from django.db import models

# Create your models here.
class Contact(models.Model):
    name= models.CharField(max_length=122)
    address= models.CharField(max_length=300)
    city= models.CharField(max_length=122)
    state= models.CharField(max_length=122)