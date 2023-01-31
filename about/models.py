from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class AboutItem(models.Model):
    title_uz = models.CharField(max_length=100)
    title_ru = models.CharField(max_length=100)
    icon = models.FileField(upload_to="about/")
    file = models.FileField(upload_to="about/", null=True, blank=True)
    text_uz = models.TextField(null=True, blank=True)
    text_ru = models.TextField(null=True, blank=True)

class AboutFile(models.Model):
    file = models.FileField(upload_to="about_file")
    about_item = models.ForeignKey(AboutItem, on_delete=models.CASCADE)
