from django.shortcuts import render
from django.forms import model_to_dict

from .models import Women, Category
from .serializers import WomenSerializer

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response


class WomenAPIView(APIView):
    # для обработки GET запросов
    def get(self, request):

        w = Women.objects.all()
        # Response просто возвращает фиксированую указаную .json строку
        # many=True указывает серилизиатору обрабатывать не одну запись  , а queryset записей нашей модели
        # data возвращает саму строку json
        return Response({"posts": WomenSerializer(w, many=True).data})

    # для обработки POST запросов
    def post(self, request):

        # проверку значений которые передаеть пользователь с указаными сериализаторе WomenSerializer
        # не бут отображаться странице Error , а json строке с неправильно указаными полями
        serializer = WomenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # создание новой записи в модели клиентов через POST запрос
        post_new = Women.objects.create(
            # requet.data["title"] - ето значения в URL адресе
            title=request.data["title"],
            content=request.data["content"],
            cat_id=request.data["cat_id"],
        )

        # model_to_dict преобразовует запись или записи модели в тип словаря
        return Response({"post": WomenSerializer(post_new).data})


# ListAPIView отображает указаные записи из нашей модели, которую связали в serializers.py
# class WomenAPIView(generics.ListAPIView):
#     # queryset тоже самое что и get_query_set в простом django
#     queryset = Women.objects.all()
#     # serializer_class указывает на сериализатор для текущего представления, который создали ниже
#     serializer_class = WomenSerializer
