from django.apps import AppConfig


class WishesConfig(AppConfig):
    name = 'wishes'

    def ready(self):
        import wishes.signals
