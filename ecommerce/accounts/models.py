from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class MyUser(User):

    is_customer = models.BooleanField('customer status', default=False)
    is_seller = models.BooleanField('seller status', default=False)

    def __str__(self):
        return self.username
