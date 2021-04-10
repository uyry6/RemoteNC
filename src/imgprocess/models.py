from django.db import models

# Create your models here.
class IMG(models.Model):
    title       = models.CharField(max_length=20, default='this is title')
    img         = models.FileField()
