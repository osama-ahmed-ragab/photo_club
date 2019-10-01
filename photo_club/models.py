from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.utils import timezone


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name

class Photo(models.Model):
    image = models.ImageField(upload_to='images', height_field=None, width_field=None)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length =100, blank=True)
    published_date = models.DateTimeField(blank=True, null=True)
    #tags = models.ManyToManyField(Tag,required = False ,blank=True, null=True)
    
    def approved_comments(self):
        return self.comments.filter(approved_comment=True)
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey('photo_club.Photo', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()
        
    def __str__(self):
        return self.text
    