import csv
from pymongo import MongoClient

# URI di connessione al cluster MongoDB Atlas
uri = "mongodb+srv://giusschillaci:4eym87kCSADBpqiU@giuschil-cluster0.s29hm.mongodb.net/giuschil-hotel?retryWrites=true&w=majority"

# Crea un client MongoDB
client = MongoClient(uri)

# Testa la connessione e scarica i dati
try:
    # Ottieni il database
    db = client['giuschil-hotel']
    # Ottieni la collezione
    collection = db['hotel']
    
    # Scarica tutti i documenti dalla collezione
    data = list(collection.find())
    
    # Estrai i campi dei documenti
    if data:
        keys = data[0].keys()
        
        # Salva i dati in un file CSV
        with open('hotel_data.csv', 'w', newline='') as output_file:
            dict_writer = csv.DictWriter(output_file, fieldnames=keys)
            dict_writer.writeheader()
            dict_writer.writerows(data)
        
        print("Dati scaricati e salvati in hotel_data.csv con successo!")
    else:
        print("Nessun dato trovato nella collezione.")
except Exception as e:
    print("Errore di connessione o di download dei dati:", e)
finally:
    # Chiudi la connessione
    client.close()