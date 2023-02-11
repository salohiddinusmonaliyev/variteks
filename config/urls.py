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

from app.views import *
from blog.views import BlogView
from contact.views import *
from product.views import *

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register('main', MainView)
router.register('social', SocialView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path("about-us/<str:lang>/", AboutItemView.as_view()),
    path("blog/<str:lang>/", BlogView.as_view()),
    path("contact/<str:lang>/", ContactUsView.as_view()),
    path("human-resources/<str:lang>/", HumanResourcesView.as_view()),
    path("product/", Productview.as_view()),
    path("test/ ", UserListView.as_view()),
    # path("main/", MainView.as_view()),
    path('', include(router.urls)),
]
