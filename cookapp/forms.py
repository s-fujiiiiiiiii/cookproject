from django import forms
from .models import BlogPost
from taggit.forms import TagWidget

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'material', 'content', 'image1']

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'material', 'content', 'image1', 'tags']
        widgets = {
            'tags': TagWidget(),
        }