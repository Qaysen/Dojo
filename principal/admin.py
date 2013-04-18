from principal.models import *
from django.contrib import admin

class AdminEntries(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ['nombre'] }

admin.site.register(Alumno)
admin.site.register(Profesor)
admin.site.register(ProtoCurso, AdminEntries)
admin.site.register(Categoria, AdminEntries)
admin.site.register(CategoriaProtoCurso)
admin.site.register(Curso)
admin.site.register(Material)
admin.site.register(PreguntaExamen)
admin.site.register(Alternativa)
admin.site.register(Paquete)
admin.site.register(ProtoCursoPaquete)
admin.site.register(Horario)
admin.site.register(Matriculado)
admin.site.register(Pregunta)
admin.site.register(Respuesta)
admin.site.register(Tema)





