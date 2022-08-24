from django.shortcuts import render
from django.views.generic import TemplateView ,ListView
from posts.models import post
# Create your views here.
# from django.http import HttpResponse
# def homePageView(request):
#     return HttpResponse('Hello, World!')

class homePageView(ListView):
    model = post
    template_name = 'pages/home.html'
    context_object_name = 'all_posts_list'

class aboutpageview(TemplateView):
    template_name = 'pages/about.html'
    