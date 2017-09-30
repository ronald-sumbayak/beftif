from rest_framework.viewsets import ModelViewSet

from api.serializers import CategorySerializer, NewsSerializer
from core.models import Category, News


class NewsViewSet (ModelViewSet):
    serializer_class = NewsSerializer
    queryset = News.objects.all ()


class CategoryViewSet (ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all ()
