from django.db import models
from django.contrib.auth.models import User
from django.template import defaultfilters

TIPO = (
	('Seminario','Seminario'),
	('Curso','Curso')
)

class Alumno(models.Model):
	usuario 	=models.ForeignKey(User)
	sobre_mi	=models.CharField(max_length=5000,null=True,blank=True)
	def __unicode__(self):
		return unicode(self.usuario)

class Profesor(models.Model):
	usuario= models.ForeignKey(User)
	desc_laboral = models.CharField(max_length=100)
	profesion = models.CharField(max_length=100)
	def __unicode__(self):
		return unicode(self.usuario)

class ProtoCurso(models.Model):
	nombre = models.CharField(max_length=100)
	descripcion = models.CharField(max_length=200)
	tipo=models.CharField(max_length=100, choices=TIPO)
	archivo_url=models.FileField(upload_to='logos/')
	slug = models.SlugField(max_length=100)
	nivel=models.IntegerField(max_length=1,default=0)

	def save(self, *args, **kwargs):
		self.slug = defaultfilters.slugify(self.nombre)
		super(ProtoCurso, self).save(*args, **kwargs)

	def __unicode__(self):
		return unicode(self.nombre)	


class Localizacion(models.Model):
	departamento = models.CharField(max_length=100)
	distrito = models.CharField(max_length=100)
	direccion = models.CharField(max_length=100)
	google_map = models.CharField(max_length=100)
		
	
	def __unicode__(self):
		return unicode(self.distrito)	
		
class Curso(models.Model):
	fecha_inicio= models.DateField(auto_now=False)
	fecha_termino= models.DateField(auto_now=False)
	cant_horas=models.IntegerField(max_length=3,default=0)	
	profesor =models.ForeignKey(Profesor)
	protoCurso =models.ForeignKey(ProtoCurso)
	localizacion =models.ForeignKey(Localizacion)
	precio=models.IntegerField(max_length=3,default=0)	
	
	def __unicode__(self):
		return '%s / %s' %(self.protoCurso, self.localizacion)


class Categoria(models.Model):
	nombre = models.CharField(max_length=100)
	slug = models.SlugField()

	def save(self, *args, **kwargs):
		self.slug = defaultfilters.slugify(self.nombre)
		super(Categoria, self).save(*args, **kwargs)

	def __unicode__(self):
		return unicode(self.nombre)	

class CategoriaProtoCurso(models.Model):
	protoCurso =models.ForeignKey(ProtoCurso)
	categoria =models.ForeignKey(Categoria)
	
	def __unicode__(self):
		return unicode(self.categoria)	

class Tema(models.Model):
	nombre=models.CharField(max_length=100)
	subtema=models.ForeignKey('Tema',blank=True,null=True)
	protoCurso=models.ForeignKey(ProtoCurso)
	orden=models.DecimalField(decimal_places=0, max_digits=2)
	descripcion=models.CharField(max_length=100)
	def __unicode__(self):
		return unicode(self.nombre)

class Material(models.Model):
	archivo_url=models.FileField(upload_to='material/')
	titulo=models.CharField(max_length=100)
	descripcion=models.CharField(max_length=100)
	tipo=models.CharField(max_length=100)
	tema =models.ForeignKey(Tema)
	def __unicode__(self):
		return unicode(self.titulo)

class PreguntaExamen(models.Model):
	protoCurso =models.ForeignKey(ProtoCurso)
	pregunta = models.CharField(max_length=200)
	def __unicode__(self):
		return unicode(self.pregunta)

class Alternativa(models.Model):
	pregunta =models.ForeignKey(PreguntaExamen)
	alternativa = models.CharField(max_length=200)
	estado=models.BooleanField()
	def __unicode__(self):
		return unicode(self.alternativa)

class Paquete(models.Model):
	nombre=models.CharField(max_length=100)
	def __unicode__(self):
		return unicode(self.nombre)

class ProtoCursoPaquete(models.Model):
	protoCurso =models.ForeignKey(ProtoCurso)
	paquete =models.ForeignKey(Paquete)
	def __unicode__(self):
		return '%s en %s' %(self.ProtoCurso, self.paquete)

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
	curso=models.ForeignKey(Curso)
	def __unicode__(self):
		return '%s / %s' %(self.dia, self.hora_inicio)


class Matriculado(models.Model):
	protoCurso=models.ForeignKey(ProtoCurso)
	alumno=models.ForeignKey(Alumno)
	def __unicode__(self):
		return '%s en %s' %(self.protoCurso, self.alumno)

class Pregunta(models.Model):
	protoCurso=models.ForeignKey(ProtoCurso)
	alumno=models.ForeignKey(Alumno)
	pregunta = models.CharField(max_length=300)
	def __unicode__(self):
		return self.pregunta

class Respuesta(models.Model):
	pregunta=models.ForeignKey(Pregunta)
	usuario_log=models.ForeignKey(User)
	respuesta= models.CharField(max_length=200)
	def __unicode__(self):
		return self.respuesta






