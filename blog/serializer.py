from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import *

class BlogUzSerializer(ModelSerializer):
    title = serializers.CharField(source='title_uz')
    class Meta:
        model = Blog
        fields = "title"

class BlogRuSerializer(ModelSerializer):
    title = serializers.CharField(source='title_ru')
    class Meta:
        model = Blog
        fields = "title"

class BlogCategoryUzSerializer(ModelSerializer):
    name = serializers.CharField(source='name_ru')
    class Meta:
        model = BlogCategory
        fields = "__all__"

class BlogCategoryRuSerializer(ModelSerializer):
    name = serializers.CharField(source='name_ru')
    class Meta:
        model = BlogCategory
        fields = "__all__"