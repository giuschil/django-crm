from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import WebsiteUser
from .forms import WebsiteUserForm

def home(request):
    return render(request, 'home.html')

@login_required
def dashboard(request):
    users = WebsiteUser.objects.all()
    return render(request, 'dashboard.html', {'users': users})

@login_required
def edit_user(request, id):
    user = get_object_or_404(WebsiteUser, id=id)
    if request.method == 'POST':
        form = WebsiteUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = WebsiteUserForm(instance=user)
    return render(request, 'edit_user.html', {'form': form})

@login_required
def delete_user(request, id):
    user = get_object_or_404(WebsiteUser, id=id)
    if request.method == 'POST':
        user.delete()
        next_url = request.POST.get('next', reverse('home'))
        return redirect(next_url)
    return redirect('home')

@login_required
def insert_user(request):
    if request.method == 'POST':
        form = WebsiteUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = WebsiteUserForm()
    return render(request, 'insert_user.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('home')

def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})