from rest_framework.fields import ReadOnlyField
from rest_framework.serializers import ModelSerializer

from core.models import News, Category


class NewsSerializer (ModelSerializer):
    popularity = ReadOnlyField (source = 'popularity.popularity')
    category = ReadOnlyField (source = 'category.name')
    class Meta:
        model  = News
        fields = '__all__'


class CategorySerializer (ModelSerializer):
    class Meta:
        model  = Category
        fields = '__all__'
