from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2',
            'email',
            'first_name',
            'last_name',
        ]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

class UserProfileForm(ModelForm):

    class Meta:
        model = UserProfile
        fields = [
            'address',
            'gender',
            'city',
            'postal_code',
            'social_number',
            'profession',
        ]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.address = self.cleaned_data['address']
        user.gender = self.cleaned_data['gender']
        if commit:
            user.save()
