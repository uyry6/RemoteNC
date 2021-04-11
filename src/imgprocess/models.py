from django.db import models

# Create your models here.
class IMG(models.Model):
    title       = models.CharField(default='tile here', max_length=(50))
    img         = models.FileField()

    @property
    def name(self):
        return self.img.url[-3:]
