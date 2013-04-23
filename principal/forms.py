#encoding:utf-8
from django.forms import ModelForm
from django import forms
from principal.models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


def validar(value):
	if value.isalpha!=1:
		raise ValidationError("Solo admite letras 'A-Z' y 'a-z'")

class RegistrarUsuarioForm(UserCreationForm):
	username = forms.CharField(max_length=20,validators=[validar])
	class Meta:
		model = User
		exclude = ("is_staff","is_active", "is_superuser", "last_login", "groups", "user_permissions", "date_joined","telefono","direccion","estado_login","foto","genero","password")

class EditarUser(ModelForm):
	
	class Meta:
		model = User
		exclude = ("genero","is_staff","is_active","is_superuser","last_login", "groups", "user_permissions", "date_joined", 'password', 'password1', 'password2')