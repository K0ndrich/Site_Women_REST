from django.shortcuts import render
from .models import Women, Category
from .serializers import WomenSerializer

# берем базовые представления из Djago REST
from rest_framework import generics
from rest_framework.views import APIView

from rest_framework.response import Response


class WomenAPIView(APIView):
    # для обработки GET запросов
    def get(self, request):
        # Response просто возвращает фиксированую указаную .json строку
        return Response({"title": "my_value"})


# ListAPIView отображает указаные записи из нашей модели, которую связали в serializers.py
# class WomenAPIView(generics.ListAPIView):
#     # queryset тоже самое что и get_query_set в простом django
#     queryset = Women.objects.filter(is_published=True)
#     # serializer_class указывает на сериализатор для текущего представления, который создали ниже
#     serializer_class = WomenSerializer
