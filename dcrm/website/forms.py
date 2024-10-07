from django import forms
from .models import WebsiteUser,WebsiteClient,Store
from django.contrib.auth.models import User  # Importa il modello User da django.contrib.auth.models


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class WebsiteUserForm(forms.ModelForm):
    class Meta:
        model = WebsiteUser
        fields = ['name', 'email', 'role', 'city', 'country']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'role': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
        }

class WebsiteClientForm(forms.ModelForm):
    class Meta:
        model = WebsiteClient
        fields = ['name', 'lastname', 'email', 'role', 'city', 'country','image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'lastname': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'role': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),

        }


class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ['nome_store', 'indirizzo', 'citta', 'latitudine', 'longitudine']
        widgets = {
            'nome_store': forms.TextInput(attrs={'class': 'form-control'}),
            'indirizzo': forms.TextInput(attrs={'class': 'form-control'}),
            'citta': forms.TextInput(attrs={'class': 'form-control'}),
            'latitudine': forms.TextInput(attrs={'class': 'form-control'}),
            'longitudine': forms.TextInput(attrs={'class': 'form-control'}),

        }