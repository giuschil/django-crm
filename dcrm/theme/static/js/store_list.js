document.addEventListener('DOMContentLoaded', function () {
    var deleteModal = document.getElementById('deleteModal');
    deleteModal.addEventListener('show.bs.modal', function (event) {
        var button = event.relatedTarget;
        var storeId = button.getAttribute('data-id');
        var deleteForm = document.getElementById('deleteForm');
        var storeIdInput = deleteForm.querySelector('#store_id');
        storeIdInput.value = storeId;
        deleteForm.action = deleteForm.action.replace('0', storeId);
    });
});