from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class BlogCategory(models.Model):
    name_uz = models.CharField(max_length=100)
    name_ru = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Blog(models.Model):
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE, null=True)
    title_uz = models.CharField(max_length=100)
    title_ru = models.CharField(max_length=100)
    image = models.FileField()
    body_uz = RichTextField()
    body_ru = RichTextField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
