from django.conf.urls import url
from facilito.apps.mascotas.views import index

urlpatterns = [
    url(r'^$', index),
]
