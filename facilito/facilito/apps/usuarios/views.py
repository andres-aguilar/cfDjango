import json

from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy

from rest_framework.views import APIView

from facilito.apps.usuarios.forms import RegistroForm
from facilito.apps.usuarios.serializers import UserSerializer


class RegistroUsuario(CreateView):
    model = User
    template_name = 'usuarios/registrar.html'
    form_class = RegistroForm
    success_url = reverse_lazy('mascotas:mascota_listar')


class UserAPI(APIView):
    serializer = UserSerializer

    def get(self, request, format=None):
        lista = User.objects.all()
        response = self.serializer(lista, many=True)

        return HttpResponse(json.dumps(response.data), content_type='application/json')