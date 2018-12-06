from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import MyUser


class MyUserCreateForm(UserCreationForm):

    class Meta:
        model = MyUser
        fields = ('username', 'first_name', 'last_name', 'email', 'is_customer', 'is_seller', 'password1', 'password2')

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['is_seller'].widget = forms.RadioSelect()
    #     self.fields['is_customer'].widget = forms.RadioSelect()
