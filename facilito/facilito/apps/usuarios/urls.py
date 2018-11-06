from django.conf.urls import url

from facilito.apps.usuarios.views import RegistroUsuario, UserAPI

urlpatterns = [
    url(r'^registrar/$', RegistroUsuario.as_view(), name='registro'),
    url(r'^api/$', UserAPI.as_view(), name='api'),
]