from principal.models import *
from home.models import *
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from principal.forms import *
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.core.servers.basehttp import FileWrapper
from urllib import unquote
from django.contrib.auth.forms import  AuthenticationForm
# from reportlab.pdfgen import canvas


def loginto(request):
	for elemento in request:
		print elemento

	if request.method == 'POST':
		formulario = AuthenticationForm(request.POST)

		if formulario.is_valid:
			
			usuario = request.POST['username']
			clave = request.POST['password']
			anterior = request.POST['anterior']

			acceso = authenticate(username=usuario, password=clave)

			if acceso is not None:
				user= User.objects.get(username=usuario)

				if acceso.is_active:
					login(request, acceso)
					user.save()
					dato = nombreusuario(user.email)
					return HttpResponseRedirect(anterior)

				else:
					return render_to_response('noactivo.html', context_instance=RequestContext(request))
			else:
				return render_to_response('nousuario.html', context_instance=RequestContext(request))
	else:
		formulario = AuthenticationForm()

	return HttpResponseRedirect('/cursos/')

# Pagina de inicio
def inicio(request):
	cursos = Curso.objects.filter(protoCurso__tipo = "Curso")[:3]
	seminarios = Curso.objects.filter(protoCurso__tipo = "Seminario")[:3]
	return render_to_response('inicio.html', {'cursos':cursos, 'seminarios':seminarios}, context_instance=RequestContext(request))

def nombreusuario(correo):
	m=correo.split('@')
	return m[0]


def perfil(request,username):
	usuario=request.user
	if usuario.username==username:
		bandera= Alumno.objects.filter(usuario=usuario.id).count()
		if bandera==0:
			profesor=Profesor.objects.get(usuario=usuario)
			dato=usuario
			dato1=username
			print profesor.id
			cursos=CursoAbierto.objects.filter(profesor_id=profesor.id).distinct()
			return render_to_response('perfilprofesor.html',{'dato':dato,'lista_cursos':cursos,'dato1':dato1,'profesor':profesor}, context_instance=RequestContext(request))
		else:
			print "la otras sea"	
	else:
		return HttpResponseRedirect('/')

@login_required(login_url='/')
def cerrar(request):
	logout(request)
	return HttpResponseRedirect('/')


def categcursos(request):
	categoria = Categoria.objects.all()
	protocurso = ProtoCurso.objects.filter(tipo="Curso")
	localizacion = Localizacion.objects.all()
	return render_to_response('categorias.html', {'categoria':categoria,'protocurso':protocurso, 'localizacion':localizacion}, context_instance=RequestContext(request))

# def detallecurso(request, nomcurso):
# 	print nomcurso
# 	curso=Curso.objects.get(slug=nomcurso)	
# 	print curso
# 	id_curso_ab=curso.id
# 	cursos_ab = CursoAbierto.objects.filter(curso=id_curso_ab).order_by("fecha_inicio")
# 	return render_to_response('curso_abierto.html', {'cursos_ab':cursos_ab}, context_instance=RequestContext(request))

def cursos(request):
	cursos = Curso.objects.filter(protoCurso__tipo = "Curso")
	tipo = "seminarios"
	mismo = "cursos"
	return render_to_response('cursos.html', {'cursos':cursos, 'tipo': tipo, 'mismo': mismo}, context_instance=RequestContext(request))

def contacto(request):
	return render_to_response('contacto.html', context_instance=RequestContext(request))

def seminarios(request):
	seminarios = Curso.objects.filter(protoCurso__tipo = "Seminario")
	tipo = "cursos"
	mismo = "seminarios"
	return render_to_response('cursos.html', {'cursos':seminarios, 'tipo': tipo, 'mismo': mismo}, context_instance=RequestContext(request))

def detallecurso(request, nomcurso):
	protocurso=ProtoCurso.objects.get(slug=nomcurso)
	curso=Curso.objects.filter(protoCurso=protocurso.id)			
	tema=Tema.objects.filter(protoCurso=protocurso.id)
	horario=Horario.objects.filter(curso__protoCurso=protocurso.id)
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
	return render_to_response('detalle_curso.html',{ 'protocurso':protocurso, 'curso':curso,'temario':padres_hijos, 'horario':horario },context_instance = RequestContext(request))


def material(request,id_subtema):
	material = Material.objects.filter(tema_id=id_subtema)
	return render_to_response('material.html',{'material':material},context_instance = RequestContext(request))

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
		formulario = EditarUser(request.POST, request.FILES, instance = usuario)
		if formulario.is_valid:
			print formulario
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


def preguntas_curso(request,id_curso):
	usuario=request.user
	pregunta=Pregunta.objects.filter(curso_id=id_curso)
	respuesta=Respuesta.objects.all()

	return render_to_response('preg_resp.html', {'usuario':usuario,'pregunta':pregunta,'respuesta':respuesta}, context_instance=RequestContext(request))

def form_pregunta(request,id_curso):
	usuario=request.user
	if request.method=='POST':
		alumno=Alumno.objects.get(usuario_id=usuario.id)
		Pregunta.objects.create(curso_id=id_curso,pregunta=request.POST['pregunta'],alumno_id=alumno.id)
	return render_to_response('preguntar.html', {'usuario':usuario},context_instance=RequestContext(request))


def responder(request,id_curso):
	usuario=request.user
	if request.method=='POST':
		Respuesta.objects.create(respuesta=request.POST['respuesta'],usuario_log_id=usuario.id,pregunta_id=request.POST['pregunta'])
	pregunta=Pregunta.objects.filter(curso_id=id_curso)
	return render_to_response('responder.html', {'pregunta':pregunta,'usuario':usuario},context_instance=RequestContext(request))


def examen(request,id_curso):
	usuario=request.user
	examen=PreguntaExamen.objects.filter(curso_id=id_curso).order_by('?')[:1]
	ex=[x.id for x in examen]
	alternativas=Alternativa.objects.filter(pregunta_id=ex[0]).order_by('?')
	return render_to_response('examen.html', {'examen':examen,'alternativas':alternativas,'usuario':usuario},context_instance=RequestContext(request))


def profesores(request):
	profesores = Profesor.objects.all()
	return render_to_response('profesores.html', {'profesores':profesores}, context_instance=RequestContext(request))

def alumnos(request):
	alumnos = Alumno.objects.all()
	return render_to_response('alumnos.html', {'alumnos':alumnos}, context_instance=RequestContext(request))
     
def descargar(request,pathy):
	path="Qaysen_Dojo/cargas/"+pathy+""
	response = HttpResponse(mimetype='application/pdf')
	response['Content-Disposition'] = 'attachment; filename='+pathy+''
	with open(path, 'rb') as fichero: contenido = fichero.read()
	response.write(contenido)
	return response

def pdf(request):	
	response = HttpResponse(mimetype='application/pdf')
	response['Content-Disposition'] = 'attachment; filename=hello.pdf'
	p=canvas.Canvas(response)

	p.drawString(0,800,"Hello Word")
	p.showPage()
	p.save()
	return response

def ver(request,path):
	print path
	return render_to_response('ver.html', {'path':path} ,context_instance=RequestContext(request))
