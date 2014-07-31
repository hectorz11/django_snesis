from django.conf.urls.defaults import patterns,url

urlpatterns = patterns('snesis.apps.home.views',
	url(r'^$','index_view',name='vista_principal'),
	url(r'^login/$','login_view',name='vista_login'),
	url(r'^logout/$','logout_view',name='vista_logout'),
	url(r'^registro/$','register_view',name='vista_registro'),
	url(r'^docentes/page/(?P<pagina>.*)/$','docentes_view',name='vista_docentes'),
	url(r'^alumnos/page/(?P<pagina>.*)/$','alumnos_view',name='vista_alumnos'),
	url(r'^cursos/page/(?P<pagina>.*)/$','cursos_view',name='vista_cursos'),
	url(r'^silabos/page/(?P<pagina>.*)/$','silabos_view',name='vista_silabos'),
	url(r'^unidades/page/(?P<pagina>.*)/$','unidades_view',name='vista_unidades'),
	url(r'^criterios/page/(?P<pagina>.*)/$','criterios_view',name='vista_criterios'),
	url(r'^matriculas/page/(?P<pagina>.*)/$','matriculas_view',name='vista_matriculas'),
	url(r'^notas/page/(?P<pagina>.*)/$','notas_view',name='vista_notas'),
	url(r'^docente/(?P<id_doc>.*)/$', 'singleDocente_view', name = 'vista_single_docente'),
	url(r'^alumno/(?P<id_alu>.*)/$', 'singleAlumno_view', name = 'vista_single_alumno'),
	url(r'^silabo/(?P<id_sil>.*)/$', 'singleSilabo_view', name = 'vista_single_silabo'),
	url(r'^curso/(?P<id_cur>.*)/$', 'singleCurso_view', name = 'vista_single_curso'),
	url(r'^unidad/(?P<id_uni>.*)/$', 'singleUnidad_view', name = 'vista_single_unidad'),
	url(r'^criterio/(?P<id_cri>.*)/$', 'singleCriterio_view', name = 'vista_single_criterio'),
	url(r'^nota/(?P<id_not>.*)/$', 'singleNota_view', name = 'vista_single_nota'),
)