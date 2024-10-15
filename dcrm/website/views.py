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
from .forms import WebsiteUserForm, WebsiteClientForm, UserForm,StoreForm
from django.core.files.storage import FileSystemStorage
from .utils import get_coordinates
from .models import Store
from .models import Hotel
from django.core.serializers import serialize
from pymongo import MongoClient
from django.core.paginator import Paginator
from django.shortcuts import render

import json

def get_total_hotels():
    uri = "mongodb+srv://giusschillaci:4eym87kCSADBpqiU@giuschil-cluster0.s29hm.mongodb.net/giuschil-hotel?retryWrites=true&w=majority"
    client = MongoClient(uri)
    try:
        db = client['giuschil-hotel']
        collection = db['hotel']
        total_hotels = collection.count_documents({})
        return total_hotels
    except Exception as e:
        print("Errore di connessione a MongoDB:", e)
        return 0
    finally:
        client.close()


def home(request):
    return render(request, 'home.html')




@login_required
def hotels_list(request):
    # URI di connessione a MongoDB
    uri = "mongodb+srv://giusschillaci:4eym87kCSADBpqiU@giuschil-cluster0.s29hm.mongodb.net/giuschil-hotel?retryWrites=true&w=majority"

    # Crea un client MongoDB
    client = MongoClient(uri)

    # Testa la connessione e scarica i dati
    try:
        # Ottieni il database
        db = client['giuschil-hotel']
        # Ottieni la collezione
        collection = db['hotel']
        
        # Recupera tutti i documenti dalla collezione
        hotels = list(collection.find())
        
        # Converti ObjectId in stringhe
        for hotel in hotels:
            hotel['_id'] = str(hotel['_id'])
    except Exception as e:
        pass
    finally:
        # Chiudi la connessione
        client.close()

    # Paginazione
    paginator = Paginator(hotels, 6)  # Mostra 6 hotel per pagina
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Serializza i dati degli hotel della pagina corrente in JSON
    hotels_json = json.dumps(list(page_obj))

    return render(request, 'hotels_list.html', {'page_obj': page_obj, 'hotels_json': hotels_json})


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
    total_stores = Store.objects.count()
    total_hotels = get_total_hotels()  
    return render(request, 'dashboard.html', {'users': users, 
                                              'clients': clients,
                                              'total_clients': total_clients,
                                              'sum_clients': sum_clients, 
                                              'total_stores': total_stores,
                                              'total_hotels': total_hotels})

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

def add_store(request):
    if request.method == 'POST':
        nome_store = request.POST.get('nome_store')
        indirizzo = request.POST.get('indirizzo')
        citta = request.POST.get('citta')
        latitudine = request.POST.get('latitudine')
        longitudine = request.POST.get('longitudine')

        # Log di debug
        print(f"Nome Store: {nome_store}")
        print(f"Indirizzo: {indirizzo}")
        print(f"Città: {citta}")
        print(f"Latitudine: {latitudine}")
        print(f"Longitudine: {longitudine}")

        # Verifica che tutti i campi siano presenti
        if nome_store and indirizzo and citta and latitudine and longitudine:
            # Salva il nuovo store nel database
            Store.objects.create(
                nome_store=nome_store,
                indirizzo=indirizzo,
                citta=citta,
                latitudine=latitudine,
                longitudine=longitudine
            )
            return redirect('store_list')  # Assicurati che 'store_list' sia il nome corretto della tua vista
        else:
            # Gestisci il caso di campi mancanti
            return render(request, 'add_store.html', {'error': 'Tutti i campi sono obbligatori.'})
    
    return render(request, 'add_store.html')


@login_required
def delete_store(request, store_id):
    store = get_object_or_404(Store, id=store_id)
    if request.method == 'POST':
        store.delete()
        return redirect('store_list')
    return render(request, 'store_list.html')

@login_required
def edit_store(request, store_id):
    store = get_object_or_404(Store, id=store_id)
    if request.method == 'POST':
        form = StoreForm(request.POST, instance=store)
        if form.is_valid():
            form.save()
            return redirect('store_list')
    else:
        form = StoreForm(instance=store)
    return render(request, 'edit_store.html', {'form': form})


@login_required
def store_list(request):
    stores = Store.objects.all()
    store_data = [
        {
            'nome_store': store.nome_store,
            'indirizzo': store.indirizzo,
            'citta': store.citta,
            'latitudine': store.latitudine,
            'longitudine': store.longitudine
        }
        for store in stores
    ]
    # Log di debug
    #print(f"Store Data: {store_data}")
    return render(request, 'store_list.html', {'stores': stores, 'stores_json': json.dumps(store_data)})

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