from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=64)
    manufacturer = models.CharField(max_length=128)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    photo = models.ImageField(upload_to='', max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

