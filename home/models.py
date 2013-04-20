from django.db import models
from django.contrib.auth.models import User

GENERO = (
	('Masculino','Masculino'),
	('Femenino','Femenino')
)

class userProfile(models.Model):

	def url(self,filename):
		ruta ="fotos/User/%s/%s"%(self.user.username,filename)
		return ruta

	user 	= models.OneToOneField(User)
	foto   		= models.ImageField(upload_to=url)
	genero  	= models.CharField(null=True,blank=True,choices=GENERO,max_length=30)
	direccion	= models.CharField(null=True,blank=True,max_length=300)
	telefono	= models.CharField(null=True,blank=True,max_length=10)
	git 		= models.CharField(null=True,blank=True,max_length=100)
	face 		= models.CharField(null=True,blank=True,max_length=100)
	twitter 	= models.CharField(null=True,blank=True,max_length=100)
	def __unicode__(self):
		return self.user.username