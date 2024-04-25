"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from women.views import *
from rest_framework import routers

# создание своего роутера
router = routers.SimpleRouter()
# регистрация нашего ViewSet в роутере
# women подсталяеться в конец нашего пути
router.register(r"women", WomenViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    #
    # заходим в сам API нашего сайта
    # обрабатывает все типы запросов
    path("api/v1/", include(router.urls)),  # 127.0.0.1:8000/api/v1/women
    #
    # для ViewSet нужно указывать какие методы будут вызывать для каждого типа запроса от клиента
    # get (тип запроса) : list (какой метод будет обрабатывать)
    # path("api/v1/womenlist/", WomenViewSet.as_view({"get": "list"})),
    # path("api/v1/womenlist/<int:pk>/", WomenViewSet.as_view({"put": "update"})),
]
