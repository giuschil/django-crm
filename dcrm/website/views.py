# website/views.py

from django.shortcuts import render
from .models import WebsiteUser

def home(request):
    users = WebsiteUser.objects.all()
    return render(request, 'home.html', {'users': users})
