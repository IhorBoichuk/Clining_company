from django.forms import ModelForm, Textarea, TextInput

from .models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={
                'placeholder': 'Please enter your name.',
                'class': 'form__input',
                
                }),
            
            'phone': TextInput(attrs={
                'placeholder': 'Here you can leave your phone number/contact',
                'class': 'form__input',
                
                }),
            
            'message': Textarea(attrs={
                'placeholder': 'Here you can leave your message, thank you.',
                'class': 'form__input',
                
                })
        }