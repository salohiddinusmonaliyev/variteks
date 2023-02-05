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

class HumanResourcesView(APIView):
    queryset = HumanResources.objects.all()

    def get(self, request, lang):
        if lang == "uz":
            queryset = HumanResources.objects.all()
            serializer = HumanResourcesUzSerializer(queryset, many=True)
            return Response(serializer.data)
        elif lang == "ru":
            queryset = HumanResources.objects.all()
            serializer = HumanResourcesRuSerializer(queryset, many=True)
            return Response(serializer.data)
