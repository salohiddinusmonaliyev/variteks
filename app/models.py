from django.db import models

# Create your models here.
class Social(models.Model):
    icon = models.FileField(upload_to="icons/")
    url = models.URLField()