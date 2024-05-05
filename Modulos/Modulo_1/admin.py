from django.contrib import admin
from Modulos.Modulo_1.models import *
from django.db import models

class DetallePedidoInline(admin.TabularInline):
    model = DetallePedido
    extra = 0


# Filtros personalizados
class PrecioProductoListFilter(admin.SimpleListFilter):
    title = 'Rango de precios'
    parameter_name = 'precio'

    def lookups(self, request, model_admin):
        return (
            ('0-10', 'Menos de 10'),
            ('10-100', '10 a 100'),
            ('100-1000', '100 a 1000'),
            ('1000-', 'Más de 1000'),
        )

    def queryset(self, request, queryset):
        value = self.value()
        if value == '0-10':
            return queryset.filter(Precio__lte=10)
        elif value == '10-100':
            return queryset.filter(Precio__gte=10, Precio__lte=100)
        elif value == '100-1000':
            return queryset.filter(Precio__gte=100, Precio__lte=1000)
        elif value == '1000-':
            return queryset.filter(Precio__gte=1000)


# Acciones personalizadas
def marcar_disponible(modeladmin, request, queryset):
    queryset.update(Disponible=True)

marcar_disponible.short_description = "Marcar como disponible"


def marcar_no_disponible(modeladmin, request, queryset):
    queryset.update(Disponible=False)

marcar_no_disponible.short_description = "Marcar como no disponible"


# Campos calculados
def calcular_total_pedido(obj):
    detalles = obj.detallepedido_set.all()
    total = sum(detalle.precio_total for detalle in detalles)
    return total

calcular_total_pedido.short_description = 'Total del pedido'


@admin.register(Colegio)
class ColegioAdmin(admin.ModelAdmin):
    list_display = ['Nombre', 'Rector']
    search_fields = ['Nombre']
    ordering = ['Nombre']


# Otros modelos

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['Nombre', 'Proveedor', 'Stock', 'Precio', 'Disponible', 'get_precio_display']
    search_fields = ['Nombre', 'Proveedor__Nombre', 'Descripcion', '^Nombre']  # Búsqueda avanzada
    list_filter = ['Proveedor', 'Disponible', PrecioProductoListFilter]
    ordering = ['Nombre']
    actions = [marcar_disponible, marcar_no_disponible]
    list_editable = ['Stock', 'Disponible']
    list_per_page = 20

    def get_precio_display(self, obj):
        return f'${obj.Precio:.2f}'

    get_precio_display.short_description = 'Precio'


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ['id', 'Estudiante', 'Profesor', 'Empleado', 'Categoria', 'Fecha', 'Estado_pedido', calcular_total_pedido]
    search_fields = ['id', 'Estudiante__Nombres', 'Profesor__Nombres']
    list_filter = ['Estado_pedido']
    ordering = ['-Fecha']
    readonly_fields = ['Fecha']
    inlines = [DetallePedidoInline]
    raw_id_fields = ['Estudiante', 'Profesor', 'Empleado']
    autocomplete_fields = ['Categoria']

@admin.register(Aniolectivo)
class AniolectivoAdmin(admin.ModelAdmin):
    list_display = ['Nombre', 'Fecha_inicio', 'Fecha_fin']
    search_fields = ['Nombre']
    ordering = ['Nombre']

@admin.register(Grado)
class GradoAdmin(admin.ModelAdmin):
    list_display = ['Nombre', 'Aniolectivo']
    search_fields = ['Nombre']
    ordering = ['Nombre']

@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ['Nombres', 'Apellido', 'Genero', 'Grado', 'Telefono', 'Correo_electronico', 'Direccion', 'Activo', 'Alergias']
    search_fields = ['Nombres', 'Apellido']
    list_filter = ['Activo', 'Grado']
    ordering = ['Apellido', 'Nombres']

@admin.register(Profesor)
class ProfesorAdmin(admin.ModelAdmin):
    list_display = ['Nombres', 'Apellido_paterno', 'Apellido_materno', 'Genero', 'Telefono', 'Correo_electronico', 'Direccion', 'Activo']
    search_fields = ['Nombres', 'Apellido_paterno', 'Apellido_materno']
    list_filter = ['Activo']
    ordering = ['Apellido_paterno', 'Apellido_materno', 'Nombres']

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ['Nombres', 'Apellido_paterno', 'Apellido_materno', 'Genero', 'Cargo', 'Telefono', 'Correo_electronico', 'Direccion', 'Activo']
    search_fields = ['Nombres', 'Apellido_paterno', 'Apellido_materno']
    list_filter = ['Cargo', 'Activo']
    ordering = ['Apellido_paterno', 'Apellido_materno', 'Nombres']

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ['Nombre', 'Ciudad', 'Telefono', 'Correo_electronico', 'Contacto']
    search_fields = ['Nombre']
    ordering = ['Nombre']

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['Nombre_categoria']
    search_fields = ['Nombre_categoria']
    ordering = ['Nombre_categoria']

@admin.register(ComentarioProducto)
class ComentarioProductoAdmin(admin.ModelAdmin):
    list_display = ['Producto', 'Comentario', 'Fecha'] 
    search_fields = ['Producto__Nombre', 'Estudiante__Nombres', 'Profesor__Nombres']
    ordering = ['-Fecha']


@admin.register(DetallePedido)
class DetallePedidoAdmin(admin.ModelAdmin):
    list_display = ['Pedido', 'Producto', 'Cantidad', 'precio_total']
    search_fields = ['Pedido__pk', 'Producto__Nombre']
    ordering = ['Pedido']

@admin.register(HistorialPedido)
class HistorialPedidoAdmin(admin.ModelAdmin):
    list_display = ['Pedido', 'Estado_entrega', 'Fecha_entrega']
    search_fields = ['Pedido__pk']
    list_filter = ['Estado_entrega']
    ordering = ['-Fecha_entrega']

@admin.register(Almuerzo)
class AlmuerzoAdmin(admin.ModelAdmin):
    list_display = ['Id_almuerzo', 'Estudiante', 'Fecha', 'Detalle', 'Precio']
    search_fields = ['Id_almuerzo', 'Estudiante__Nombres']
    ordering = ['-Fecha']

@admin.register(Padre)
class PadreAdmin(admin.ModelAdmin):
    list_display = ['Nombre', 'Estudiante', 'Correo_electronico', 'Telefono', 'Recomendaciones']
    search_fields = ['Nombre', 'Estudiante__Nombres']
    ordering = ['Estudiante', 'Nombre']
