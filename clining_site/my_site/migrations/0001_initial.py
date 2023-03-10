# Generated by Django 4.1.7 on 2023-02-14 23:18

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Імя_замовника')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('message', models.TextField(max_length=250, verbose_name='Текст_замовника')),
                ('date_created', models.DateField(auto_now_add=True, verbose_name='Дата_замовлення')),
            ],
        ),
    ]
