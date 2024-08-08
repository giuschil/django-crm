from django.contrib import admin
from django.urls import path
from website import views  # Assicurati di importare dalle tue app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Cambia a seconda delle tue viste
]
