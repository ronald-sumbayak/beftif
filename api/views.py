from django.http import HttpResponse, JsonResponse
from rest_framework.generics import ListAPIView, RetrieveAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api.serializers import CategorySerializer, NewsSerializer
from core.models import Category, News


def test (request):
    return JsonResponse ({"version": "v.0.0.2"})


class NewsList (ListAPIView):
    serializer_class = NewsSerializer
    
    def get_queryset (self):
        params = {k:self.request.query_params[k] for k in self.request.query_params.keys ()}
        queryset = News.objects.all ()
        if params.get ('ordering'):
            queryset = queryset.order_by (params['ordering'])
            params.pop ('ordering', None)
        return queryset.filter (**params)


class RetrieveNews (RetrieveAPIView):
    serializer_class = NewsSerializer
    
    def get_object (self):
        obj = get_object_or_404 (News, pk = self.kwargs['pk'])
        obj.popularity.visit_count += 1
        obj.save ()
        return obj


class CategoryViewSet (ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all ()
    
    def get_queryset (self):
        return Category.objects.filter (name__in = News.objects.all ().values_list ('category__name', flat = True).distinct ())
