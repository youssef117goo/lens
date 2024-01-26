from django.db import models

# Create your models here.

class Lens(models.Model):
    image = models.ImageField(upload_to='images/',null=False)