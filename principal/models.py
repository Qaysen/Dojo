from django.db import models
from django.contrib.auth.models import User

GENERO = (
	('Masculino','Masculino'),
	('Femenino','Femenino')
)

User.add_to_class('telefono', models.IntegerField(null=True,blank=True, max_length=7))
User.add_to_class('direccion', models.CharField(null=True,blank=True, max_length=500))
User.add_to_class('genero', models.CharField(null=True,blank=True, choices=GENERO, max_length=30))
User.add_to_class('foto', models.CharField(null=True,blank=True, max_length=500))
User.add_to_class('estado_login',models.BooleanField(default=False))

class PerfilUsuario(models.Model):
	TIPO=(
			('alumno','alumno'),
			('profesor','profesor'),
		)
	tipo = models.CharField(max_length=20,choices=TIPO)
	fecha_registro = models.DateField(auto_now=True) 
	estado = models.BooleanField()
	online = models.BooleanField()
	usuario =models.ForeignKey(User)

	def __unicode__(self):
		return '%s y %s' %(self.usuario,self.tipo)

class Curso(models.Model):
	nombre = models.CharField(max_length=100)
	silabo = models.CharField(max_length=100)
	def __unicode__(self):
		return unicode(self.nombre)		

class CursoAbierto(models.Model):
	lugar = models.CharField(max_length=100)
	fecha_inicio= models.DateField(auto_now=False)
	cant_horas=models.IntegerField(max_length=11,default=0)
	profesor =models.ForeignKey(User)
	curso =models.ForeignKey(Curso)
	def __unicode__(self):
		return unicode(self.lugar)	

class Material(models.Model):
	archivo_url=models.CharField(max_length=200)
	nombre_archivo=models.CharField(max_length=100)
	curso =models.ForeignKey(Curso)
	def __unicode__(self):
		return unicode(self.nombre_archivo)

class PreguntaExamen(models.Model):
	curso =models.ForeignKey(Curso)
	def __unicode__(self):
		return unicode(self.curso)

class Paquete(models.Model):
	nombre=models.CharField(max_length=100)
	def __unicode__(self):
		return unicode(self.nombre)

class CursoPaquete(models.Model):
	curso =models.ForeignKey(Curso)
	paquete =models.ForeignKey(Paquete)
	def __unicode__(self):
		return '%s en %s' %(self.curso, self.paquete)

class Horario(models.Model):
	dia=models.DateField(auto_now=False)
	hora=models.TimeField(auto_now=False)
	def __unicode__(self):
		return '%s / %s' %(self.dia, self.hora)


class Matriculado(models.Model):
	cursoabierto=models.ForeignKey(CursoAbierto)
	alumno=models.ForeignKey(User)
	def __unicode__(self):
		return self.cursoabierto

class Pregunta(models.Model):
	curso=models.ForeignKey(Curso)
	alumno=models.ForeignKey(User)
	def __unicode__(self):
		return self.curso

class Respuesta(models.Model):
	pregunta=models.ForeignKey(Pregunta)
	usuario_log=models.ForeignKey(User)
	def __unicode__(self):
		return self.pregunta

