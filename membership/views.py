from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegistrationForm, UserProfileForm
from django.contrib.auth.models import User
from .models import UserProfile

def index(request):
    return render(request, 'membership/index.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/membership/login')
    else:
        form = RegistrationForm()

    return render(request, 'membership/signup.html', {'form': form})

def profile(request):
    args = {'user': request.user}
    return render(request, 'membership/profile.html', args)

def update_profile(request):
    id = UserProfile.objects.get(user=request.user.id)

    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, instance=id)
        if form.is_valid():
            form.save()
            return redirect('/membership/profile')
    else:
        form = UserProfileForm(instance=id)

    return render(request, 'membership/profile_update.html', {
        'form': form,
        'id' : id,
    })
