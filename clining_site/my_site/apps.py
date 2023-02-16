from django.apps import AppConfig


class MySiteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'my_site'

    def ready(self):
        # import signal handlers
        import my_site.signals
        my_site.signals.post_save.connect(my_site.signals.post_save_contact, sender=self)