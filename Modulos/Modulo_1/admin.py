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
    queryset.update(disponible=True)

marcar_disponible.short_description = "Marcar como disponible"


def marcar_no_disponible(modeladmin, request, queryset):
    queryset.update(disponible=False)

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
    list_display = ['nombre', 'proveedor', 'stock', 'precio', 'disponible', 'get_precio_display']
    search_fields = ['nombre', 'proveedor__nombre', 'descripcion', '^nombre']  # Búsqueda avanzada
    list_filter = ['proveedor', 'disponible', PrecioProductoListFilter]
    ordering = ['nombre']
    actions = [marcar_disponible, marcar_no_disponible]
    list_editable = ['stock', 'disponible']
    list_per_page = 20

    def get_precio_display(self, obj):
        return f'${obj.precio:.2f}'

    get_precio_display.short_description = 'Precio'


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ['id', 'cliente', 'empleado', 'categoria', 'fecha', 'estado', calcular_total_pedido]
    search_fields = ['id', 'cliente__firt_name']
    list_filter = ['estado']
    ordering = ['-fecha']
    readonly_fields = ['fecha']
    inlines = [DetallePedidoInline]
    raw_id_fields = ['cliente', 'empleado']
    autocomplete_fields = ['categoria']

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

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['get_first_name', 'get_last_name', 'genero', 'telefono', 'email', 'direccion', 'activo']
    search_fields = ['usuario__first_name', 'usuario__last_name']
    list_filter = ['activo']
    ordering = ['usuario__last_name', 'usuario__first_name']

    def get_first_name(self, obj):
        return obj.usuario.first_name
    
    def get_last_name(self, obj):
        return obj.usuario.last_name
    
    def email(self, obj):
        return obj.usuario.email


@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ['get_first_name', 'get_last_name', 'genero', 'cargo', 'telefono', 'email', 'direccion', 'activo']
    search_fields = ['usuario__first_name', 'usuario__last_name']
    list_filter = ['cargo', 'activo']
    ordering = ['usuario__last_name', 'usuario__first_name']

    def get_first_name(self, obj):
        return obj.usuario.first_name
    
    def get_last_name(self, obj):
        return obj.usuario.last_name
    
    def email(self, obj):
        return obj.usuario.email

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'ciudad', 'telefono', 'correo_electronico', 'contacto', 'activo']
    search_fields = ['nombre']
    ordering = ['nombre']

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    search_fields = ['nombre']
    ordering = ['nombre']

@admin.register(ComentarioProducto)
class ComentarioProductoAdmin(admin.ModelAdmin):
    list_display = ['producto', 'comentario', 'fecha']
    search_fields = ['producto__Nombre', 'cliente_first_name']
    ordering = ['-fecha']


@admin.register(DetallePedido)
class DetallePedidoAdmin(admin.ModelAdmin):
    list_display = ['pedido', 'producto', 'cantidad', 'precio_total']
    search_fields = ['pedido__pk', 'producto__Nombre']
    ordering = ['pedido']

@admin.register(HistorialPedido)
class HistorialPedidoAdmin(admin.ModelAdmin):
    list_display = ['pedido', 'estado_entrega', 'fecha_entrega']
    search_fields = ['pedido__pk']
    list_filter = ['estado_entrega']
    ordering = ['-fecha_entrega']

@admin.register(Almuerzo)
class AlmuerzoAdmin(admin.ModelAdmin):
    list_display = ['cliente', 'fecha', 'detalle', 'precio']
    search_fields = ['cliente_first_name']
    ordering = ['-fecha']

@admin.register(Padre)
class PadreAdmin(admin.ModelAdmin):
    list_display = ['get_first_name', 'get_last_name', 'email', 'telefono', 'recomendaciones']
    search_fields = ['usuario__first_name', 'usuario__last_name']
    ordering = ['usuario__last_name', 'usuario__first_name']

    def get_first_name(self, obj):
        return obj.usuario.first_name
    
    def get_last_name(self, obj):
        return obj.usuario.last_name
    
    def email(self, obj):
        return obj.usuario.email