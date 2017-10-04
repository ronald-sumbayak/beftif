from django.apps import AppConfig


class MediaConfig (AppConfig):
    name = 'api.media'
    
    def ready (self):
        from . import signals
