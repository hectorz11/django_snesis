from django.shortcuts import render_to_response
from django.template import RequestContext
from snesis.apps.page.models import *
from snesis.apps.home.forms import *
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.models import User
from django.core.paginator import Paginator,EmptyPage,InvalidPage
from django.contrib.auth.decorators import login_required

from snesis.settings import URL_LOGIN
import simplejson

def index_view(request):
	return render_to_response('home/index.html',context_instance=RequestContext(request))

@login_required(login_url=URL_LOGIN)
def docentes_view(request,pagina):
	if request.method == "POST":
		if "docente_id" in request.POST:
			try:
				id_docente = request.POST['docente_id']
				p = Docente.objects.get(pk=id_docente)
				mensaje = {"status":"True","docente_id":p.id}
				p.delete()
				return HttpResponse(simplejson.dumps(mensaje),mimetype='application/json')
			except:
				mensaje = {"status":"False"}
	lista_doc = Docente.objects.filter(control=True)
	paginator = Paginator(lista_doc,5)
	try:
		page = int(pagina)
	except:
		page = 1
	try:
		docentes = paginator.page(page)
	except (EmptyPage,InvalidPage):
		docentes = paginator.page(paginator.num_pages)
	ctx = {'docentes':docentes}
	return render_to_response('home/docentes.html',ctx,context_instance=RequestContext(request))

@login_required(login_url=URL_LOGIN)
def alumnos_view(request,pagina):
	if request.method == "POST":
		if "alumno_id" in request.POST:
			try:
				id_alumno = request.POST['alumno_id']
				p = Alumno.objects.get(pk=id_alumno)
				mensaje = {"status":"True","alumno_id":p.id}
				p.delete()
				return HttpResponse(simplejson.dumps(mensaje),mimetype='application/json')
			except:
				mensaje = {"status":"False"}
	lista_alu = Alumno.objects.filter(control=True)
	paginator = Paginator(lista_alu,5)
	try:
		page = int(pagina)
	except:
		page = 1
	try:
		alumnos = paginator.page(page)
	except (EmptyPage,InvalidPage):
		alumnos = paginator.page(paginator.num_pages)
	ctx = {'alumnos':alumnos}
	return render_to_response('home/alumnos.html',ctx,context_instance=RequestContext(request))

@login_required(login_url=URL_LOGIN)
def cursos_view(request,pagina):
	if request.method == "POST":
		if "curso_id" in request.POST:
			try:
				id_curso = request.POST['curso_id']
				p = Curso.objects.get(pk=id_curso)
				mensaje = {"status":"True","curso_id":p.id}
				p.delete()
				return HttpResponse(simplejson.dumps(mensaje),mimetype='application/json')
			except:
				mensaje = {"status":"False"}
	lista_alu = Curso.objects.filter(control=True)
	paginator = Paginator(lista_alu,5)
	try:
		page = int(pagina)
	except:
		page = 1
	try:
		cursos = paginator.page(page)
	except (EmptyPage,InvalidPage):
		cursos = paginator.page(paginator.num_pages)
	ctx = {'cursos':cursos}
	return render_to_response('home/cursos.html',ctx,context_instance=RequestContext(request))

@login_required(login_url=URL_LOGIN)
def silabos_view(request,pagina):
	if request.method == "POST":
		if "silabo_id" in request.POST:
			try:
				id_silabo = request.POST['silabo_id']
				p = Silabo.objects.get(pk=id_silabo)
				mensaje = {"control":"True","silabo_id":p.id}
				p.delete()
			except:
				mensaje = {"control":"False"}
	lista_sil = Silabo.objects.filter(control=True)
	paginator = Paginator(lista_sil,5)
	try:
		page = int(pagina)
	except:
		page = 1
	try:
		silabos = paginator.page(page)
	except (EmptyPage,InvalidPage):
		silabos = paginator.page(paginator.num_pages)
	ctx = {'silabos':silabos}
	return render_to_response('home/silabos.html',ctx,context_instance=RequestContext(request))

@login_required(login_url=URL_LOGIN)
def unidades_view(request,pagina):
	if request.method == "POST":
		if "unidad_id" in request.POST:
			try:
				id_unidad = request.POST['unidad_id']
				p = Unidad.objects.get(pk=id_unidad)
				mensaje = {"control":"True","unidad_id":p.id}
				p.delete()
			except:
				mensaje = {"control":"False"}
	lista_uni = Unidad.objects.filter(control=True)
	paginator = Paginator(lista_uni,5)
	try:
		page = int(pagina)
	except:
		page = 1
	try:
		unidades = paginator.page(page)
	except (EmptyPage,InvalidPage):
		unidades = paginator.page(paginator.num_pages)
	ctx = {'unidades':unidades}
	return render_to_response('home/unidades.html',ctx,context_instance=RequestContext(request))

@login_required(login_url=URL_LOGIN)
def criterios_view(request,pagina):
	if request.method == "POST":
		if "criterio_id" in request.POST:
			try:
				id_criterio = request.POST['criterio_id']
				p = Criterio.objects.get(pk=id_criterio)
				mensaje = {"control":"True","criterio_id":p.id}
				p.delete()
			except:
				mensaje = {"control":"False"}
	lista_cri = Criterio.objects.filter(control=True)
	paginator = Paginator(lista_cri,5)
	try:
		page = int(pagina)
	except:
		page = 1
	try:
		criterios = paginator.page(page)
	except (EmptyPage,InvalidPage):
		criterios = paginator.page(paginator.num_pages)
	ctx = {'criterios':criterios}
	return render_to_response('home/criterios.html',ctx,context_instance=RequestContext(request))

@login_required(login_url=URL_LOGIN)
def matriculas_view(request,pagina):
	if request.method == "POST":
		if "matricula_id" in request.POST:
			try:
				id_matricula = request.POST['matricula_id']
				p = Matricula.objects.get(pk=id_matricula)
				mensaje = {"control":"True","matricula_id":p.id}
				p.delete()
			except:
				mensaje = {"control":"False"}
	lista_mat = Matricula.objects.filter(control=True)
	paginator = Paginator(lista_mat,5)
	try:
		page = int(pagina)
	except:
		page = 1
	try:
		matriculas = paginator.page(page)
	except (EmptyPage,InvalidPage):
		matriculas = paginator.page(paginator.num_pages)
	ctx = {'matriculas':matriculas}
	return render_to_response('',ctx,context_instance=RequestContext(request))

@login_required(login_url=URL_LOGIN)
def notas_view(request,pagina):
	if request.method == "POST":
		if "nota_id" in request.POST:
			try:
				id_nota = request.POST['nota_id']
				p = Nota.objects.get(pk=id_nota)
				mensaje = {"control":"True","nota_id":p.id}
				p.delete()
			except:
				mensaje = {"control":"False"}
	lista_not = Nota.objects.filter(control=True)
	paginator = Paginator(lista_not,5)
	try:
		page = int(pagina)
	except:
		page = 1
	try:
		notas = paginator.page(page)
	except (EmptyPage,InvalidPage):
		notas = paginator.page(paginator.num_pages)
	ctx = {'notas':notas}
	return render_to_response('home/notas.html',ctx,context_instance=RequestContext(request))

def login_view(request):
	mensaje = ""
	if request.user.is_authenticated():
		return HttpResponseRedirect('/')
	else:
		if request.method == "POST":
			form = LoginForm(request.POST)
			if form.is_valid():
				next = request.POST['next']
				username = form.cleaned_data['username']
				password = form.cleaned_data['password']
				usuario = authenticate(username=username,password=password)
				if usuario is not None and usuario.is_active:
					login(request,usuario)
					return HttpResponseRedirect(next)
				else:
					mensaje = "usuario y/o password incorrecto"
		next = request.REQUEST.get('next')
		form = LoginForm()
		ctx = {'form':form,'mensaje':mensaje,'next':next}
		return render_to_response('home/login.html',ctx,context_instance=RequestContext(request))

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')

def register_view(request):
	form = RegisterForm()
	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			email = form.cleaned_data['email']
			password_one = form.cleaned_data['password_one']
			password_two = form.cleaned_data['password_two']
			u = User.objects.create_user(username=username,email=email,password=password_one)
			u.save()
			return render_to_response('home/thanks_register.html',context_instance=RequestContext(request))
		else:
			ctx = {'form':form}
			return render_to_response('home/register.html',ctx,context_instance=RequestContext(request))
	ctx = {'form':form}
	return render_to_response('home/register.html',ctx,context_instance=RequestContext(request))

def singleDocente_view(request,id_doc):
	if request.method == "POST":
		if "silabo_id" in request.POST:
			try:
				id_silabo = request.POST['silabo_id']
				p = Silabo.objects.get(pk=id_silabo)
				mensaje = {"status":"True","silabo_id":p.id}
				p.delete()
				return HttpResponse(simplejson.dumps(mensaje),mimetype='application/json')
			except:
				mensaje = {"status":"False"}
	prod = Docente.objects.get(id=id_doc)
	valor1 = prod.silabo_set.all
	#resultados = curso.fetchall()
	ctx = {'docente':prod,'resultados':valor1}
	return render_to_response('home/singleDocente.html',ctx,context_instance=RequestContext(request))

def singleAlumno_view(request,id_alu):
	prod = Alumno.objects.get(id=id_alu)
	valor1 = prod.matricula_set.all
	valor3 = Nota.objects.extra(select={"nota_total":"select distinct avg(nota) from page_nota n inner join page_matricula m on m.id=n.matricula_id inner join page_curso c on c.id=m.curso_id inner join page_alumno a on m.alumno_id="+id_alu},)
	ctx = {'alumno':prod,'resultados':valor1,'valor':valor3}
	return render_to_response('home/singleAlumno.html',ctx,context_instance=RequestContext(request))

def singleSilabo_view(request,id_sil):
	if request.method == "POST":
		if "unidad_id" in request.POST:
			try:
				id_unidad = request.POST['unidad_id']
				p = Unidad.objects.get(pk=id_unidad)
				mensaje = {"status":"True","unidad_id":p.id}
				p.delete()
				return HttpResponse(simplejson.dumps(mensaje),mimetype='application/json')
			except:
				mensaje = {"status":"False"}
	prod = Silabo.objects.get(id=id_sil)
	valor1 = prod.unidad_set.all
	ctx = {'silabo':prod,'resultados':valor1}
	return render_to_response('home/singleSilabo.html',ctx,context_instance=RequestContext(request))

def singleCurso_view(request,id_cur):
	prod = Curso.objects.get(id=id_cur)
	valor1 = prod.silabo_set.all
	valor2 = prod.matricula_set.all
	valor3 = Nota.objects.extra(select={"nota_total":"select distinct avg(nota) from page_nota n inner join page_matricula m on m.id=n.matricula_id inner join page_curso c on m.curso_id ="+id_cur},)
	ctx = {'curso':prod,'resultados':valor1,'resultados2':valor2,'valor':valor3}
	return render_to_response('home/singleCurso.html',ctx,context_instance=RequestContext(request))

def singleUnidad_view(request,id_uni):
	if request.method == "POST":
		if "criterio_id" in request.POST:
			try:
				id_criterio = request.POST['criterio_id']
				p = Criterio.objects.get(pk=id_criterio)
				mensaje = {"status":"True","criterio_id":p.id}
				p.delete()
				return HttpResponse(simplejson.dumps(mensaje),mimetype='application/json')
			except:
				mensaje = {"status":"False"}
	prod = Unidad.objects.get(id=id_uni)
	valor1 = prod.criterio_set.all
	ctx = {'unidad':prod,'resultados':valor1}
	return render_to_response('home/singleUnidad.html',ctx,context_instance=RequestContext(request))

def singleCriterio_view(request,id_cri):
	if request.method == "POST":
		if "nota_id" in request.POST:
			try:
				id_nota = request.POST['nota_id']
				p = Nota.objects.get(pk=id_nota)
				mensaje = {"status":"True","nota_id":p.id}
				p.delete()
				return HttpResponse(simplejson.dumps(mensaje),mimetype='application/json')
			except:
				mensaje = {"status":"False"}
	prod = Criterio.objects.get(id=id_cri)
	valor1 = prod.nota_set.all
	ctx = {'criterio':prod,'resultados':valor1}
	return render_to_response('home/singleCriterio.html',ctx,context_instance=RequestContext(request))

def singleNota_view(request,id_not):
	prod = Nota.objects.get(id=id_not)
	ctx = {'nota':prod}
	return render_to_response('home/singleNota.html',ctx,context_instance=RequestContext(request))