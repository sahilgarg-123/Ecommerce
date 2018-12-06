from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from accounts.forms import MyUserCreateForm

# Create your views here.


class Signup(CreateView):
    form_class = MyUserCreateForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('login')
