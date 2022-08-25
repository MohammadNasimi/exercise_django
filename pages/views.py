from django.shortcuts import render
from django.views.generic import TemplateView ,ListView,DetailView,CreateView ,UpdateView,DeleteView
from blog.models import blog
# Create your views here.
# from django.http import HttpResponse
# def homePageView(request):
#     return HttpResponse('Hello, World!')
from django.urls import reverse_lazy
class homePageView(ListView):
    model = blog
    template_name = 'pages/home.html'
    context_object_name = 'all_posts_list'

class aboutpageview(TemplateView):
    template_name = 'pages/about.html'
    
class blogDetail(DetailView):
    model = blog
    template_name = 'pages/detail.html'
    context_object_name = 'Detail_post'
    
class blogcreate(CreateView):
    model = blog
    template_name = 'pages/create.html'
    fields = [ 'title','author','body']
    
class BlogUpdateView(UpdateView): 
    model = blog
    template_name = 'pages/update.html'
    fields = ['title', 'body']

class blogdeleteView(DeleteView):
    model =blog
    template_name = 'pages/delete.html'
    success_url = reverse_lazy('home')