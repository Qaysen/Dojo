from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^cursos/$','principal.views.cursos'),
	url(r'^cursos/(?P<id_curso_ab>\d+)$','principal.views.dato_curso_abierto'),
	url(r'^cursos/tema/(?P<id_subtema>\d+)$','principal.views.material')

)


