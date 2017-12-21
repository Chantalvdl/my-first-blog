from django import forms

from .models import Post, Todo

class PostForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = ('item', 'comments','deadline', )
