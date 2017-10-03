from django.conf.urls import url, include
from rest_framework import routers

from api import views
from api.views import CategoryViewSet, NewsList, RetrieveNews

router = routers.SimpleRouter ()
router.register (r'categories', CategoryViewSet)

urlpatterns = [
    url (r'^$', views.test),
    url (r'^news$', NewsList.as_view ()),
    url (r'^news/(?P<pk>[\d]+)$', RetrieveNews.as_view ()),
    url (r'^media/', include ('api.media.urls'))
]

urlpatterns += router.urls
