# Generated by Django 4.2 on 2023-04-26 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_products_image_products_product_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='youtube',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('videoid', models.CharField(max_length=50)),
            ],
        ),
    ]