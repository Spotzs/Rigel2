from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static

# Importaciones de vistas desde los módulos correspondientes
from Modulos.Modulo_1.views import (
    Index, formularioContacto, contactar, agregar_estudiante, agregar_profesor,
    agregar_producto, listado_cliente, eliminar_estudiante, modificar_estudiante,
    listado_colegio, listado_grado, agregar_colegio, agregar_grado, modificar_grado,
    modificar_colegio, listado_aniolectivo, agregar_aniolectivo, modificar_aniolectivo,
    buscarestudiante, buscar_grado, buscar_colegio, buscar_lectivo, listado_producto, eliminar_producto,
    modificar_producto, listado_proveedor, buscar_producto, exportar_listado, listado_pedido, buscar_pedido, agregar_alcarrito,
    listado_empleado, agregar_empleado, modificar_empleado, eliminar_empleado, agregar_proveedor, modificar_proveedor,
    eliminar_proveedor

)

from Modulos.Modulo_2.views import (
    LoginView, LogoutView, landing, user_login, register
)
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views


# Definición de las URLs de la aplicación
urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', login_required(Index), name='index'),
    path('registro/', register, name='register'),
    path('login/', user_login, name='login'),
    path('formularioContacto/', login_required(formularioContacto)),
    path('contactar/', login_required(contactar)),
    path('exportar-listado/', login_required(exportar_listado), name='exportar_listado'),


    # URLs relacionadas con listados y agregados
    path('listgrado/', login_required(listado_grado), name='listado_grado'),
    path('listgrado/search/', login_required(buscar_grado), name='buscar_grado'),
    path('listlectivo/', login_required(listado_aniolectivo), name='listado_aniolectivo'),
    path('listlectivo/search/', login_required(buscar_lectivo), name='buscar_lectivo'),
    path('listcliente/', login_required(listado_cliente), name='listado_cliente'),
    path('listest/search/', login_required(buscarestudiante), name='buscarestudiante'),
    path('listcole/', login_required(listado_colegio), name='listado_colegio'),
    path('listcole/search/', login_required(buscar_colegio), name='buscar_colegio'),
    path('listproducto/', login_required(listado_producto), name='listado_producto'),
    path('listproducto/search/', login_required(buscar_producto), name='buscar_producto'),
    path('listproveedor', login_required(listado_proveedor), name='listado_proveedor'),
    path('listpedido', login_required(listado_pedido), name='listado_pedido'),
    path('listpedido/search/', login_required(buscar_pedido), name='buscar_pedido'),
    path('listempleado/', login_required(listado_empleado), name='listado_empleado'),

    # URLs para acciones de agregar y modificar
    path('landing/', login_required(landing), name='landingpage'),
    path('agregar_grado/', login_required(agregar_grado), name='agregar_grado'),
    path('agregar_colegio/', login_required(agregar_colegio), name='agregar_colegio'),
    path('agregar_estudiante/', login_required(agregar_estudiante), name='agregar_estudiante'),
    path('agregar_profesor/', login_required(agregar_profesor), name='agregar_profesor'),
    path('agregar_empleado/', login_required(agregar_empleado), name='agregar_empleado'),
     path('agregar_proveedor/', login_required(agregar_proveedor), name='agregar_proveedor'),
    path('agregar_producto/', login_required(agregar_producto), name='agregar_producto'),
    path('agregar_aniolectivo/', login_required(agregar_aniolectivo), name='agregar_aniolectivo'),

    # URLs para acciones de modificar y eliminar
    path('modificar-Año/<Codigo>/', login_required(modificar_aniolectivo), name='modificar_aniolectivo'),
    path('modificar_producto/<int:pk>/', login_required(modificar_producto), name='modificar_producto'),
    path('modificar-colegio/<Codigo>/', login_required(modificar_colegio), name='modificar_colegio'),
    path('modificar-grado/<Codigo>/', login_required(modificar_grado), name='modificar_grado'),
    path('modificar-estudiante/<Id_estudiante>/', login_required(modificar_estudiante), name='modificar_estudiante'),
    path('modificar-empleado/<Id_empleado>/', login_required(modificar_empleado), name='modificar_empleado'),
    path('modificar-proveedor/<pk>/', login_required(modificar_proveedor), name='modificar_proveedor'),

    path('eliminar-estudiante/<Id_estudiante>/', login_required(eliminar_estudiante), name='eliminar_estudiante'),
    path('eliminar_proveedor/<pk>/', login_required(eliminar_proveedor), name='eliminar_proveedor'),
    path('eliminar_producto/<int:Id_producto>', login_required(eliminar_producto), name='eliminar_producto'),
    path('eliminar_empleado/<int:Id_empleado>', login_required(eliminar_empleado), name='eliminar_empleado'),

    path('agregar_alcarrito/', login_required(agregar_alcarrito), name='agregar_alcarrito'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
