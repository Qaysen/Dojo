from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^media/(?P<path>.*)$','django.views.static.serve',
		{'document_root':settings.MEDIA_ROOT,}
	),
	# Pagina de Inicio
	url(r'^$', 'principal.views.inicio'),
	url(r'^registrar/$', 'principal.views.registrarse'),
	url(r'^settings/perfil/$', 'principal.views.actualizar_perfil'),
	url(r'^settings/password/$', 'principal.views.actualizar_password'),
	#url(r'^$','principal.views.home'),
	url(r'^cursos/$','principal.views.cursos'),
	url(r'^cursos/(?P<id_curso_ab>\d+)$','principal.views.dato_curso_abierto'),
	url(r'^cerrar/$','principal.views.cerrar'),




	url(r'^(?P<username>[-\w]+)/$','principal.views.perfil'),
    
)


