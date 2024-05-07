from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


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
    Aniolectivo = models.ForeignKey(Aniolectivo, on_delete=models.CASCADE, null=True, blank=True, verbose_name=("Año lectivo"))

    def __str__(self):
        return self.Nombre


class Cliente(models.Model):
    colegio = models.ForeignKey(Colegio, on_delete=models.CASCADE)
    genero = models.CharField(max_length=1, choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')])
    grado = models.ForeignKey(Grado, on_delete=models.SET_NULL, null=True, blank=True)
    telefono = models.CharField(max_length=15, null=True, blank=True)
    direccion = models.CharField(max_length=50, null=True, blank=True)
    activo = models.BooleanField(default=True)
    alergias = models.CharField(max_length=50, null=True, blank=True)
    tipo = models.CharField(max_length=10, choices=[('PROFESOR', 'Profesor'), ('ESTUDIANTE', 'cliente')], default='ESTUDIANTE')


class Empleado(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    genero = models.CharField(max_length=1, choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')])
    cargo = models.CharField(max_length=15, choices=[('E', 'Empleado'), ('A', 'Administrador')])
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=50)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return "{0}, {1}".format(self.Apellido_paterno, self.Nombres)


# Tabla para almacenar información sobre los proveedores de productos
class Proveedor(models.Model):
    nombre = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=35)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15)
    correo_electronico = models.EmailField(max_length=50)
    contacto = models.CharField(max_length=35)
    activo = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre


# Tabla para almacenar información sobre los productos ofrecidos por los proveedores
class Producto(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='Productos/', default='no_disponible.jpg')
    nombre = models.CharField(max_length=50)
    stock = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)  # Precio del producto
    descripcion = models.CharField(max_length=255)
    fecha_vencimiento = models.DateField(null=True, blank=True)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

# Tabla para almacenar información sobre las categorías de los productos
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)  # Nombre de la categoría
    descripcion = models.CharField(max_length=255)  # Descripción de la categoría

    def __str__(self):
        return self.Nombre_categoria

# Tabla para almacenar comentarios de los estudiantes y profesores sobre los productos
class ComentarioProducto(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)  # Producto relacionado al comentario
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True, blank=True)  # Estudiante relacionado al comentario
    comentario = models.CharField(max_length=255)  # Contenido del comentario
    fecha = models.DateTimeField(auto_now_add=True)  # Fecha y hora del comentario

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
class Pedido(models.Model):
    ESTADO_CHOICES = [
        ('PENDIENTE', 'Pendiente'),
        ('EN_PROCESO', 'En proceso'),
        ('ENVIADO', 'Enviado'),
        ('ENTREGADO', 'Entregado'),
        ('CANCELADO', 'Cancelado'),
    ]
    cliente = models.ForeignKey('Cliente', on_delete=models.SET_NULL, null=True, blank=True, related_name='pedidos')
    empleado = models.ForeignKey('Empleado', on_delete=models.SET_NULL, null=True, blank=True, related_name='pedidos')
    categoria = models.ForeignKey('Categoria', on_delete=models.SET_NULL, null=True, blank=True)  # Categoría del pedido
    fecha = models.DateTimeField(auto_now_add=True)  # Fecha y hora del pedido
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='PENDIENTE')  # Estado actual del pedido

    def __str__(self):
        return f"Pedido #{self.pk}"


# Tabla para almacenar información detallada sobre los productos incluidos en los pedidos
class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return "Detalle pedido {0}".format(self.Pedido)

# Tabla para almacenar el historial de entregas de los pedidos
class HistorialPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    fecha_entrega = models.DateField()
    estado_entrega = models.CharField(max_length=10)

    def __str__(self):
        return "Historial pedido {0}".format(self.Pedido)


# Tabla para almacenar información sobre los almuerzos pedidos por los estudiantes
class Almuerzo(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateField()
    detalle = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return "Almuerzo {0} de {1}".format(self.Id_almuerzo, self.Estudiante)


# Tabla para almacenar información sobre los padres de los estudiantes
class Padre(models.Model):
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE)
    hijos = models.ManyToManyField(Cliente, related_name='padres')
    telefono = models.CharField(max_length=15)
    recomendaciones = models.CharField(max_length=255)

    def __str__(self):
        return self.first_name

    def get_cliente(self):
        return Cliente.objects.get(id=self.cliente_id)

# recomendaciones de no darle al estudiante, quitar las contraseñas, hacer una tabla de almuerzos y de padres (padres, por las alergias que pueden contener los estudiantes)
