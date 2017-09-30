from rest_framework.serializers import ModelSerializer

from core.models import News, Category


class NewsSerializer (ModelSerializer):
    class Meta:
        model  = News
        fields = '__all__'


class CategorySerializer (ModelSerializer):
    class Meta:
        model  = Category
        fields = '__all__'
