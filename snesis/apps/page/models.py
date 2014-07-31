from django.db import models
from snesis.apps.home.models import UserProfile

class Docente(models.Model):
	nombres = models.CharField(max_length=70,verbose_name='Nombre(s)')
	apellidos = models.CharField(max_length=70)
	cargo = models.CharField(max_length=45)
	profesion = models.CharField(max_length=45)
	grado = models.CharField(max_length=45)
	control = models.BooleanField(default=True)
	user = models.OneToOneField(UserProfile)

	def __unicode__(self):
		nombreCompleto = "%s %s"%(self.nombres,self.apellidos)
		return nombreCompleto

class Alumno(models.Model):
	codigo = models.CharField(max_length=12)
	nombres = models.CharField(max_length=70,verbose_name='Nombre(s)')
	apellidos = models.CharField(max_length=70)
	fecha_nac = models.DateField()
	correo = models.EmailField()
	control = models.BooleanField(default=True)

	def __unicode__(self):
		nombreCompleto = "%s %s"%(self.nombres,self.apellidos)
		return nombreCompleto

class Curso(models.Model):

	STATUS_CHOICES = (
		('I Semestre',('I Semestre')),
		('II Semestre',('II Semestre')),)

	nombre = models.CharField(max_length=120,verbose_name='Curso')
	semestre = models.CharField(max_length=45,choices=STATUS_CHOICES,default=1)
	creditos = models.IntegerField()
	control = models.BooleanField(default=True)

	def __unicode__(self):
		return self.nombre

class Silabo(models.Model):

	STATUS_CHOICES = (
		('1ro',('1ro')),
		('2do',('2do')),
		('3ro',('3ro')),
		('4to',('4to')),
		('5to',('5to')),)

	descripcion = models.CharField(max_length=120,verbose_name='Silabo')
	anio_academico = models.CharField(max_length=5,choices=STATUS_CHOICES,default=1)
	docente = models.ForeignKey(Docente)
	curso = models.ForeignKey(Curso)
	control = models.BooleanField(default=True)

	def __unicode__(self):
		return self.descripcion

class Unidad(models.Model):

	STATUS_CHOICES = (
		('Unidad I',('Unidad I')),
		('Unidad II',('Unidad II')),
		('Unidad III',('Unidad III')),
		('Unidad IV',('Unidad IV')),)

	descripcion = models.CharField(max_length=120,verbose_name="Unidad",choices=STATUS_CHOICES,default=1)
	porcentaje = models.IntegerField()
	silabo = models.ForeignKey(Silabo)
	control = models.BooleanField(default=True)

	def __unicode__(self):
		nombre = "%s %s"%(self.silabo.descripcion,self.descripcion)
		return nombre

class Criterio(models.Model):

	descripcion = models.CharField(max_length=120,verbose_name="Criterio")
	porcentaje = models.IntegerField()
	unidad = models.ForeignKey(Unidad)
	control = models.BooleanField(default=True)

	def __unicode__(self):
		nombre = "%s %s %s"%(self.unidad.silabo.descripcion,self.unidad.descripcion,self.descripcion)
		return nombre
		
class Matricula(models.Model):

	STATUS_CHOICES = (
		('1ro',('1ro')),
		('2do',('2do')),
		('3ro',('3ro')),
		('4to',('4to')),
		('5to',('5to')),)

	anio_academico = models.CharField(max_length=5,choices=STATUS_CHOICES,default=1)
	curso = models.ForeignKey(Curso)
	alumno = models.ForeignKey(Alumno)
	control = models.BooleanField(default=True)

	def __unicode__(self):
		nombre = "%s %s"%(self.alumno.apellidos,self.curso.nombre)
		return nombre

class Nota(models.Model):
	nota = models.IntegerField()
	criterio = models.ForeignKey(Criterio)
	matricula = models.ForeignKey(Matricula)
	control = models.BooleanField(default=True)

	def __unicode__(self):
		nombre = "%s %s %s %s"%(self.matricula.alumno.apellidos,self.criterio.unidad.silabo.descripcion,self.criterio.unidad.descripcion,self.criterio.descripcion)
		return nombre