import imp
from django.db import models
from accounts.models import CustomerUser
from django.urls import reverse
# Create your models here.
from django.db import models
class blog(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        CustomerUser,
        on_delete=models.CASCADE,
        )
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self): 
        return reverse('detail', args=[str(self.id)])
    
class Comment(models.Model): 
    blog = models.ForeignKey(blog, on_delete=models.CASCADE,related_name='comments')
    comment = models.CharField(max_length=140)
    author = models.ForeignKey(CustomerUser,on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.comment
    def get_absolute_url(self):
        return reverse('bloglist')