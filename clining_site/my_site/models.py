from django.db import models
from django.urls import reverse



class Contact(models.Model):
    name = models.CharField('Імя_замовника', max_length=50)
    phone = models.CharField('Телефон', null=True, blank=True, max_length=50)
    message = models.TextField('Текст_замовника', max_length=250, null=True)
    date_created = models.DateField('Дата_замовлення', auto_now_add=True)
    
    def get_absolute_url(self):
        return reverse("home", kwargs={"pk": self.pk})
    
    def __str__(self):
        return self.name