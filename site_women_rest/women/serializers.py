# В етом файле храняться сериализаторы для наших представлений в views.py
from .models import Women, Category
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io


# ModelSerializer специальный сериализатор для работы с моделями , уже встроенный функционал с созданием, изменением, удалением записей в модели
class WomenSerializer(serializers.ModelSerializer):
    class Meta:
        # указываем модель с которой свзяываемся
        model = Women
        # указываем поля которые будем возвращать пользователю
        fields = "__all__"


# -----   НЕ ИСПОЛЬЗУЕМ   --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# создание сериализатора для модели Women
# текущий сериализатор проверяет значения которые отправил клиент в POST запросе с указаными характеристиками
# class WomenSerializer(serializers.Serializer):
#     # все записанные поля беруться из нашей модели models.py
#     title = serializers.CharField(max_length=255)
#     content = serializers.CharField()
#     time_create = serializers.DateTimeField(read_only=True)
#     time_update = serializers.DateTimeField(read_only=True)
#     is_published = serializers.BooleanField(default=True)
#     cat_id = serializers.IntegerField()

#     # добавление записей в наше модель Women
#     # validated_data хранит все данные которые пользователь указал в POST запросе
#     def create(self, validated_data):
#         return Women.objects.create(**validated_data)

#     # зименение уже существуюущей записи в модели
#     def update(self, instance, validate_data):
#         # берем значение из POST запроса пользователя , если нету тогда возвращаем второй агрумент функци get()
#         instance.title = validate_data.get("title", instance.title)
#         instance.content = validate_data.get("content", instance.content)
#         instance.time_create = validate_data.get("time_create", instance.time_create)
#         instance.time_update = validate_data.get("time_update", instance.time_update)
#         instance.is_published = validate_data.get("is_published", instance.is_published)
#         instance.cat_id = validate_data.get("cat_id", instance.cat_id)
#         instance.save()
#         return instance
#
#
#


# -----   НЕ ИСПОЛЬЗУЕМ   --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# простое создание обьекта
# class WomenModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content


# сериализация обьекта - функция преобразовывает созданные обьеткы класса WomenModel в json формат
# прописываме действия построчно, но сериализатор делает ето автоматически
# def encode():
#     model = WomenModel("Sana", "OlEGOV")
#     # model_sr хранит внери себя обьект сериализации
#     model_sr = WomenSerializer(model)
#     # возвращает просто словарь со значениями   {'title': 'Sana', 'content': 'OlEGOV'}
#     print(model_sr.data, type(model_sr.data), sep="\n")
#     # переводим обьект сериализации в json строку
#     json = JSONRenderer().render(model_sr.data)
#     # возвращает байтовую строку json , которую можна отдавать пользователю   b'{"title":"Sana","content":"OlEGOV"}'
#     print(json)


# десериализация обьекта - преобразование json строки в обьект класса WomenModel
# прописываме действия построчно, но сериализатор делает ето автоматически
# def decode():
#     # берем байтовую json строку
#     stream = io.BytesIO(b'{"title":"Sana","content":"OlEGOV"}')
#     data = JSONParser().parse(stream=stream)
#     # делаем обьект сериализации
#     serializers = WomenSerializer(data=data)
#     # проверка коректности обьекта сериализации
#     serializers.is_valid()
#     # возвращает уже готовый обьект, который был до сериализации
#     print(serializers.validated_data)
