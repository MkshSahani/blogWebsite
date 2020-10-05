from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):  # our post model.
    
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    author = models.ForeignKey(User,on_delete=models.PROTECT)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title # get the title for post.
    

