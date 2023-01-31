"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from about.views import *

from account.views import UserViewSet
from rest_framework.routers import DefaultRouter

from blog.views import BlogView
from contact.views import ContactUsView
from product.views import Productview

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("about/<str:lang>/", AboutItemView.as_view()),
    path("blog/<str:lang>/", BlogView.as_view()),
    path("contact/<str:lang>/", ContactUsView.as_view()),
    path("product/<str:lang>/", Productview.as_view()),
    path('', include(router.urls)),
]
