from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from facilito.apps.adopciones.views import index, SolicitudList, SolicitudCreate, SolicitudUpdate, SolicitudDelete

urlpatterns = [
    url(r'^$', index),
    url(r'^listar', login_required(SolicitudList.as_view()), name='solicitud_listar'),
    url(r'^crear', login_required(SolicitudCreate.as_view()), name='solicitud_crear'),
    url(r'^editar/(?P<pk>\d+)/$', login_required(SolicitudUpdate.as_view()), name='solicitud_editar'),
    url(r'^eliminar/(?P<pk>\d+)/$', login_required(SolicitudDelete.as_view()), name='solicitud_eliminar')
]
