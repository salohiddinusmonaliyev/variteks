from django.db import models

# Create your models here.
class Category(models.Model):
    name_uz = models.CharField(max_length=200)
    name_ru = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Subcategory(models.Model):
    name_uz= models.CharField(max_length=200)
    name_ru= models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Product(models.Model):
    code = models.IntegerField(unique=True)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    name_uz = models.CharField(max_length=200)
    name_ru = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    description_uz = models.TextField(blank=True)
    description_ru = models.TextField(blank=True)
    price = models.IntegerField()
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

class MainImage(models.Model):
    image = models.FileField(upload_to="main/")

class ContentImage(models.Model):
    image = models.FileField(upload_to="content/")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)