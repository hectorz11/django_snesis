from django.contrib import admin
from snesis.apps.page.models import Docente,Alumno,Curso,Silabo,Unidad,Criterio,Matricula,Nota

class DocenteAdmin(admin.ModelAdmin):
	list_display = ('apellidos','nombres','cargo','profesion','grado','control')
	list_filter = ('cargo','grado')
	fields = (('nombres','apellidos'),('profesion','grado'),('cargo','control'),'user')
	search_fields = ['apellidos','nombres','cargo']

class AlumnoAdmin(admin.ModelAdmin):
	list_display = ('apellidos','nombres','codigo','fecha_nac','correo','control')
	#list_filter = ('fecha_nac')
	fields = ('codigo',('nombres','apellidos'),'fecha_nac','correo','control')
	search_fields = ['apellidos','nombres','codigo']

class CursoAdmin(admin.ModelAdmin):
	list_display = ('nombre','semestre','creditos','control')
	list_filter = ('semestre','creditos')
	fields = (('nombre','semestre'),('creditos','control'))
	search_fields = ['nombre']

class SilaboAdmin(admin.ModelAdmin):
	list_display = ('descripcion','anio_academico','docente','curso','control')
	list_filter = ('docente','anio_academico')
	fields = ('descripcion','docente','curso',('anio_academico','control'))
	search_fields = ['curso','docente','anio_academico']

class UnidadAdmin(admin.ModelAdmin):
	list_display = ('descripcion','silabo','porcentaje','control')
	list_filter = ('descripcion',)
	fields = ('descripcion','silabo',('porcentaje','control'))
	search_fields = ('descripcion','silabo')

class CriterioAdmin(admin.ModelAdmin):
	list_display = ('descripcion','unidad','porcentaje','control')
	fields = ('descripcion','unidad',('porcentaje','control'))

class MatriculaAdmin(admin.ModelAdmin):
	list_display = ('alumno','curso','anio_academico','control')
	fields = ('alumno','curso',('anio_academico','control'))
	search_fields = ['curso','alumno']

class NotaAdmin(admin.ModelAdmin):
	list_display = ('matricula','criterio','nota','control')
	fields = ('matricula','criterio',('nota','control'))
	search_fields = ['matricula']

admin.site.register(Docente,DocenteAdmin)
admin.site.register(Alumno,AlumnoAdmin)
admin.site.register(Curso,CursoAdmin)
admin.site.register(Silabo,SilaboAdmin)
admin.site.register(Unidad,UnidadAdmin)
admin.site.register(Criterio,CriterioAdmin)
admin.site.register(Matricula,MatriculaAdmin)
admin.site.register(Nota,NotaAdmin)