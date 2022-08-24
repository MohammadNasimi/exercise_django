from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.db import models
class blog(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        )
    body = models.TextField()
    
    
    def __str__(self):
        return self.title