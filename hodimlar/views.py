from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import UserLoginForm
User = get_user_model()

@login_required
def profileView(request):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)
        print(user)
        return render(request, 'profile.html', {'user': user})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = UserLoginForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is None:
            try:
                user = User.objects.filter(username=username)
                user = authenticate(request, username=user.username, password=password)
            except User.DoesNotExist:
                user = None

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', context={'form': form, 'error': 'Parol yoki username xato kiritlgan'})
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})


def logoutView(request):
    logout(request)
    return redirect('hodimlar:login')
