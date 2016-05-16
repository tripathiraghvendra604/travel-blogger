from django import forms
from .models import Post


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.Field(label='Password', widget=forms.PasswordInput())

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'content'
        ]