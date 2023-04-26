from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.
class Contact(models.Model):
    email = models.EmailField(max_length=254)
    subject = models.CharField( max_length=50)
    message = models.TextField()


class products(models.Model):
    product_name = models.CharField( max_length=50)
    price = models.PositiveIntegerField()
    product_img = CloudinaryField('plants')

class youtube(models.Model):
    videoid = models.CharField( max_length=50)