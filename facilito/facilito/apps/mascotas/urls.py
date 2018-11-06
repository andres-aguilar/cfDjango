from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from facilito.apps.mascotas.views import index, mascota_view, mascota_list, mascota_edit, mascota_delete
from facilito.apps.mascotas.views import MascotaList, MascotaCreate, MascotaUpdate, MascotaDelete

from facilito.apps.mascotas.views import listado


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^nuevo$', login_required(MascotaCreate.as_view()), name='mascota_view'),
    url(r'^listar', login_required(MascotaList.as_view()), name='mascota_listar'),
    url(r'^editar/(?P<pk>\d+)/$', login_required(MascotaUpdate.as_view()), name='mascota_editar'),
    url(r'^eliminar/(?P<pk>\d+)/$', login_required(MascotaDelete.as_view()), name='mascota_eliminar'),
    url(r'^listado', listado, name='listado')
]
