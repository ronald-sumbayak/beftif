from django.db import models
from django.utils.translation import ugettext_lazy


class Category (models.Model):
    name = models.CharField (max_length = 16, unique = True)
    
    def __str__ (self):
        return self.name
    
    class Meta:
        verbose_name_plural = ugettext_lazy ('categories')
        ordering = ['name']


class News (models.Model):
    title      = models.CharField (max_length = 64)
    header     = models.ImageField ('header')
    content    = models.TextField ()
    category   = models.ForeignKey (Category)
    created_at = models.DateTimeField (auto_now_add = True)
    
    def __str__ (self):
        return self.title
    
    class Meta:
        verbose_name_plural = ugettext_lazy ('news')
        ordering = ['-created_at']
