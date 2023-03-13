from django.views.generic.edit import CreateView
from django.views.generic import TemplateView

from django.urls import reverse_lazy

from .forms import ContactForm
from .models import Contact


class ContactCreateView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'my_site/contacts.html'
    success_url = reverse_lazy('home')
    
    