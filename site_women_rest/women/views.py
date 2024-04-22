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
        # не будет отображаться страница Error , а будет json строка с неправильно указаными полями
        serializer = WomenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # сохранение записи в модели
        serializer.save()
        # model_to_dict преобразовует запись или записи модели в тип словаря
        return Response({"post": serializer.data})

    # нужен для изменения записи в модели , вызывает метод update
    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"Error": "Method PUT is not defined"})

        try:
            instance = Women.objects.get(pk=pk)
        except:
            return Response({"Error": "Obejct is not exist"})

        # instance запись в модели, которую будем менять
        serializer = WomenSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"Error": "Method DELETE is not defined"})
        try:
            instance = Women.objects.get(pk=pk)
        except:
            return Response({"Error": "Object is not exist"})

        serializer = WomenSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"Delete Object -> ": str(pk)})


# ListAPIView отображает указаные записи из нашей модели, которую связали в serializers.py
# class WomenAPIView(generics.ListAPIView):
#     # queryset тоже самое что и get_query_set в простом django
#     queryset = Women.objects.all()
#     # serializer_class указывает на сериализатор для текущего представления, который создали ниже
#     serializer_class = WomenSerializer
