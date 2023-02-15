from django.views.generic.edit import CreateView
from django.views.generic import TemplateView

from django.urls import reverse_lazy

from .forms import ContactForm
from .models import Contact






# from django.views.generic import DetailView
# from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect

class IndexTemplateView(TemplateView):
    template_name = 'my_site/index.html'
    

class ServiceTemplateView(TemplateView):
    template_name = 'my_site/service.html'
    

class ContactCreateView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'my_site/contacts.html'
    success_url = reverse_lazy('home')
    
    