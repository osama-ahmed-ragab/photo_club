from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView 
from .models import Photo, Comment
from .forms import PhotoForm, CommentForm

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

def photo_new(request):
    if request.method == "POST":
        form = PhotoForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.owner = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('photo_detail', pk=post.pk)
    else:
        form = PhotoForm()
    return render(request, 'photo_club/photo_edit.html', {'form': form})


def add_comment_to_photo(request, pk):
    post = get_object_or_404(Photo, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('photo_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'photo_club/add_comment_to_photo.html', {'form': form})


def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('photo_detail', pk=comment.post.pk)

def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('photo_detail', pk=comment.post.pk)
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

def add_tag(request,pk):
    post = get_object_or_404(Photo, pk=pk)
    if request.method == "POST":
        form = TagForm(request.POST)
        if form.is_valid():
            tg = form.save()
            post.tags.add(tg) 
            post.save()
            return redirect('photo_detail', pk=post.pk)
    else:
        form = TagForm()
    return render(request, 'photo_club/add_tag.html', {'form': form})
'''