from django.shortcuts import render_to_response
from django.template import RequestContext
from snesis.apps.page.forms import *
from snesis.apps.page.models import *
from django.http import HttpResponseRedirect,HttpResponse

def add_docente_view(request):
	info = "iniciando"
	if request.method == "POST":
		form = addDocenteForm(request.POST,request.FILES)
		if form.is_valid():
			add = form.save(commit=False)
			add.save()
			info = "Guardado satisfactoriamente"
			return HttpResponseRedirect('/docentes/page/1')
	else:
		form = addDocenteForm()
	ctx = {'form':form,'informacion':info}
	return render_to_response('page/addDocente.html',ctx,context_instance=RequestContext(request))

def add_alumno_view(request):
	info = "iniciando"
	if request.method == "POST":
		form = addAlumnoForm(request.POST,request.FILES)
		if form.is_valid():
			add = form.save(commit=False)
			add.save()
			info = "Guardado satisfactoriamente"
			return HttpResponseRedirect('/alumnos/page/1')
	else:
		form = addAlumnoForm()
	ctx = {'form':form,'informacion':info}
	return render_to_response('page/addAlumno.html',ctx,context_instance=RequestContext(request))

def add_curso_view(request):
	info = "iniciando"
	if request.method == "POST":
		form = addCursoForm(request.POST,request.FILES)
		if form.is_valid():
			add = form.save(commit=False)
			add.save()
			info = "Guardado satisfactoriamente"
			return HttpResponseRedirect('/cursos/page/1')
	else:
		form = addCursoForm()
	ctx = {'form':form,'informacion':info}
	return render_to_response('page/addCurso.html',ctx,context_instance=RequestContext(request))

def add_silabo_view(request):
	info = "iniciando"
	if request.method == "POST":
		form = addSilaboForm(request.POST,request.FILES)
		if form.is_valid():
			add = form.save(commit=False)
			add.save()
			info = "Guardado satisfactoriamente"
			return HttpResponseRedirect('/silabo/%s'%add.id)
	else:
		form = addSilaboForm()
	ctx = {'form':form,'informacion':info}
	return render_to_response('page/addSilabo.html',ctx,context_instance=RequestContext(request))

def add_unidad_view(request):
	info = "iniciando"
	if request.method == "POST":
		form = addUnidadForm(request.POST,request.FILES)
		if form.is_valid():
			add = form.save(commit=False)
			add.save()
			info = "Guardado satisfactoriamente"
			return HttpResponseRedirect('/unidad/%s'%add.id)
	else:
		form = addUnidadForm()
	ctx = {'form':form,'informacion':info}
	return render_to_response('page/addUnidad.html',ctx,context_instance=RequestContext(request))

def add_criterio_view(request):
	info = "iniciando"
	if request.method == "POST":
		form = addCriterioForm(request.POST,request.FILES)
		if form.is_valid():
			add = form.save(commit=False)
			add.save()
			info = "Guardado satisfactoriamente"
			return HttpResponseRedirect('/criterio/%s'%add.id)
	else:
		form = addCriterioForm()
	ctx = {'form':form,'informacion':info}
	return render_to_response('page/addCriterio.html',ctx,context_instance=RequestContext(request))

def add_nota_view(request):
	info = "iniciando"
	if request.method == "POST":
		form = addNotaForm(request.POST,request.FILES)
		if form.is_valid():
			add = form.save(commit=False)
			add.save()
			info = "Guardado satisfactoriamente"
			return HttpResponseRedirect('')
	else:
		form = addNotaForm()
	ctx = {'form':form,'informacion':info}
	return render_to_response('page/addNota.html',ctx,context_instance=RequestContext(request))

def edit_docente_view(request,id_doc):
	info = "iniciado"
	prod = Docente.objects.get(pk=id_doc)
	if request.method == "POST":
		form = addDocenteForm(request.POST,request.FILES,instance=prod)
		if form.is_valid():
			edit = form.save(commit=False)
			edit.save() # Guardamos el objeto
			info = "Correcto"
			return HttpResponseRedirect('/docentes/page/1')
	else:
		form = addDocenteForm(instance=prod)
	ctx = {'form':form, 'informacion':info}
	return render_to_response('page/editDocente.html',ctx,context_instance=RequestContext(request))

def edit_alumno_view(request,id_alu):
	info = "iniciado"
	prod = Alumno.objects.get(pk=id_alu)
	if request.method == "POST":
		form = addAlumnoForm(request.POST,request.FILES,instance=prod)
		if form.is_valid():
			edit = form.save(commit=False)
			edit.save() # Guardamos el objeto
			info = "Correcto"
			return HttpResponseRedirect('/alumnos/page/1')
	else:
		form = addAlumnoForm(instance=prod)
	ctx = {'form':form, 'informacion':info}
	return render_to_response('page/editAlumno.html',ctx,context_instance=RequestContext(request))

def edit_curso_view(request,id_cur):
	info = "iniciado"
	prod = Curso.objects.get(pk=id_cur)
	if request.method == "POST":
		form = addCursoForm(request.POST,request.FILES,instance=prod)
		if form.is_valid():
			edit = form.save(commit=False)
			edit.save() # Guardamos el objeto
			info = "Correcto"
			return HttpResponseRedirect('/cursos/page/1')
	else:
		form = addCursoForm(instance=prod)
	ctx = {'form':form, 'informacion':info}
	return render_to_response('page/editCurso.html',ctx,context_instance=RequestContext(request))

def edit_silabo_view(request,id_sil):
	info = "iniciado"
	prod = Silabo.objects.get(pk=id_sil)
	if request.method == "POST":
		form = addSilaboForm(request.POST,request.FILES,instance=prod)
		if form.is_valid():
			edit = form.save(commit=False)
			edit.save() # Guardamos el objeto
			info = "Correcto"
			return HttpResponseRedirect('/silabo/%s'%edit.id)
	else:
		form = addSilaboForm(instance=prod)
	ctx = {'form':form, 'informacion':info}
	return render_to_response('page/editSilabo.html',ctx,context_instance=RequestContext(request))

def edit_unidad_view(request,id_uni):
	info = "iniciado"
	prod = Unidad.objects.get(pk=id_uni)
	if request.method == "POST":
		form = addUnidadForm(request.POST,request.FILES,instance=prod)
		if form.is_valid():
			edit = form.save(commit=False)
			edit.save() # Guardamos el objeto
			info = "Correcto"
			return HttpResponseRedirect('/unidad/%s'%edit.id)
	else:
		form = addUnidadForm(instance=prod)
	ctx = {'form':form, 'informacion':info}
	return render_to_response('page/editUnidad.html',ctx,context_instance=RequestContext(request))

def edit_criterio_view(request,id_cri):
	info = "iniciado"
	prod = Criterio.objects.get(pk=id_cri)
	if request.method == "POST":
		form = addCriterioForm(request.POST,request.FILES,instance=prod)
		if form.is_valid():
			edit = form.save(commit=False)
			edit.save() # Guardamos el objeto
			info = "Correcto"
			return HttpResponseRedirect('/criterio/%s'%edit.id)
	else:
		form = addCriterioForm(instance=prod)
	ctx = {'form':form, 'informacion':info}
	return render_to_response('page/editCriterio.html',ctx,context_instance=RequestContext(request))

def edit_nota_view(request,id_not):
	info = "iniciado"
	prod = Nota.objects.get(pk=id_not)
	if request.method == "POST":
		form = addNotaForm(request.POST,request.FILES,instance=prod)
		if form.is_valid():
			edit = form.save(commit=False)
			edit.save() # Guardamos el objeto
			info = "Correcto"
			return HttpResponseRedirect('/nota/%s'%edit.id)
	else:
		form = addNotaForm(instance=prod)
	ctx = {'form':form, 'informacion':info}
	return render_to_response('page/editNota.html',ctx,context_instance=RequestContext(request))