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
		return render_to_response('perfilprofesor.html',{'dato':dato,'dato1':dato1,'profesor':profesor}, context_instance=RequestContext(request))
	else:
		print "la otras sea"	
	return HttpResponseRedirect('/')

@login_required(login_url='/')
def cerrar(request):
	logout(request)
	return HttpResponseRedirect('/')


def cursos(request):
	cursos_ab = CursoAbierto.objects.all().order_by("fecha_inicio")
	cursos=Curso.objects.all()
	return render_to_response('cursos.html', {'cursos_ab':cursos_ab, 'cursos':cursos}, context_instance=RequestContext(request))

def dato_curso_abierto(request, id_curso_ab):
	dato = CursoAbierto.objects.get(pk=id_curso_ab)
	cursoab = Curso.objects.get(pk=dato.curso_id)

	
	tema=Tema.objects.filter(cursoabierto=id_curso_ab)
	
	
<<<<<<< HEAD
	return render_to_response('dato_curso_abierto.html',{'curso_ab':dato, 'curso':cursoab, 'silabo':silabo, 'tema':tema, 'subtema':subtema},context_instance = RequestContext(request))

=======
	return render_to_response('dato_curso_abierto.html',{'curso_ab':dato, 'curso':cursoab,  'tema':tema },context_instance = RequestContext(request))
>>>>>>> 34b6f885194f30238d2deb2f7e4d073065eccc5e
