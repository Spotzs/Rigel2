from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required.')

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Ingresa tu usuario'
        self.fields['email'].widget.attrs['placeholder'] = 'Ingresa tu email'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Ingresa tu nombre'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Ingresa tu apellido'
        self.fields['password1'].widget.attrs['placeholder'] = 'Ingresar Contraseña'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirmar contraseña'
        
