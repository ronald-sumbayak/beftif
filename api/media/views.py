from base64 import b64decode

from django.http import HttpResponse
from rest_framework.decorators import api_view

from api.media.models import HeaderImage


@api_view (['GET'])
def header_image (request, id):
    header = HeaderImage.objects.get (news_id = id)
    return HttpResponse (b64decode (header.base64), content_type = 'image/png')
