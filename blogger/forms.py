from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.Field(label='Password', widget=forms.PasswordInput())
