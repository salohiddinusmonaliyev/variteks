from django.db import models

from product.models import Product


# Create your models here.
class Social(models.Model):
    icon = models.FileField(upload_to="icons/")
    url = models.URLField()

class Main(models.Model):
    new_product = models.ForeignKey(Product, on_delete=models.CASCADE)