from django.conf.urls import url

from api.media import views

urlpatterns = [
    url (r'^header/(?P<id>[\d]+).png$', views.header_image)
]
