from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
# from django.http import HttpResponse
# def homePageView(request):
#     return HttpResponse('Hello, World!')

class homePageView(TemplateView):
    template_name = 'pages/home.html'

class aboutpageview(TemplateView):
    template_name = 'pages/about.html'
    