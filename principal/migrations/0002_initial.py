# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Alumno'
        db.create_table('principal_alumno', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('usuario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('sobre_mi', self.gf('django.db.models.fields.CharField')(max_length=5000, null=True, blank=True)),
        ))
        db.send_create_signal('principal', ['Alumno'])

        # Adding model 'Profesor'
        db.create_table('principal_profesor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('usuario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('desc_laboral', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('profesion', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('principal', ['Profesor'])

        # Adding model 'ProtoCurso'
        db.create_table('principal_protocurso', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('tipo', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('archivo_url', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=100)),
            ('nivel', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=1)),
        ))
        db.send_create_signal('principal', ['ProtoCurso'])

        # Adding model 'Localizacion'
        db.create_table('principal_localizacion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('departamento', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('distrito', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('google_map', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('principal', ['Localizacion'])

        # Adding model 'Curso'
        db.create_table('principal_curso', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha_inicio', self.gf('django.db.models.fields.DateField')()),
            ('fecha_termino', self.gf('django.db.models.fields.DateField')()),
            ('cant_horas', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=3)),
            ('profesor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Profesor'])),
            ('protoCurso', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.ProtoCurso'])),
            ('localizacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Localizacion'])),
            ('precio', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=3)),
        ))
        db.send_create_signal('principal', ['Curso'])

        # Adding model 'Categoria'
        db.create_table('principal_categoria', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
        ))
        db.send_create_signal('principal', ['Categoria'])

        # Adding model 'CategoriaProtoCurso'
        db.create_table('principal_categoriaprotocurso', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('protoCurso', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.ProtoCurso'])),
            ('categoria', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Categoria'])),
        ))
        db.send_create_signal('principal', ['CategoriaProtoCurso'])

        # Adding model 'Tema'
        db.create_table('principal_tema', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('subtema', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Tema'], null=True, blank=True)),
            ('protoCurso', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.ProtoCurso'])),
            ('orden', self.gf('django.db.models.fields.DecimalField')(max_digits=2, decimal_places=0)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('principal', ['Tema'])

        # Adding model 'Material'
        db.create_table('principal_material', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('archivo_url', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('tipo', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('tema', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Tema'])),
        ))
        db.send_create_signal('principal', ['Material'])

        # Adding model 'PreguntaExamen'
        db.create_table('principal_preguntaexamen', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('protoCurso', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.ProtoCurso'])),
            ('pregunta', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('principal', ['PreguntaExamen'])

        # Adding model 'Alternativa'
        db.create_table('principal_alternativa', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pregunta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.PreguntaExamen'])),
            ('alternativa', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('estado', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('principal', ['Alternativa'])

        # Adding model 'Paquete'
        db.create_table('principal_paquete', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('principal', ['Paquete'])

        # Adding model 'ProtoCursoPaquete'
        db.create_table('principal_protocursopaquete', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('protoCurso', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.ProtoCurso'])),
            ('paquete', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Paquete'])),
        ))
        db.send_create_signal('principal', ['ProtoCursoPaquete'])

        # Adding model 'Horario'
        db.create_table('principal_horario', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('dia', self.gf('django.db.models.fields.CharField')(max_length=12)),
            ('hora_inicio', self.gf('django.db.models.fields.TimeField')()),
            ('hora_fin', self.gf('django.db.models.fields.TimeField')()),
            ('curso', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Curso'])),
        ))
        db.send_create_signal('principal', ['Horario'])

        # Adding model 'Matriculado'
        db.create_table('principal_matriculado', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('protoCurso', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.ProtoCurso'])),
            ('alumno', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Alumno'])),
        ))
        db.send_create_signal('principal', ['Matriculado'])

        # Adding model 'Pregunta'
        db.create_table('principal_pregunta', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('protoCurso', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.ProtoCurso'])),
            ('alumno', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Alumno'])),
            ('pregunta', self.gf('django.db.models.fields.CharField')(max_length=300)),
        ))
        db.send_create_signal('principal', ['Pregunta'])

        # Adding model 'Respuesta'
        db.create_table('principal_respuesta', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pregunta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Pregunta'])),
            ('usuario_log', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('respuesta', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('principal', ['Respuesta'])


    def backwards(self, orm):
        # Deleting model 'Alumno'
        db.delete_table('principal_alumno')

        # Deleting model 'Profesor'
        db.delete_table('principal_profesor')

        # Deleting model 'ProtoCurso'
        db.delete_table('principal_protocurso')

        # Deleting model 'Localizacion'
        db.delete_table('principal_localizacion')

        # Deleting model 'Curso'
        db.delete_table('principal_curso')

        # Deleting model 'Categoria'
        db.delete_table('principal_categoria')

        # Deleting model 'CategoriaProtoCurso'
        db.delete_table('principal_categoriaprotocurso')

        # Deleting model 'Tema'
        db.delete_table('principal_tema')

        # Deleting model 'Material'
        db.delete_table('principal_material')

        # Deleting model 'PreguntaExamen'
        db.delete_table('principal_preguntaexamen')

        # Deleting model 'Alternativa'
        db.delete_table('principal_alternativa')

        # Deleting model 'Paquete'
        db.delete_table('principal_paquete')

        # Deleting model 'ProtoCursoPaquete'
        db.delete_table('principal_protocursopaquete')

        # Deleting model 'Horario'
        db.delete_table('principal_horario')

        # Deleting model 'Matriculado'
        db.delete_table('principal_matriculado')

        # Deleting model 'Pregunta'
        db.delete_table('principal_pregunta')

        # Deleting model 'Respuesta'
        db.delete_table('principal_respuesta')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'principal.alternativa': {
            'Meta': {'object_name': 'Alternativa'},
            'alternativa': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'estado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pregunta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['principal.PreguntaExamen']"})
        },
        'principal.alumno': {
            'Meta': {'object_name': 'Alumno'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sobre_mi': ('django.db.models.fields.CharField', [], {'max_length': '5000', 'null': 'True', 'blank': 'True'}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'principal.categoria': {
            'Meta': {'object_name': 'Categoria'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        'principal.categoriaprotocurso': {
            'Meta': {'object_name': 'CategoriaProtoCurso'},
            'categoria': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['principal.Categoria']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'protoCurso': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['principal.ProtoCurso']"})
        },
        'principal.curso': {
            'Meta': {'object_name': 'Curso'},
            'cant_horas': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '3'}),
            'fecha_inicio': ('django.db.models.fields.DateField', [], {}),
            'fecha_termino': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'localizacion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['principal.Localizacion']"}),
            'precio': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '3'}),
            'profesor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['principal.Profesor']"}),
            'protoCurso': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['principal.ProtoCurso']"})
        },
        'principal.horario': {
            'Meta': {'object_name': 'Horario'},
            'curso': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['principal.Curso']"}),
            'dia': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'hora_fin': ('django.db.models.fields.TimeField', [], {}),
            'hora_inicio': ('django.db.models.fields.TimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'principal.localizacion': {
            'Meta': {'object_name': 'Localizacion'},
            'departamento': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'distrito': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'google_map': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'principal.material': {
            'Meta': {'object_name': 'Material'},
            'archivo_url': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tema': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['principal.Tema']"}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'principal.matriculado': {
            'Meta': {'object_name': 'Matriculado'},
            'alumno': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['principal.Alumno']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'protoCurso': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['principal.ProtoCurso']"})
        },
        'principal.paquete': {
            'Meta': {'object_name': 'Paquete'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'principal.pregunta': {
            'Meta': {'object_name': 'Pregunta'},
            'alumno': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['principal.Alumno']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pregunta': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'protoCurso': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['principal.ProtoCurso']"})
        },
        'principal.preguntaexamen': {
            'Meta': {'object_name': 'PreguntaExamen'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pregunta': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'protoCurso': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['principal.ProtoCurso']"})
        },
        'principal.profesor': {
            'Meta': {'object_name': 'Profesor'},
            'desc_laboral': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'profesion': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'principal.protocurso': {
            'Meta': {'object_name': 'ProtoCurso'},
            'archivo_url': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nivel': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'principal.protocursopaquete': {
            'Meta': {'object_name': 'ProtoCursoPaquete'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'paquete': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['principal.Paquete']"}),
            'protoCurso': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['principal.ProtoCurso']"})
        },
        'principal.respuesta': {
            'Meta': {'object_name': 'Respuesta'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pregunta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['principal.Pregunta']"}),
            'respuesta': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'usuario_log': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'principal.tema': {
            'Meta': {'object_name': 'Tema'},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'orden': ('django.db.models.fields.DecimalField', [], {'max_digits': '2', 'decimal_places': '0'}),
            'protoCurso': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['principal.ProtoCurso']"}),
            'subtema': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['principal.Tema']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['principal']