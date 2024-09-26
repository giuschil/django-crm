# website/views.py

from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

from .models import WebsiteUser

def home(request):
    users = WebsiteUser.objects.all()
    return render(request, 'home.html', {'users': users})

def login_user(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login effettuato con successo')
            return redirect('home')
        else:
            messages.error(request, 'Email o password non validi')
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    messages.success(request, 'Logout effettuato con successo')
    return redirect('login')