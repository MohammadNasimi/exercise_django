from django.shortcuts import render
from django.views.generic import ListView ,DetailView
from django.views.generic.edit import UpdateView, DeleteView,CreateView
# Create your views here.
from django.urls import reverse_lazy
from blog.models import blog
class blogListView(ListView):
    model = blog
    template_name = 'blog/listview_blog.html'
    
    
class blogDetailView(DetailView):
    model = blog
    template_name = 'blog/detailblog.html'
    context_object_name = 'Detail_post'
    
class blogcreateview(CreateView):
    model = blog
    template_name = 'blog/create_blog.html'
    fields = [ 'title','author','body']
    
class blogUpdateView(UpdateView): 
    model = blog
    template_name = 'blog/updateblog.html'
    fields = ['title', 'body']

class blogDeleteView(DeleteView):
    model =blog
    template_name = 'blog/deleteblog.html'
    success_url = reverse_lazy('bloglist')