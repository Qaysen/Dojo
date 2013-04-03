from principal.models import *
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import  AuthenticationForm

def home(request):
	if request.method == 'POST':
		formulario = AuthenticationForm(request.POST)
		if formulario.is_valid:
			usuario = request.POST['username']
			clave = request.POST['password']
			acceso = authenticate(username=usuario, password=clave)
			if acceso is not None:
				user= User.objects.get(username=usuario)
				if acceso.is_active:
					login(request, acceso)
					user.save()
					dato=nombreusuario(user.email)
					return render_to_response('home.html',{'dato':dato}, context_instance=RequestContext(request))

				else:
					return render_to_response('noactivo.html', context_instance=RequestContext(request))
			else:
				return render_to_response('nousuario.html', context_instance=RequestContext(request))
	else:
		formulario = AuthenticationForm()
	return render_to_response('home.html',{'formulario':formulario}, context_instance=RequestContext(request))

def nombreusuario(correo):
	m=correo.split('@')
	return m[0]

def perfil(request,username):
	usuario=request.user
	perfil= Alumno.objects.filter(usuario=usuario.id).count()

	if perfil==0:
		dato=usuario
		return render_to_response('miperfil.html',{'dato':dato}, context_instance=RequestContext(request))
	else:
		print "la otras sea "	
	return HttpResponseRedirect('/')

@login_required(login_url='/')
def cerrar(request):
	logout(request)
	return HttpResponseRedirect('/')


