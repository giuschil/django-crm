document.addEventListener('DOMContentLoaded', function() {
    console.log('DOM completamente caricato e analizzato');
    
    const updateImageButton = document.getElementById('update-image-btn');
    const imageInput = document.getElementById('id_image');
    const imagePreviewContainer = document.getElementById('image-preview-container');
    const imagePreview = document.getElementById('image-preview');

    if (updateImageButton) {
        console.log('Trovato update-image-btn');
    } else {
        console.error('Elemento non trovato: update-image-btn');
    }

    if (imageInput) {
        console.log('Trovato id_image');
    } else {
        console.error('Elemento non trovato: id_image');
    }

    if (updateImageButton && imageInput) {
        updateImageButton.addEventListener('click', function() {
            console.log('Pulsante Aggiorna Immagine cliccato');
            imageInput.click();
        });

        imageInput.addEventListener('change', function(event) {
            const file = event.target.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = function(e) {
                    imagePreview.src = e.target.result;
                    imagePreviewContainer.style.display = 'block';
                };
                reader.readAsDataURL(file);
            }
        });
    }
});