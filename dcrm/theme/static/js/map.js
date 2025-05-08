document.addEventListener('DOMContentLoaded', function() {
    var map = L.map('map').setView([41.9028, 12.4964], 5); // Centra la mappa su Roma, Italia

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    // Dati degli store passati dal template
    var storesDataElement = document.getElementById('stores-data');
    if (storesDataElement) {
        var stores = JSON.parse(storesDataElement.textContent);

        stores.forEach(function(store) {
            L.marker([store.latitudine, store.longitudine]).addTo(map)
                .bindPopup('<b>' + store.nome_store + '</b><br>' + store.indirizzo + '<br>' + store.citta);
        });
    } else {
        console.error('Elemento stores-data non trovato.');
    }
});