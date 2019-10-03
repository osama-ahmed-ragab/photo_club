from django import forms
from .models import Photo, Comment,Tag

class PhotoForm(forms.ModelForm):

    class Meta:
        model = Photo
        fields = ('title','image',)
        
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)
        
class TagForm(forms.ModelForm):
    
    class Meta:
        model = Tag
        fields = ('name',)
