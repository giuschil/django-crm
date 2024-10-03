from django.contrib import admin
from .models import WebsiteUser,WebsiteClient

admin.site.register(WebsiteUser)


@admin.register(WebsiteClient)
class WebsiteClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'lastname', 'email', 'role', 'city', 'country')
    search_fields = ('name', 'lastname', 'email', 'role', 'city', 'country')