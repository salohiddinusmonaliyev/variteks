from django.shortcuts import render
from rest_framework.viewsets import *
from .models import *
from .serializer import *
from rest_framework.response import Response

from rest_framework.views import APIView

class Main_imageViewSet(ModelViewSet):
    queryset = MainImage.objects.all()
    serializer_class = Main_imageserializer


class Content_imageViewSet(ModelViewSet):
    queryset = ContentImage.objects.all()
    serializer_class = Content_imageserializer

class Categoryview(APIView):
    queryset = Category.objects.all()
    def get(self,request,lang):
        if lang=="uz":
            queryset = Category.objects.all()
            serializer = Category_uz_serializer(queryset,many=True)
            return Response(serializer.data)
        elif lang=="ru":
            queryset = Category.objects.all()
            serializer = Category_ru_serializer(queryset,many=True)
            return Response(serializer.data)


class Subcategoryview(APIView):
    queryset = Subcategory.objects.all()
    def get(self,request,lang):
        if lang=="uz":
            queryset = Subcategory.objects.all()
            serializer = Subcategory_uz_serializer(queryset,many=True)
            return Response(serializer.data)
        elif lang=="ru":
            queryset = Subcategory.objects.all()
            serializer = Subcategory_ru_serializer(queryset,many=True)
            return Response(serializer.data)


class Productview(APIView):
    queryset = Product.objects.all()
    def get(self,request,lang):
        if lang=="uz":
            queryset = Product.objects.all()
            serializer = Product_uz_serializer(queryset,many=True)
            return Response(serializer.data)
        elif lang=="ru":
            queryset = Product.objects.all()
            serializer = Product_ru_serializer(queryset,many=True)
            return Response(serializer.data)
