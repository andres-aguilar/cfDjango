from django.shortcuts import render, redirect
from django.http import HttpResponse
from facilito.apps.mascotas.forms import MascotaForm
from facilito.apps.mascotas.models import Mascota

def index(request):
    return render(request, "mascotas/index.html")


def mascota_view(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)

        if form.is_valid():
            form.save()
        return redirect('mascotas:index')
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