from principal.models import *
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from principal.forms import *
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import  AuthenticationForm

# Pagina de inicio
def inicio(request):
	return render_to_response('inicio.html', context_instance=RequestContext(request))

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
					dato=usuario
					return render_to_response('home.html',{'dato1':dato}, context_instance=RequestContext(request))
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
		profesor=Profesor.objects.get(usuario=usuario)
		dato=usuario
		dato1=username
		print profesor.id
		cursos=CursoAbierto.objects.filter(profesor_id=profesor.id).distinct()
		return render_to_response('perfilprofesor.html',{'dato':dato,'lista_cursos':cursos,'dato1':dato1,'profesor':profesor}, context_instance=RequestContext(request))
	else:
		print "la otras sea"	
	return HttpResponseRedirect('/')

@login_required(login_url='/')
def cerrar(request):
	logout(request)
	return HttpResponseRedirect('/')


def cursos(request):
	cursos_abiertos = CursoAbierto.objects.all().order_by("fecha_inicio")
	return render_to_response('cursos.html', {'cursos_abiertos':cursos_abiertos}, context_instance=RequestContext(request))

def dato_curso_abierto(request, id_curso_ab):
	dato = CursoAbierto.objects.get(pk=id_curso_ab)
	cursoab = Curso.objects.get(pk=dato.curso_id)


	tema=Tema.objects.filter(cursoabierto=id_curso_ab)

	return render_to_response('dato_curso_abierto.html',{'curso_ab':dato, 'curso':cursoab,  'tema':tema },context_instance = RequestContext(request))

def registrarse(request):
	if request.method=='POST':
		formulario=RegistrarUsuarioForm(request.POST)
		#Hay diferencia entre is_valid() y is_valid, mientras que el primero valida mostrando los errores el ultimo no muestra los errores.
		if formulario.is_valid():
			formulario.save()
			iduser=User.objects.get(username=request.POST['username'])
			Alumno.objects.create(usuario_id=iduser.id)
			return HttpResponseRedirect('/')
	else:
		formulario = RegistrarUsuarioForm()
	return render_to_response('registrar.html', {'formulario':formulario}, context_instance=RequestContext(request))

def actualizar_perfil(request):
	usuario = User.objects.get(pk = request.user.id)
	if request.method=='POST':
		formulario = EditarUser(request.POST,request.FILES,instance = usuario)
		if formulario.is_valid():
			print formulario.cleaned_data['foto']

			formulario.save()
			return HttpResponseRedirect('/')
	else:
		formulario = EditarUser(instance = usuario)
	return render_to_response('actualizar_perfil.html', {'formulario':formulario,'dato1':usuario.username, 'usuario':usuario}, context_instance=RequestContext(request))

def actualizar_password(request):
	usuario = User.objects.get(pk = request.user.id)
	if request.method=='POST':
		bandera= usuario.check_password(request.POST['password'])
		if bandera:
			usuario.set_password(request.POST['password1'])
			usuario.save();
	return render_to_response('cambiarpassword.html', {'dato1':usuario.username, 'usuario':usuario}, context_instance=RequestContext(request))
