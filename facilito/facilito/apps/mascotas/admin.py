from django.contrib import admin

from facilito.apps.mascotas.models import Vacuna, Mascota

# Register your models here.
admin.site.register(Vacuna)
admin.site.register(Mascota)