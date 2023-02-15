from django.apps import AppConfig
# from django.core.signals import setting_changed

class MySiteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'my_site'

    # def ready(self):
    #     setting_changed.connect(my_callback)
        
        
        
    # def ready(self):
    #     # import signal handlers
    #     import my_site.signals
    #     my_site.signals.connect(my_site.signals.post_save_contact, sender=self)