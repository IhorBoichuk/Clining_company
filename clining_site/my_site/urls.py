from django.urls import path

from . import views


urlpatterns = [
    path('', views.IndexTemplateView.as_view(), name='home'),
    path('service/', views.ServiceTemplateView.as_view(), name='service'),
    path('contacts/', views.ContactCreateView.as_view(), name='contacts')
    
]