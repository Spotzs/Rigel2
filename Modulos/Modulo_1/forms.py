from django import forms
from .models import Estudiante, Profesor, Producto, Colegio, Grado, Aniolectivo, Proveedor, Pedido, Empleado

# Formulario para el modelo Estudiante
class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = '__all__'

# Formulario para el modelo Colegio
class ColegioForm(forms.ModelForm):
    class Meta:
        model = Colegio
        fields = '__all__'

# Formulario para el modelo Grado
class GradoForm(forms.ModelForm):
    class Meta:
        model = Grado
        fields = '__all__'

# Formulario para el modelo Producto
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        widgets = {
            'Id_producto': forms.TextInput(attrs={'class': 'form-control'}),  # Campo solo lectura
            'Fecha_vencimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'Proveedor': forms.Select(attrs={'class': 'form-control'}),
            'Categoria': forms.Select(attrs={'class': 'form-control'}),
            'Nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'Stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'Precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'Descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'Disponible': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'Imagen': forms.FileInput(attrs={'class': 'form-control-file mt-2'})  # Para cargar imagen
        }

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = '__all__'

# Formulario para el modelo Profesor
class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = '__all__'
        widgets = {
            'Id_profesor': forms.TextInput(attrs={'class': 'form-control'}),  # Campo solo lectura
            'Apellido_paterno': forms.TextInput(attrs={'class': 'form-control'}),
            'Apellido_materno': forms.TextInput(attrs={'class': 'form-control'}),
            'Nombres': forms.TextInput(attrs={'class': 'form-control'}),
            'Genero': forms.Select(attrs={'class': 'form-control'}),
            'Telefono': forms.NumberInput(attrs={'class': 'form-control'}),
            'Correo_electronico': forms.TextInput(attrs={'class': 'form-control'}),
            'Direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'Activo  ': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

# Formulario para el modelo Año Lectivo
class AniolectivoForm(forms.ModelForm):
    class Meta:
        model = Aniolectivo
        fields = '__all__'
        widgets = {
            'Fecha_inicio': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'Fecha_fin': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

# Formulario para el modelo Proveedor
class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = '__all__'


class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'
        widgets = {
            'Id_empleado': forms.TextInput(attrs={'class': 'form-control'}),  # Campo solo lectura
            'Apellido_paterno': forms.TextInput(attrs={'class': 'form-control'}),
            'Apellido_materno': forms.TextInput(attrs={'class': 'form-control'}),
            'Nombres': forms.TextInput(attrs={'class': 'form-control'}),
            'Genero': forms.Select(attrs={'class': 'form-control'}),
            'Cargo': forms.Select(attrs={'class': 'form-control'}),
            'Telefono': forms.NumberInput(attrs={'class': 'form-control'}),
            'Correo_electronico': forms.TextInput(attrs={'class': 'form-control'}),
            'Direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'Activo  ': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
