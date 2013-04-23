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
	url(r'^loginto/', 'principal.views.loginto'),
	#url(r'^$','principal.views.home'),
	

	url(r'^cursos/$','principal.views.cursos'),
	url(r'^cursos/(?P<nomcurso>[-\w]+)/$','principal.views.detallecurso'),

	url(r'^seminarios/$','principal.views.seminarios'),
	url(r'^seminarios/(?P<nomcurso>[-\w]+)/$','principal.views.detallecurso'),
	# url(r'^(?P<pathy>.*)$', 'principal.views.ver'),
	url(r'^descargar/(?P<pathy>.*)$','principal.views.descargar'),
	url(r'^pdf/$', 'principal.views.pdf'),


	url(r'^cursos/preguntas/(?P<id_curso>\d+)$','principal.views.preguntas_curso'),
	url(r'^cursos/form_pre/(?P<id_curso>\d+)$','principal.views.form_pregunta'),
	url(r'^cursos/responder/(?P<id_curso>\d+)$','principal.views.responder'),
	url(r'^cursos/examen/(?P<id_curso>\d+)$','principal.views.examen'),
	# url(r'^cursos/(?P<id_curso_ab>\d+)$','principal.views.dato_curso_abierto'),

	url(r'^cursos/tema/(?P<id_subtema>\d+)$','principal.views.material'),
	url(r'^cerrar/$','principal.views.cerrar'),

	url(r'^profesores/$','principal.views.profesores'),

	url(r'^alumnos/$','principal.views.alumnos'),
	url(r'^contacto/$','principal.views.contacto'),
	url(r'^(?P<username>[-\w]+)/$','principal.views.perfil'),

)


