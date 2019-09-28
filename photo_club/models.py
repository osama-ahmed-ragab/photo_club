from django.conf import settings
from django.db import models
from django.utils import timezone

class Photo(models.Model):
    image = models.ImageField(upload_to=None, height_field=None, width_field=None)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    published_date = models.DateTimeField(blank=True, null=True)
    