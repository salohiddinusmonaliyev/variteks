from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import *

# Category_uz
class Category_uz_serializer(serializers.HyperlinkedModelSerializer):
    name = serializers.CharField(source='name_uz')
    class Meta:
        model = Category
        fields = ["name"]


# Category_ru
class Category_ru_serializer(serializers.HyperlinkedModelSerializer):
    name = serializers.CharField(source='name_ru')

    class Meta:
        model = Category
        fields = ["name"]


# Subcategory_uz
class Subcategory_uz_serializer(serializers.HyperlinkedModelSerializer):
    name = serializers.CharField(source='name_uz')
    class Meta:
        model = Subcategory
        fields = ["name"]


# Subcategory_ru
class Subcategory_ru_serializer(serializers.HyperlinkedModelSerializer):
    name = serializers.CharField(source='name_ru')
    class Meta:
        model = Subcategory
        fields = ["name"]

# Product_uz
class Product_uz_serializer(serializers.HyperlinkedModelSerializer):
    name = serializers.CharField(source='name_uz')
    description = serializers.CharField(source='description_uz')

    class Meta:
        model = Product
        fields = ["name","description"]


# Product_ru
class Product_ru_serializer(serializers.HyperlinkedModelSerializer):
    name = serializers.CharField(source='name_ru')
    description = serializers.CharField(source='description_ru')

    class Meta:
        model = Product
        fields = ["name","description"]

class Product_serializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Product
        fields = ["name_uz","name_ru","description_uz"]

# Main
class Main_imageserializer(ModelSerializer):
    class Meta:
        model = MainImage
        fields = '__all__'

# Content
class Content_imageserializer(ModelSerializer):
    class Meta:
        model = ContentImage
        fields = '__all__'