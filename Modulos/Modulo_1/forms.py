from django import forms
from .models import Cliente, Producto, Colegio, Grado, Aniolectivo, Proveedor, Pedido, Empleado

# Formulario para el modelo Estudiante
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        widgets = {
            'usuario': forms.Select(attrs={'class': 'form-control'}),
            'colegio': forms.Select(attrs={'class': 'form-control'}),
            'genero': forms.Select(attrs={'class': 'form-control'}),
            'grado': forms.Select(attrs={'class': 'form-control'}),
            'telefono': forms.NumberInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'activo  ': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'alergias': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-control'})  # Para cargar imagen
        }

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
            'fecha_vencimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'proveedor': forms.Select(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'disponible': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control-file mt-2'})  # Para cargar imagen
        }

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = '__all__'


# Formulario para el modelo Año Lectivo
class AniolectivoForm(forms.ModelForm):
    class Meta:
        model = Aniolectivo
        fields = '__all__'
        widgets = {
            'Codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'Nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'Fecha_inicio': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'Fecha_fin': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

# Formulario para el modelo Proveedor
class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.NumberInput(attrs={'class': 'form-control'}),
            'correo_electronico': forms.EmailInput(attrs={'class': 'form-control'}),
            'contacto': forms.TextInput(attrs={'class': 'form-control'}),
            'activo  ': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'genero': forms.Select(attrs={'class': 'form-control'}),
            'cargo': forms.Select(attrs={'class': 'form-control'}),
            'telefono': forms.NumberInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'activo  ': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
