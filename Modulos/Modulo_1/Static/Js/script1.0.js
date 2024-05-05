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

$(document).ready(function() {
    // Verifica si hay un mensaje de éxito y muestra SweetAlert
    {% if messages %}
        {% for message in messages %}
            {% if message.tags == 'success' %}
                Swal.fire("¡Éxito!", "{{ message }}", "success");
            {% elif message.tags == 'error' %}
                Swal.fire("Error", "{{ message }}", "error");
            {% endif %}
        {% endfor %}
    {% endif %}

    // Resto de tu código JavaScript...
});

function eliminarProducto(Id_producto) {
    // Realiza una solicitud AJAX para eliminar el producto
    $.ajax({
        url: `/eliminar_producto/${Id_producto}`,
        type: 'POST',
        data: {
            csrfmiddlewaretoken: '{{ csrf_token }}'
        },
        success: function (data) {
            // Muestra SweetAlert con el mensaje
            Swal.fire(data.title, data.text, data.icon);
            // Recarga la página o realiza alguna otra acción si es necesario
            setTimeout(function () {
                location.reload();
            }, 1500); // Recarga la página después de 1.5 segundos
        },
        error: function (xhr, status, error) {
            // Maneja errores si es necesario
            console.error(xhr.responseText);
        }
    });
}

$(document).ready(function() {
    // Evento para confirmar la eliminación del producto al hacer clic en el botón "Eliminar"
    $('.btn-danger').click(function() {
        var Id_producto = $(this).closest('tr').find('td:first').text(); // Obtener el Id_producto de la fila actual
        Swal.fire({
            title: '¿Estás seguro?',
            text: 'Esta acción no se puede deshacer.',
            icon: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#d33',
            cancelButtonColor: '#3085d6',
            confirmButtonText: 'Sí, eliminar'
        }).then((result) => {
            if (result.isConfirmed) {
                eliminarProducto(Id_producto); // Llama a la función para eliminar el producto
            }
        });
    });
});