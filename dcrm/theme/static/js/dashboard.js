document.addEventListener('DOMContentLoaded', function () {
    // Inizializza DataTables
    $('#clients-table').DataTable();

    // Gestione del modal di eliminazione
    var deleteModal = document.getElementById('deleteModal');
    deleteModal.addEventListener('show.bs.modal', function (event) {
        var button = event.relatedTarget; // Button that triggered the modal
        var userId = button.getAttribute('data-id'); // Extract info from data-* attributes
        var userIdInput = document.getElementById('user_id');
        userIdInput.value = userId; // Set the user ID in the hidden input field
        var deleteForm = document.getElementById('deleteForm');
        deleteForm.action = deleteForm.action.replace('0', userId); // Update form action with user ID
    });
});