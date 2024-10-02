from django.contrib import admin
from django.urls import path
from website import views  # Assicurati di importare dalle tue app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Cambia a seconda delle tue viste
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.user_login, name='login'),
    path('register/', views.user_register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('edit/<int:id>/', views.edit_user, name='edit_user'),
    path('delete/<int:id>/', views.delete_user, name='delete_user'),
    path('insert/', views.insert_user, name='insert_user')
]

