from django.dispatch import receiver
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Contact
from .services import main


@receiver(post_save)
def post_save_contact(sender=Contact, **kwargs):
    my_obj = Contact.objects.last()
    context = {}
    context['name'] = my_obj.name
    context['contact_info'] = my_obj.phone
    context['message'] = my_obj.message    
    main(context)

