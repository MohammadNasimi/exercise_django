import imp
from sre_constants import SUCCESS
from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm
from accounts.forms import CustomUserCreationForm
# Create your views here.
from django.views.generic import CreateView ,TemplateView
from django.urls import reverse_lazy
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')
    
    
# from django.conf import settings
# User = settings.AUTH_USER_MODEL
class homePageView(TemplateView):
    template_name = 'home_user.html'