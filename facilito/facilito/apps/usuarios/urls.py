from django.conf.urls import url

from facilito.apps.usuarios.views import RegistroUsuario

urlpatterns = [
    url(r'^registrar/$', RegistroUsuario.as_view(), name='registro'),
]