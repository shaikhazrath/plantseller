# Generated by Django 4.2 on 2023-04-23 20:30

import cloudinary.models
from django.db import migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_products_delete_subscribe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='image',
        ),
        migrations.AddField(
            model_name='products',
            name='product_img',
            field=cloudinary.models.CloudinaryField(default=django.utils.timezone.now, max_length=255, verbose_name='plants'),
            preserve_default=False,
        ),
    ]
