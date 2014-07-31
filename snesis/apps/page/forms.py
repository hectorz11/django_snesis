from django import forms
from snesis.apps.page.models import *

class addDocenteForm(forms.ModelForm):
	class Meta:
		model = Docente

class addAlumnoForm(forms.ModelForm):
	class Meta:
		model = Alumno

class addCursoForm(forms.ModelForm):
	class Meta:
		model = Curso

class addSilaboForm(forms.ModelForm):
	class Meta:
		model = Silabo

class addUnidadForm(forms.ModelForm):
	class Meta:
		model = Unidad

class addCriterioForm(forms.ModelForm):
	class Meta:
		model = Criterio

class addMatriculaForm(forms.ModelForm):
	class Meta:
		model = Matricula

class addNotaForm(forms.ModelForm):
	class Meta:
		model = Nota