import json
from pathlib import Path
from .models import Hotel

def load_hotels_data():
    try:
        # Percorso assoluto del file JSON
        json_file_path = Path('/Users/giuseppe/Desktop/django-crm/dcrm/hotels_data_all.json')
        print(f"Loading data from {json_file_path}")
        
        with open(json_file_path, 'r') as file:
            hotels_data = json.load(file)
        
        for hotel_data in hotels_data:
            print(f"Creating hotel: {hotel_data['name']}")
            Hotel.objects.using('mongodb').create(
                name=hotel_data['name'],
                address=hotel_data['address'],
                latitude=hotel_data['geodata']['latitude'],
                longitude=hotel_data['geodata']['longitude'],
                link=hotel_data['link'],
                img=hotel_data['img']
            )
        print("Data loaded successfully")
    except Exception as e:
        print(f"Error: {e}")