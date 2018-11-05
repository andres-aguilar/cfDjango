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
    mascotas = Mascota.objects.all()
    context = {'mascotas': mascotas}

    return render(request, 'mascotas/mascota_list.html', context)