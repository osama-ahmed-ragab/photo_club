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
    title = models.CharField(max_length=100)
    published_date = models.DateTimeField(blank=True, null=True)
    tags = models.ManyToManyField(Tag)
    
    def __str__(self):
        return self.title
    