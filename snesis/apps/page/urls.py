from django.conf.urls.defaults import patterns,url

urlpatterns = patterns('snesis.apps.page.views',
	url(r'^add/docente/$','add_docente_view',name="vista_agregar_docente"),
	url(r'^add/alumno/$','add_alumno_view',name="vista_agregar_alumno"),
	url(r'^add/curso/$','add_curso_view',name="vista_agregar_curso"),
	url(r'^add/silabo/$','add_silabo_view',name="vista_agregar_silabo"),
	url(r'^add/unidad/$','add_unidad_view',name="vista_agregar_unidad"),
	url(r'^add/criterio/$','add_criterio_view',name="vista_agregar_criterio"),
	url(r'^add/nota/$','add_nota_view',name="vista_agregar_nota"),
	url(r'^edit/docente/(?P<id_doc>.*)/$','edit_docente_view',name="vista_editar_docente"),
	url(r'^edit/alumno/(?P<id_alu>.*)/$','edit_alumno_view',name="vista_editar_alumno"),
	url(r'^edit/curso/(?P<id_cur>.*)/$','edit_curso_view',name="vista_editar_curso"),
	url(r'^edit/silabo/(?P<id_sil>.*)/$','edit_silabo_view',name="vista_editar_silabo"),
	url(r'^edit/unidad/(?P<id_uni>.*)/$','edit_unidad_view',name="vista_editar_unidad"),
	url(r'^edit/criterio/(?P<id_cri>.*)/$','edit_criterio_view',name="vista_editar_criterio"),
	url(r'^edit/nota/(?P<id_not>.*)/$','edit_nota_view',name="vista_editar_nota"),

)