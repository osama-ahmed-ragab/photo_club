from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView 
from .models import Photo
from .forms import PhotoForm

def photo_list(request):
    posts = Photo.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'photo_club/photo_list.html',{'posts' : posts})

def photo_detail(request,pk):
    post = get_object_or_404(Photo, pk=pk)
    return render(request,'photo_club/photo_detail.html', {'post': post})


def photo_edit(request, pk):
    post = get_object_or_404(Photo, pk=pk)
    if request.method == "POST":
        form = PhotoForm(request.POST,request.FILES, instance=post)
        if form.is_valid():
            post.save()
            return redirect('photo_detail', pk=post.pk)
    else:
        form = PhotoForm(instance=post)
    return render (request, 'photo_club/photo_edit.html', {'form': form} )
'''
class photo_edit(UpdateView):
    model = Photo
    form_class = PhotoForm
    template_name = 'templates/photo_club/phot_edit.html'
    success_url = '/home/'
    pk_url_kwarg = 'post_pk'
    context_object_name = 'post'
    
     def form_valid(self, form):
        post = form.save(commit=False)
        post.updated_by = self.request.user
        post.updated_at = timezone.now()
        post.save()
        return render (request, 'photo_club/photo_edit.html', {'form': form} )
'''