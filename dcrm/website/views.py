from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import WebsiteClient
from .forms import WebsiteClientForm
from django.db.models import Sum



from .models import WebsiteUser, WebsiteClient
from .forms import WebsiteUserForm, WebsiteClientForm, UserForm
from django.core.files.storage import FileSystemStorage


def home(request):
    return render(request, 'home.html')

@login_required
def image_upload(request):
    if request.method == 'POST' and request.FILES['image']:
        image = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        uploaded_file_url = fs.url(filename)
        return render(request, 'image_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'image_upload.html')

@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

@login_required
def dashboard(request):
    users = WebsiteUser.objects.all()
    clients = WebsiteClient.objects.all()
    total_clients = WebsiteClient.objects.count()
    sum_clients = WebsiteClient.objects.aggregate(Sum('id'))['id__sum']
    return render(request, 'dashboard.html', {'users': users, 
                                              'clients': clients,
                                              'total_clients': total_clients,
                                              'sum_clients': sum_clients})

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

@login_required

def edit_client(request, id):
    client = get_object_or_404(WebsiteClient, id=id)
    if request.method == 'POST':
        form = WebsiteClientForm(request.POST, request.FILES, instance=client)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = WebsiteClientForm(instance=client)
    return render(request, 'edit_client.html', {'form': form})

@login_required
def delete_client(request, id):
    client = get_object_or_404(WebsiteClient, id=id)
    if request.method == 'POST':
        client.delete()
        next_url = request.POST.get('next', reverse('dashboard'))
        return redirect(next_url)
    return redirect('dashboard')

@login_required
def insert_client(request):
    if request.method == 'POST':
        form = WebsiteClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = WebsiteClientForm()
    return render(request, 'insert_client.html', {'form': form})

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