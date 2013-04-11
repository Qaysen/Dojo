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
					return HttpResponseRedirect('/')
				else:
					return render_to_response('noactivo.html', context_instance=RequestContext(request))
			else:
				return render_to_response('nousuario.html', context_instance=RequestContext(request))
	else:
		formulario = AuthenticationForm()
	return render_to_response('home.html',{'formulario':formulario}, context_instance=RequestContext(request))

@login_required(login_url='/')
def cerrar(request):
	logout(request)
	return HttpResponseRedirect('/')

def cursos(request):
	cursos_ab = CursoAbierto.objects.all().order_by("fecha_inicio")

	return render_to_response('cursos.html', {'cursos_ab':cursos_ab}, context_instance=RequestContext(request))

def dato_curso_abierto(request, id_curso_ab):
	dato = CursoAbierto.objects.get(pk=id_curso_ab)
	cursoab = Curso.objects.get(pk=dato.curso_id)
		
	tema=Tema.objects.filter(cursoabierto=id_curso_ab)

	padres=tema.filter(subtema_id=None).order_by("orden")
	hijos=tema.exclude(subtema_id=None)


	hijoss={}
	

	for i in range(len(padres)):
		hijoss[i+1] = {}

	for x in hijos:
	  	id_padre=x.subtema_id
	  	for y in padres:
	  		if y.id is id_padre:
	  			padre=y.orden
	  			print padre

	  	subhijos=tema.filter(subtema_id=id_padre)
	  	hijoss[id_padre]={}
	  	for y in subhijos:	
	  		hijoss[padre][y.orden]=y 	 	

	a = [hijoss[x].values() for x in hijoss]

	padres_hijos=zip(padres,a)

	# print a

	return render_to_response('dato_curso_abierto.html',{'curso_ab':dato, 'curso':cursoab,  'temario':padres_hijos },context_instance = RequestContext(request))


def material(request,id_subtema):
	material = Material.objects.filter(tema_id=id_subtema)
	print id_subtema
	mat= Material.objects.filter(tema_id=id_subtema).count()
	print mat	

	return render_to_response('material.html',{'material':material},context_instance = RequestContext(request))
