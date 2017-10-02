import os
from base64 import b64encode
from datetime import timedelta, datetime, timezone

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from beftif import settings
from core.models import News


class HeaderImage (models.Model):
    news   = models.OneToOneField (News)
    base64 = models.TextField ()
    
    def __str__ (self):
        return str (self.news)


class Popularity (models.Model):
    news        = models.OneToOneField (News)
    visit_count = models.IntegerField (default = 0)
    _popularity = models.IntegerField (default = 0)
    
    @property
    def popularity (self):
        created_at = self.news.created_at
        now = datetime.now (timezone.utc)
        monday1 = (created_at - timedelta (days = created_at.weekday ()))
        monday2 = (now - timedelta (days = now.weekday ()))
        week_diff = int ((monday2 - monday1).days / 7)
        pop = self.visit_count - (week_diff * 50)
        if pop != self._popularity:
            self._popularity = pop
            self.save ()
        return pop
    
    def __str__ (self):
        return str (self.news)


@receiver (post_save, sender = News)
def generate_news_related_media (sender, instance, created, **kwargs):
    if created:
        Popularity.objects.create (news = instance)
    
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
