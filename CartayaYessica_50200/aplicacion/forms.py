from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class PlantaForm(forms.Form):
    nombre = forms.CharField(max_length=50,required=True,label="Nombre de la Planta")
    ambiente = forms.CharField(max_length=50,required=True,label="Ambiente de Ubicación")
    riego = forms.CharField(max_length=50,required=True,label="Tipo de Riego")
    iluminacion = forms.CharField(max_length=50,required=True,label="Iluminación")
    tamaño = forms.CharField(max_length=50,required=True,label="Tamaño de la Planta") 

class MacetaForm(forms.Form):
    material = forms.CharField(max_length=50,required=True,label="Material de la Maceta")
    forma = forms.CharField(max_length=50,required=True,label="Forma")
    tamaño = forms.CharField(max_length=50,required=True,label="Tamaño")
    color = forms.CharField(max_length=50,required=True,label="Color")

class FertilizanteForm(forms.Form):
    nombre = forms.CharField(max_length=50,required=True,label="Nombre del Fertilizante")
    nutrientes = forms.CharField(max_length=100,required=True,label="Nutrientes")
    dosis = forms.CharField(max_length=100,required=True,label="Dosis")
    precauciones = forms.CharField(max_length=500,required=True,label="Precauciones")

class PlaguicidaForm(forms.Form):
    nombre = forms.CharField(max_length=50,required=True,label="Nombre del Plaguicida")
    presentacion = forms.CharField(max_length=50,required=True,label="Presentación")
    plaga = forms.CharField(max_length=300,required=True,label="Plagas que Controla")
    contenidoNeto = forms.CharField(max_length=50,required=True,label="Contenido Neto")

class RegistroForm(UserCreationForm):
    email = forms.EmailField(max_length=50,required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields= ['username','email','password1','password2']

class UserEditForm(UserCreationForm):
    email = forms.EmailField(max_length=50,required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)
    first_name = forms.CharField(label="Nombre/s", max_length=50, required=True)
    last_name = forms.CharField(label="Apellido/s", max_length=50, required=True)

    class Meta:
        model = User
        fields= ['email','password1','password2','first_name', 'last_name']

class AvatarForm(forms.Form):
    imagen= forms.ImageField(required=True)