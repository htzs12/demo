from django import forms
from .models import UserProfile,Image


class RegisterForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ['username', 'password', 'birthday','mobile','width','height','image']


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image']