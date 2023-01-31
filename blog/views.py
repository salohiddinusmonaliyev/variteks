from django.shortcuts import render
from rest_framework.viewsets import *
from .models import *
from .serializer import *
from rest_framework.response import Response

from rest_framework.views import APIView

class BlogView(APIView):
    queryset = Blog.objects.all()
    def get(self, request, lang):
        if lang=="uz":
            queryset = Blog.objects.all()
            serializer = BlogUzSerializer(queryset, many=True)
            return Response(serializer.data)
        elif lang=="ru":
            queryset = Blog.objects.all()
            serializer = BlogRuSerializer(queryset, many=True)
            return Response(serializer.data)

class BlogCategoryView(APIView):
    queryset = BlogCategory.objects.all()
    def get(self, request, lang):
        if lang=="uz":
            queryset = BlogCategory.objects.all()
            serializer = BlogCategoryUzSerializer(queryset, many=True)
            return Response(serializer.data)
        elif lang=="ru":
            queryset = BlogCategory.objects.all()
            serializer = BlogCategoryRuSerializer(queryset, many=True)
            return Response(serializer.data)