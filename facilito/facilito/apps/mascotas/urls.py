from django.conf.urls import url
from facilito.apps.mascotas.views import index, mascota_view, mascota_list

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^nuevo$', mascota_view, name='mascota_view'),
    url(r'^listar$', mascota_list, name='mascota_listar')
]
