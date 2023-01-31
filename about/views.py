from django.shortcuts import render
from rest_framework.viewsets import *
from .models import *
from .serializer import *
from rest_framework.response import Response

from rest_framework.views import APIView

class AboutItemView(APIView):
    queryset = AboutItem.objects.all()
    def get(self, request, lang):
        if lang=="uz":
            queryset = AboutItem.objects.all()
            serializer = AboutItemUzSerializer(queryset, many=True)
            return Response(serializer.data)
        elif lang=="ru":
            queryset = AboutItem.objects.all()
            serializer = AboutItemRuSerializer(queryset, many=True)
            return Response(serializer.data)