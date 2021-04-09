from django.db import models

# Create your models here.
class IMG(models.Model):
    title       = models.CharField(max_length=50)
    img         = models.FileField()
