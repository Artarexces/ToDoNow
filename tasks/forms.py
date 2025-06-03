from django import forms
from .models import Task
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

class TaskForm(forms.ModelForm):
    due_date = forms.DateTimeField(
        label='Fecha y hora',
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'})
    )
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'priority']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder':'Titulo'}),
            'description': forms.Textarea(attrs={'placeholder':'Descripción'})
        }

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, label='Nombre')
    email = forms.EmailField(required=True, label='Correo electrónico')
    class Meta:
        model = User
        fields = ['username', 'first_name', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Usuario'}),
            'password1': forms.PasswordInput(attrs={'placeholder': 'Contraseña'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Repite la contraseña'}),
        }
        

