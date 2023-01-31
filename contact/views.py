from django.shortcuts import render
from rest_framework.viewsets import *
from .models import *
from .serializer import *
from rest_framework.response import Response

from rest_framework.views import APIView

class ContactUsView(APIView):
    queryset = ContactUs.objects.all()
    def get(self, request, lang):
        if lang=="uz":
            queryset = ContactUs.objects.all()
            serializer = ContactUzSerializer(queryset, many=True)
            return Response(serializer.data)
        elif lang=="ru":
            queryset = ContactUs.objects.all()
            serializer = ContactRuSerializer(queryset, many=True)
            return Response(serializer.data)