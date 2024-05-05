// static/js/modals/modals.js
var $ = jQuery.noConflict();

function AbrirModalEliminacion(url) {
    $('#deleteModalContent').load(url, function() {
        $('#deleteModal').modal('show');
    });
}

function AbrirModalEdicion(url, productId) {
    $('#edicionModal' + productId + ' .modal-body').load(url, function() {
        $('#edicionModal' + productId).modal('show');
    });
}

function AbrirModalAgregar() {
    $('#agregarProductoModal').load("{% url 'agregar_producto' %}", function() {
        $('#agregarProductoModal').modal('show');
    });
}

function guardarCambios(productId) {
    $('#edicionModal').modal('hide');
    $('#productTable').load(document.URL +  ' #productTable'); // Reload the table
}

$(document).ready(function() {
    // Evento para abrir el modal de modificación al hacer clic en el botón "Modificar"
    $('.btn-info').click(function() {
        var url = $(this).data('url');
        var productId = $(this).closest('tr').find('td:first').text(); // Obtener el Id_producto de la fila actual
        AbrirModalEdicion(url, productId);
    });

    // Evento para abrir el modal de agregar producto al hacer clic en el botón "Agregar Producto"
    $('.btn-primary').click(function() {
        AbrirModalAgregar();
    });
});