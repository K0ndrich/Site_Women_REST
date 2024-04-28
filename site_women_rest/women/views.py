from django.shortcuts import render
from django.forms import model_to_dict

from .models import Women, Category
from .serializers import WomenSerializer

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
    ListCreateAPIView,
    RetrieveUpdateAPIView,
    RetrieveDestroyAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework import viewsets

from rest_framework.decorators import action


# ViewSet -> APIView
class WomenViewSet(viewsets.ModelViewSet):
    # queryset = Women.objects.all()
    serializer_class = WomenSerializer

    # переопредиляем queryset , который был выше
    def get_queryset(self):
        pk = self.kwargs.get("pk")
        if not pk:
            return Women.objects.all()[:3]

        return Women.objects.filter(pk=pk)

    # @action позволяет добалвялть новые методы для маршрутизации
    # detail=True будет возвращаться одну запись в таблице Category
    @action(methods=["GET"], detail=True)
    def category(self, request, pk=None):
        cats = Category.objects.filter(pk=pk)
        return Response({"cats": [c.name for c in cats]})


# -----   НЕ ИСПОЛЬЗУЕМ   -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# class WomenAPIList(ListCreateAPIView):
#     # queryset список записей, которые будут возвращаться клиенту
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer


# class WomenAPIUpdate(UpdateAPIView):
#     # но клиенту будет возвращаться одна текузая измененая запись
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer


# class WomenAPIDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer


# -----   НЕ ИСПОЛЬЗУЕМ   --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#  class WomenAPIView(APIView):
#     # для обработки GET запросов
#     def get(self, request):

#         w = Women.objects.all()
#         # Response просто возвращает фиксированую указаную .json строку
#         # many=True указывает серилизиатору обрабатывать не одну запись  , а queryset записей нашей модели
#         # data возвращает саму строку json
#         return Response({"posts": WomenSerializer(w, many=True).data})

#     # для обработки POST запросов
#     def post(self, request):

#         # проверку значений которые передаеть пользователь с указаными сериализаторе WomenSerializer
#         # не будет отображаться страница Error , а будет json строка с неправильно указаными полями
#         serializer = WomenSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         # сохранение записи в модели
#         serializer.save()
#         # model_to_dict преобразовует запись или записи модели в тип словаря
#         return Response({"post": serializer.data})

#     # нужен для изменения записи в модели , вызывает метод update
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"Error": "Method PUT is not defined"})

#         try:
#             instance = Women.objects.get(pk=pk)
#         except:
#             return Response({"Error": "Obejct is not exist"})

#         # instance запись в модели, которую будем менять
#         serializer = WomenSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"post": serializer.data})
