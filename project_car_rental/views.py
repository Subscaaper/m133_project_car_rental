from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from project_car_rental.forms import SignUpForm
from django.contrib import auth


@login_required()
def home(request):
    """
    home
    """
    return render(request, 'base_home/home.html')


def signup_view(request):
    """
    signUp
    param: user request
    returns: signup.html
    """
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
        else:
            form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def login_view(request):
    """
    login
    param: user request
    returns: login.html
    """
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    return render(request, 'registration/login.html')


def logout_view(request):
    """
    logout
    param: user request
    returns: logout.html
    """
    auth.logout(request)
    return render(request, 'registration/logout.html')
