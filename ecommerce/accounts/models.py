from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class MyUser(User):

    is_customer = models.BooleanField('Is Customer', default=False)
    is_seller = models.BooleanField('Is Seller', default=False)

    def __str__(self):
        return self.username
