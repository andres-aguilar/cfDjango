from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy

from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from facilito.apps.mascotas.models import Mascota
from facilito.apps.mascotas.forms import MascotaForm


def listado(request):
    lista = serializers.serialize('json', Mascota.objects.all(), 
        fields=['nombre', 'sexo', 'edad_aproximada', 'fecha_rescate'])
    return HttpResponse(lista, content_type='application/json')


def index(request):
    return render(request, "mascotas/index.html")


def mascota_view(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)

        if form.is_valid():
            form.save()
        return redirect('mascotas:mascota_listar')
    else:
        form = MascotaForm()

    return render(request, 'mascotas/mascota_form.html', {'form': form})


def mascota_list(request):
    mascotas = Mascota.objects.all().order_by('id')
    context = {'mascotas': mascotas}

    return render(request, 'mascotas/mascota_list.html', context)


def mascota_edit(request, id_mascota):
    mascota = Mascota.objects.get(id=id_mascota)

    if request.method == 'GET':
        form = MascotaForm(instance=mascota)
    else:
        form = MascotaForm(request.POST, instance=mascota)

        if form.is_valid():
            form.save()
        return redirect('mascotas:mascota_listar')

    return render(request, 'mascotas/mascota_form.html', {'form': form})


def mascota_delete(request, id_mascota):
    mascota = Mascota.objects.get(id=id_mascota)

    if request.method == 'POST':
        mascota.delete()
        return redirect(request, 'mascotas:mascota_listar')
    
    return render(request, 'mascotas/mascota_delete.html', {'mascota': mascota})


# Vistas basadas en clases
class MascotaList(ListView):
    model = Mascota
    template_name = 'mascotas/mascota_list.html'


class MascotaCreate(CreateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'mascotas/mascota_form.html'
    success_url = reverse_lazy('mascotas:mascota_listar')


class MascotaUpdate(UpdateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'mascotas/mascota_form.html'
    success_url = reverse_lazy('mascotas:mascota_listar')


class MascotaDelete(DeleteView):
    model = Mascota
    template_name = 'mascotas/mascota_delete.html'
    success_url = reverse_lazy('mascotas:mascota_listar')
