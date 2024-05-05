from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from PIL import Image


class Colegio(models.Model):
    Codigo = models.CharField(max_length=10, unique=True)
    Nombre = models.CharField(max_length=100)
    Rector = models.CharField(max_length=100)
    # Otros campos que quieras agregar como dirección, teléfono, etc.

    def __str__(self):
        return self.Nombre

# Tabla para almacenar información del año lectivo
class Aniolectivo(models.Model):
    Codigo = models.CharField(max_length=10, primary_key=True)
    Nombre = models.CharField(max_length=100)
    Fecha_inicio = models.DateField()
    Fecha_fin = models.DateField()
    

    def __str__(self):
        return self.Nombre

# Tabla para almacenar información de los grados
class Grado(models.Model):
    Codigo = models.CharField(max_length=10, primary_key=True)
    Nombre = models.CharField(max_length=50)
    Aniolectivo = models.ForeignKey(Aniolectivo, on_delete=models.CASCADE, null=True, blank=True, verbose_name=_("Año lectivo"))
    def __str__(self):
        return self.Nombre

# Tabla para almacenar información sobre los estudiantess
class Estudiante(models.Model):
    Id_estudiante = models.CharField(max_length=8, primary_key=True)  # Identificador único del estudiante
    Colegio = models.ForeignKey(Colegio, on_delete=models.CASCADE)
    Apellido = models.CharField(max_length=35)  # Apellido del estudiante
    Nombres = models.CharField(max_length=35)  # Nombres del estudiante
    Genero = models.CharField(max_length=1, choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')])  # Género del estudiante
    Grado = models.ForeignKey(Grado, on_delete=models.CASCADE)
    Telefono = models.CharField(max_length=15)  # Teléfono del estudiante  
    Correo_electronico = models.EmailField(max_length=50)  # Correo electrónico del estudiante
    Direccion = models.CharField(max_length=50)  # Dirección del estudiante
    Activo = models.BooleanField(default=True)  # Estado de activación del estudiante
    Alergias = models.CharField(max_length=255, null=True, blank=True)  # Alergias del estudiante

    def __str__(self):
        return "{0}, {1}".format(self.Apellido, self.Nombres)

# Tabla para almacenar información sobre los profesores
class Profesor(models.Model):
    Id_profesor = models.CharField(max_length=8, primary_key=True)  # Identificador único del profesor
    Apellido_paterno = models.CharField(max_length=35)  # Apellido del profesor
    Apellido_materno = models.CharField(max_length=35)
    Nombres = models.CharField(max_length=35)  # Nombres del profesor
    Genero = models.CharField(max_length=1, choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')])  # Género del profesor
    Telefono = models.CharField(max_length=15)  # Teléfono del profesor
    Correo_electronico = models.EmailField(max_length=50)  # Correo electrónico del profesor
    Direccion = models.CharField(max_length=50)  # Dirección del profesor
    Activo = models.BooleanField(default=True)  # Estado de activación del profesor

    def __str__(self):
        return "{0}, {1}".format(self.Apellido_paterno, self.Nombres)

# Tabla para almacenar información sobre los empleados (incluidos administradores)
class Empleado(models.Model):
    Id_empleado = models.CharField(max_length=8, primary_key=True)  # Identificador único del empleado
    Apellido_paterno = models.CharField(max_length=35)  # Apellido del empleado
    Apellido_materno = models.CharField(max_length=35)  # Apellido del empleado
    Nombres = models.CharField(max_length=35)  # Nombres del empleado
    Genero = models.CharField(max_length=1, choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')])  # Género del empleado
    Cargo = models.CharField(max_length=15, choices=[('E', 'Empleado'), ('A', 'Administrador')])  # Cargo del empleado (puede ser empleado o administrador)
    Telefono = models.CharField(max_length=15)  # Número de teléfono del empleado
    Correo_electronico = models.EmailField(max_length=50)  # Dirección de correo electrónico del empleado
    Direccion = models.CharField(max_length=50)  # Dirección del empleado
    Activo = models.BooleanField(default=True)  # Estado de activación del empleado

    def __str__(self):
        return "{0}, {1}".format(self.Apellido_paterno, self.Nombres)

# Tabla para almacenar información sobre los proveedores de productos
class Proveedor(models.Model):
    Id_proveedor = models.CharField(max_length=8, primary_key=True)  # Identificador único del proveedor
    Nombre = models.CharField(max_length=50)  # Nombre del proveedor
    Ciudad = models.CharField(max_length=35)  # Ciudad del proveedor
    Direccion = models.CharField(max_length=50)  # Dirección del proveedor
    Telefono = models.CharField(max_length=15)  # Teléfono del proveedor
    Correo_electronico = models.EmailField(max_length=50)  # Correo electrónico del proveedor
    Contacto = models.CharField(max_length=35)  # Persona de contacto en el proveedor

    def __str__(self):
        return self.Nombre

# Tabla para almacenar información sobre los productos ofrecidos por los proveedores
class Producto(models.Model):
    Id_producto = models.CharField(max_length=8, primary_key=True)  # Identificador único del producto
    Proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)  # Proveedor del producto
    Imagen_Producto = models.ImageField(upload_to='Productos/', default='no_disponible.jpg')  # Aquí se establece el valor predeterminado #! Tengo que installar pillow en pypi para que tenga utilidad
    Nombre = models.CharField(max_length=50)  # Nombre del producto
    Stock = models.IntegerField()  # Stock del producto
    Precio = models.DecimalField(max_digits=10, decimal_places=2)  # Precio del producto
    Descripcion = models.CharField(max_length=255)  # Descripción del producto
    Fecha_vencimiento = models.DateField(null=True, blank=True)  # Fecha de vencimiento del producto (si aplica)
    Disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.Nombre

# Tabla para almacenar información sobre las categorías de los productos
class Categoria(models.Model):
    Id_categoria = models.CharField(max_length=8, primary_key=True)  # Identificador único de la categoría
    Nombre_categoria = models.CharField(max_length=50)  # Nombre de la categoría
    Descripcion = models.CharField(max_length=255)  # Descripción de la categoría

    def __str__(self):
        return self.Nombre_categoria

# Tabla para almacenar comentarios de los estudiantes y profesores sobre los productos
class ComentarioProducto(models.Model):
    Id_comentario = models.CharField(max_length=8, primary_key=True)  # Identificador único del comentario
    Producto = models.ForeignKey(Producto, on_delete=models.CASCADE)  # Producto relacionado al comentario
    Estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, null=True, blank=True)  # Estudiante que realiza el comentario (puede ser nulo si el comentario lo hace un profesor)
    Profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE, null=True, blank=True)  # Profesor que realiza el comentario (puede ser nulo si el comentario lo hace un estudiante)
    Comentario = models.CharField(max_length=255)  # Contenido del comentario
    Fecha = models.DateTimeField(auto_now_add=True)  # Fecha y hora del comentario

    def __str__(self):
        if self.estudiante:
            return _("Comentario de {0} sobre {1}").format(self.estudiante, self.producto)
        elif self.profesor:
            return _("Comentario de {0} sobre {1}").format(self.profesor, self.producto)
        else:
            return _("Comentario sobre {0}").format(self.producto)

    # def __str__(self):
    #     return "Comentario de {0} sobre {1}".format(self.Estudiante or self.Profesor, self.Producto)

# Tabla para almacenar información sobre los pedidos realizados por los estudiantes
from django.contrib.auth.models import User
class Pedido(models.Model):
    ESTADO_CHOICES = [
        ('PENDIENTE', 'Pendiente'),
        ('EN_PROCESO', 'En proceso'),
        ('ENVIADO', 'Enviado'),
        ('ENTREGADO', 'Entregado'),
        ('CANCELADO', 'Cancelado'),
    ]
     # TODO: CAMBIAR ESTO POR CLIENTE  
    usuario = models.Foreignkey(User, on_delete=models.CASCADE)
    Estudiante = models.ForeignKey('Estudiante', on_delete=models.SET_NULL, null=True, blank=True)  # Estudiante que realiza el pedido
    Profesor = models.ForeignKey('Profesor', on_delete=models.SET_NULL, null=True, blank=True)  # Profesor relacionado al pedido
    Empleado = models.ForeignKey('Empleado', on_delete=models.SET_NULL, null=True, blank=True)  # Empleado encargado del pedido
    Categoria = models.ForeignKey('Categoria', on_delete=models.SET_NULL, null=True, blank=True)  # Categoría del pedido
    Fecha = models.DateTimeField(auto_now_add=True)  # Fecha y hora del pedido
    Estado_pedido = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='PENDIENTE')  # Estado actual del pedido

    def __str__(self):
        return f"Pedido #{self.pk}"

    # def esta_disponible(self):
    #     return self.Stock > 0 and self.Disponible

# Tabla para almacenar información detallada sobre los productos incluidos en los pedidos
class DetallePedido(models.Model):
    Pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)  # Pedido al que pertenece el detalle
    Producto = models.ForeignKey(Producto, on_delete=models.CASCADE)  # Producto incluido en el detalle del pedido
    Cantidad = models.IntegerField()  # Cantidad del producto en el detalle del pedido
    # TODO: PRECIO TOTAL
    precio_total = models.DecimalField(max_digits=10, decimal_places=2)  # Precio unitario del producto en el detalle del pedido

    def __str__(self):
        return "Detalle pedido {0}".format(self.Pedido)

# Tabla para almacenar el historial de entregas de los pedidos
class HistorialPedido(models.Model):
    Id_historial_pedido = models.CharField(max_length=8, primary_key=True)  # Identificador único del historial del pedido
    Pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)  # Pedido al que pertenece el historial
    Fecha_entrega = models.DateField()  # Fecha de entrega del pedido
    Estado_entrega = models.CharField(max_length=10)  # Estado de entrega del pedido

    def __str__(self):
        return "Historial pedido {0}".format(self.Pedido)

# Tabla para almacenar información sobre los almuerzos pedidos por los estudiantes
class Almuerzo(models.Model):
    Id_almuerzo = models.CharField(max_length=8, primary_key=True)  # Identificador único del almuerzo
    Estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)  # Estudiante que realiza el pedido de almuerzo
    Fecha = models.DateField()  # Fecha del almuerzo
    Detalle = models.CharField(max_length=255)  # Detalle del almuerzo
    Precio = models.DecimalField(max_digits=10, decimal_places=2)  # Precio del almuerzo

    def __str__(self):
        return "Almuerzo {0} de {1}".format(self.Id_almuerzo, self.Estudiante)

# Tabla para almacenar información sobre los padres de los estudiantes
class Padre(models.Model):
    Id_padre = models.CharField(max_length=8, primary_key=True)  # Identificador único del padre
    Estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)  # Estudiante relacionado al padre
    Nombre = models.CharField(max_length=50)  # Nombre del padre
    Correo_electronico = models.EmailField(max_length=50)  # Correo electrónico del padre
    Telefono = models.CharField(max_length=15)  # Teléfono del padre
    Recomendaciones = models.CharField(max_length=255)  # Recomendaciones del padre (p. ej., sobre alergias)

    def __str__(self):
        return self.Nombre

# recomendaciones de no darle al estudiante, quitar las contraseñas, hacer una tabla de almuerzos y de padres (padres, por las alergias que pueden contener los estudiantes)
