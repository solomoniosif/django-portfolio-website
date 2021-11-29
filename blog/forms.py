from django import forms

from .models import Post, PostImage
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('published_on', 'slug',)
        widgets = {
            'title': forms.TextInput(),
            'text': SummernoteWidget(),
        }


class PostImageForm(forms.ModelForm):
    class Meta:
        model = PostImage
        fields = ['image', ]
        widgets = {
            'image': forms.FileInput()
        }
