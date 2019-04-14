from django import forms
from .models import Post2

class PostForm(forms.ModelForm) :
    class Meta :
        model = Post2
        fields = {'title', 'text', 'author', }
