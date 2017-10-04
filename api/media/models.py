from datetime import datetime, timedelta, timezone

from django.db import models
from django.db.models.signals import post_save

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
