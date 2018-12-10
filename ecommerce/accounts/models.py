from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class MyUser(User):

    is_customer = models.BooleanField('Is Customer', default=False)
    is_seller = models.BooleanField('Is Seller', default=False)

    def __str__(self):
        return self.username


class MyUserAddress(models.Model):
    owner = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=128)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    street = models.CharField(max_length=128)
    building_num = models.PositiveIntegerField()
    flat_num = models.PositiveIntegerField()
    zip_code = models.CharField(max_length=16)
    city = models.CharField(max_length=128)

    def __str__(self):
        return self.owner.username + ' address'
