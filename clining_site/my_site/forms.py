from django.forms import ModelForm, Textarea, TextInput

from .models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'phone', 'message']
        widgets = {
            'name': TextInput(attrs={
                'placeholder': 'Please enter your name.',
                'size':50
                }),
            
            'phone': Textarea(attrs={
                'placeholder': 'Here you can leave your phone number/contact',
                'rows':2,
                'cols':61,
                }),
            
            'message': Textarea(attrs={
                'placeholder': 'Here you can leave your message, thank you.',
                'rows':14,
                'cols':61,
                })
        }