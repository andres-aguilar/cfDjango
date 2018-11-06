from django.conf.urls import url
from facilito.apps.adopciones.views import index, SolicitudList, SolicitudCreate, SolicitudUpdate, SolicitudDelete

urlpatterns = [
    url(r'^$', index),
    url(r'^listar', SolicitudList.as_view(), name='solicitud_listar'),
    url(r'^crear', SolicitudCreate.as_view(), name='solicitud_crear'),
    url(r'^editar/(?P<pk>\d+)/$', SolicitudUpdate.as_view(), name='solicitud_editar'),
    url(r'^eliminar/(?P<pk>\d+)/$', SolicitudDelete.as_view(), name='solicitud_eliminar')
]
