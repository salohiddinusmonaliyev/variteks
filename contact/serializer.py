from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import *

class ContactUzSerializer(ModelSerializer):
    text = serializers.CharField(source='text_uz')
    class Meta:
        model = ContactUs
        fields = ["text"]


class HumanResourcesUzSerializer(ModelSerializer):
    text = serializers.CharField(source='text_uz')
    class Meta:
        model = HumanResources
        fields = ["text"]

class ContactRuSerializer(ModelSerializer):
    text = serializers.CharField(source='text_ru')
    class Meta:
        model = ContactUs
        fields = ["text"]


class HumanResourcesRuSerializer(ModelSerializer):
    text = serializers.CharField(source='text_ru')
    class Meta:
        model = HumanResources
        fields = ["text"]