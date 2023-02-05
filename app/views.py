from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from app.models import *
from app.serializer import *


# Create your views here.
class MainView(ModelViewSet):
    queryset = Main.objects.all()
    serializer_class = MainSerializer

class SocialView(ModelViewSet):
    queryset = Social.objects.all()
    serializer_class = SocialSerializer
