from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Photo

def photo_list(request):
     posts = Photo.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
     return render(request, 'photo_club/photo_list.html',{'posts' : posts})

def photo_detail(request,pk):
     post = get_object_or_404(Photo, pk=pk)
     return render(request,'photo_club/photo_detail.html', {'post': post})