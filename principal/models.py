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

	
class Alumno(models.Model):
	usuario=models.ForeignKey(User)

	def __unicode__(self):
		return unicode(self.usuario)

class Profesor(models.Model):
	usuario= models.ForeignKey(User)
	desc_laboral = models.CharField(max_length=100)
	profesion = models.CharField(max_length=100)
	git = models.CharField(max_length=100)
	face = models.CharField(max_length=100)
	twitter = models.CharField(max_length=100)

	def __unicode__(self):
		return unicode(self.usuario)

class Curso(models.Model):
	nombre = models.CharField(max_length=100)
	descripcion = models.CharField(max_length=200)
	url_imagen= models.CharField(max_length=100)
	def __unicode__(self):
		return unicode(self.nombre)		

class CursoAbierto(models.Model):
	lugar = models.CharField(max_length=100)
	fecha_inicio= models.DateField(auto_now=False)
	fecha_termino= models.DateField(auto_now=False)
	cant_horas=models.IntegerField(max_length=11,default=0)
	profesor =models.ForeignKey(Profesor)
	curso =models.ForeignKey(Curso)
	def __unicode__(self):
		return unicode(self.lugar)	

class Tema(models.Model):
	nombre=models.CharField(max_length=100)
	subtema=models.ForeignKey('Tema',blank=True,null=True)
	cursoabierto=models.ForeignKey(CursoAbierto)
	def __unicode__(self):
		return unicode(self.nombre)

class Material(models.Model):
	archivo_url=models.FileField(upload_to='material/')
	titulo=models.CharField(max_length=100)
	descripcion=models.CharField(max_length=100)
	tipo=models.CharField(max_length=100)
	tema =models.ForeignKey(Tema)
	def __unicode__(self):
		return unicode(self.nombre_archivo)

class PreguntaExamen(models.Model):
	curso =models.ForeignKey(Curso)
	pregunta = models.CharField(max_length=200)
	item1=models.CharField(max_length=50)
	item2=models.CharField(max_length=50)
	item3=models.CharField(max_length=50)
	item4=models.CharField(max_length=50)
	def __unicode__(self):
		return unicode(self.pregunta)

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
	dias = (
		('Lunes','Lunes'),
		('Martes','Martes'),
		('Miercoles','Miercoles'),
		('Jueves','Jueves'),
		('Viernes','Viernes'),
		('Sabado','Sabado'),
		('Domingo','Domingo')
	)
	dia=models.CharField(choices=dias,max_length=12)
	hora_inicio=models.TimeField(auto_now=False)
	hora_fin=models.TimeField(auto_now=False)
	cursoabierto=models.ForeignKey(CursoAbierto)
	def __unicode__(self):
		return '%s / %s' %(self.dia, self.hora_inicio)


class Matriculado(models.Model):
	cursoabierto=models.ForeignKey(CursoAbierto)
	alumno=models.ForeignKey(Alumno)
	def __unicode__(self):
		return '%s en %s' %(self.cursoabierto, self.alumno)

class Pregunta(models.Model):
	curso=models.ForeignKey(Curso)
	alumno=models.ForeignKey(User)
	pregunta = models.CharField(max_length=300)
	def __unicode__(self):
		return self.pregunta

class Respuesta(models.Model):
	pregunta=models.ForeignKey(Pregunta)
	usuario_log=models.ForeignKey(User)
	respuesta= models.CharField(max_length=200)
	def __unicode__(self):
		return self.respuesta






