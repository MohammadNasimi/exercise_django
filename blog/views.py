from django.shortcuts import render
from django.views.generic import ListView ,DetailView
from django.views.generic.edit import UpdateView, DeleteView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin ,UserPassesTestMixin
# Create your views here.
from django.urls import reverse_lazy
from blog.models import blog
class blogListView(LoginRequiredMixin,ListView):
    model = blog
    template_name = 'blog/listview_blog.html'
    
    
class blogDetailView(LoginRequiredMixin,DetailView):
    model = blog
    template_name = 'blog/detailblog.html'
    context_object_name = 'Detail_post'
    
class blogcreateview(LoginRequiredMixin,CreateView):
    model = blog
    template_name = 'blog/create_blog.html'
    fields = [ 'title','body']
    
    def form_valid(self, form):
        print(self.request.user)
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class blogUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView): 
    model = blog
    template_name = 'blog/updateblog.html'
    fields = ['title', 'body']
    def test_func(self): 
        obj = self.get_object()
        return obj.author == self.request.user

class blogDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model =blog
    template_name = 'blog/deleteblog.html'
    success_url = reverse_lazy('bloglist')
    def test_func(self): 
        obj = self.get_object()
        return obj.author == self.request.user