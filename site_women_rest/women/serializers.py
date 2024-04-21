# В етом файле храняться сериализаторы для наших представлений в views.py
from .models import Women, Category
from rest_framework import serializers


# ModelSerializer работает только с нашими моделями
class WomenSerializer(serializers.ModelSerializer):
    class Meta:
        # связываемся с нашей моделью Women
        model = Women
        # указываем поля нашей модели, которые попадут в сериализацию и будут отправляються обратно пользователю
        # ети поля будут отображаться при сахождении в API сайта
        fields = ("title", "cat")
