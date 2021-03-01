from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from Tracker.core_forms.signup_form import SignUpForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, f'Registration was successful for {username}')
            return redirect('landing')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})
