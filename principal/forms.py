#encoding:utf-8
from django.forms import ModelForm
from django import forms
from principal.models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrarUsuarioForm(UserCreationForm):  
    class Meta:
        model = User
        exclude = ("is_staff","is_active", "is_superuser", "last_login", "groups", "user_permissions", "date_joined","telefono","direccion","estado_login","foto","genero","password")

class EditarUser(ModelForm):
	
	class Meta:
		model = User
		exclude = ("genero","is_staff","is_active","is_superuser","last_login", "groups", "user_permissions", "date_joined", 'password', 'password1', 'password2')