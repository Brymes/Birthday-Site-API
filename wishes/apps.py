from django.apps import AppConfig


class WishesConfig(AppConfig):
    name = 'wishes'

    def ready(self):
        from . import signals
