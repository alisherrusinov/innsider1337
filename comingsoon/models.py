from django.db import models

# Create your models here.

class submitmodel(models.Model):
    text = models.EmailField(default='ivan@gmail.com')
