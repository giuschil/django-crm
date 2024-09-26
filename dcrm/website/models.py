# website/models.py

from django.db import models

class WebsiteUser(models.Model):
    # Definisci i campi che corrispondono alle colonne della tua tabella
    id = models.AutoField(primary_key=True)  # Se la tua tabella ha un campo ID auto-incrementale
    name = models.CharField(max_length=255)  # Adatta il tipo e la lunghezza a seconda del tuo schema
    email = models.EmailField()
    role = models.CharField(max_length=255)
    city = models.CharField(max_length=255, blank=True, null=True)
    
    class Meta:
        db_table = 'website_user'  # Specifica il nome della tabella nel database

    def __str__(self):
        return self.name
