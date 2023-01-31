from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class HumanResources(models.Model):
    text_uz = RichTextField()
    text_ru = RichTextField()
    url = models.URLField()

class ContactUs(models.Model):
    text_uz = models.TextField()
    text_ru = models.TextField()
    p_number = models.CharField(max_length=60)