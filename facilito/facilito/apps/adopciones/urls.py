from django.conf.urls import url
from facilito.apps.adopciones.views import index

urlpatterns = [
    url(r'^$', index),
]
