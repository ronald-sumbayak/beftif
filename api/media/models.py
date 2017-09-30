import os
from base64 import b64encode

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from beftif import settings
from core.models import News


class HeaderImage (models.Model):
    news = models.OneToOneField (News)
    base64 = models.TextField ()
    
    def __str__ (self):
        return str (self.news)


@receiver (post_save, sender = News)
def generate_image_base64 (sender, instance, created, **kwargs):
    try:
        path = os.path.join (settings.MEDIA_ROOT, instance.header.path)
        with open (path, 'rb') as file:
            image, created = HeaderImage.objects.get_or_create (news = instance)
            image.base64 = b64encode (file.read ())
            image.save ()
        try:
            os.remove (path)
        except OSError:
            pass
        instance.header = 'header/%d.png' % instance.id
        instance.save ()
    except FileNotFoundError:
        pass
