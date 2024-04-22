# В етом файле храняться сериализаторы для наших представлений в views.py
from .models import Women, Category
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io

# простое создание обьекта
# class WomenModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content


# создание сериализатора для модели Women
# текущий сериализатор проверяет значения которые отправил клиент в POST запросе с указаными характеристиками
class WomenSerializer(serializers.Serializer):
    # все записанные поля беруться из нашей модели models.py
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField(default=True)
    cat_id = serializers.IntegerField()


# -----   НЕ ИСПОЛЬЗУЕМ   -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#
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


# ModelSerializer работает только с нашими моделями
# class WomenSerializer(serializers.ModelSerializer):
#     class Meta:
#         # связываемся с нашей моделью Women
#         model = Women
#         # указываем поля нашей модели, которые попадут в сериализацию и будут отправляються обратно пользователю
#         # ети поля будут отображаться при сахождении в API сайта
#         fields = ("title", "cat")
