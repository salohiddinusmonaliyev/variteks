from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from .models import *

class AboutItemUzSerializer(ModelSerializer):
    title = serializers.CharField(source="title_uz")
    text = serializers.CharField(source="text_uz")
    class Meta:
        model = AboutFile
        fields = ["title", 'text']


class AboutItemRuSerializer(serializers.HyperlinkedModelSerializer):
    title = serializers.CharField(source='title_ru')
    text = serializers.CharField(source="text_ru")
    class Meta:
        model = AboutFile
        fields = ["title", 'text']

class AboutItemSerializer(ModelSerializer):
    class Meta:
        model = AboutItem
        fields = "__all__"