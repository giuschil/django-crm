from django.contrib import admin
from .models import WebsiteUser, WebsiteClient, Store, Hotel

# Registra i modelli
admin.site.register(WebsiteUser)
admin.site.register(WebsiteClient)
admin.site.register(Store)
admin.site.register(Hotel)

@admin.register(WebsiteClient)
class WebsiteClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'lastname', 'email', 'role', 'city', 'country')
    search_fields = ('name', 'lastname', 'email', 'role', 'city', 'country')


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('nome_store', 'indirizzo', 'citta', 'latitudine', 'longitudine')  # Aggiungi i campi che vuoi visualizzare nella lista
    search_fields = ('nome_store', 'citta')  # Aggiungi i campi per la ricerca
    list_filter = ('citta',)  # Aggiungi i campi per i filtri laterali