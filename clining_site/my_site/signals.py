from django.shortcuts import redirect
from django.dispatch import receiver
from clining_site import settings
from .models import Contact

from django.db.models.signals import post_save
from django.dispatch import receiver

import asyncio
from .services import main


@receiver(post_save)
def post_save_contact(sender=Contact, **kwargs):
    my_obj = Contact.objects.last()
    if my_obj.name:
        print(my_obj.name)
        asyncio.run(main())

