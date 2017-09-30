from django.conf.urls import url, include
from rest_framework import routers

from api.views import NewsViewSet, CategoryViewSet

router = routers.SimpleRouter()
router.register (r'news', NewsViewSet)
router.register (r'categories', CategoryViewSet)

urlpatterns = [
    url (r'^media/', include ('api.media.urls'))
]

urlpatterns += router.urls
