from website import views  # Assicurati di importare dalle tue app
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('edit_user/<int:id>/', views.edit_user, name='edit_user'),
    path('delete_user/<int:id>/', views.delete_user, name='delete_user'),
    path('insert_user/', views.insert_user, name='insert_user'),
    path('edit_client/<int:id>/', views.edit_client, name='edit_client'),
    path('delete_client/<int:id>/', views.delete_client, name='delete_client'),
    path('insert_client/', views.insert_client, name='insert_client'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.user_register, name='register'),
    path('image_upload/', views.image_upload, name='upload'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
