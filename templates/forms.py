from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=100)
    confirm = forms.CharField(max_length=100)

    def save(self):
        data = self.cleaned_data
        user = User(username=data['email'], email=data['email'], password=data['password'])
        user.save()
        