from django.db import models

# Create your models here.
class Upload(models.Model):
    image= models.ImageField(upload_to='media',null=True)
    date= models.DateTimeField(auto_now=True)