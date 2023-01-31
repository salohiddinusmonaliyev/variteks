from rest_framework.serializers import ModelSerializer

from .models import *

class SocialSerializer(ModelSerializer):
    class Meta:
        model = Social
        fields = "__all__"