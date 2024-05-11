from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from Modulos.Modulo_1.models import Colegio, Cliente

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    colegio = forms.ModelChoiceField(queryset=Colegio.objects.all(), required=True, widget=forms.Select(attrs={'class': 'form-select'}))
    tipo = forms.ChoiceField(choices=[('ESTUDIANTE', 'Estudiante'), ('PROFESOR', 'Profesor')], required=True, widget=forms.Select(attrs={'class': 'form-select'}))
    telefono = forms.CharField(max_length=15, required=True)
    direccion = forms.CharField(max_length=50, required=False)
    genero = forms.ChoiceField(choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')], required=False, widget=forms.Select(attrs={'class': 'form-select'}))
    
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'colegio', 'tipo', 'telefono', 'direccion', 'genero')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Ingresa tu usuario'
        self.fields['email'].widget.attrs['placeholder'] = 'Ingresa tu email'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Ingresa tu nombre'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Ingresa tu apellido'
        self.fields['password1'].widget.attrs['placeholder'] = 'Ingresar Contraseña'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirmar contraseña'
        self.fields['telefono'].widget.attrs['placeholder'] = 'Ingresa tu telefono'
        self.fields['direccion'].widget.attrs['placeholder'] = 'Ingresa tu direccion'
        