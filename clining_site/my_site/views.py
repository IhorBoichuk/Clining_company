from django.shortcuts import render
from django.http import HttpRequest, HttpResponse




from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from .models import Contact
from django.urls import reverse_lazy

from .forms import ContactForm

# Create your views here.
def index(request):
    return render(request, 'my_site/index.html')


def service(request):
    return render(request, 'my_site/service.html')


class ContactCreateView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'my_site/contacts.html'
    success_url = reverse_lazy('home')