from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Photo

def photo_list(request):
    return render(request, 'photo_club/base.html')