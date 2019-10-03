from django.contrib import admin
from .models import Photo, Comment,Tag

admin.site.register(Photo)
admin.site.register(Tag)
admin.site.register(Comment)