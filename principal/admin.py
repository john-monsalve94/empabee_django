from django.contrib import admin
from .models import *

admin.site.register(Pais)  # no
admin.site.register(Colmena)  # ----
admin.site.register(Estanque)
admin.site.register(Ciudad)  # no
admin.site.register(Persona)  # ----
admin.site.register(Contrato)
admin.site.register(Cultivo)  # ----
admin.site.register(Departamentos)  # no
admin.site.register(Direccion)  # si registro
admin.site.register(InfotrataColmena)  # si
admin.site.register(InfotrataEstanque)  # si
admin.site.register(MSensorColmena)  # no
admin.site.register(MSensorEstanque)  # no
admin.site.register(Sensor)  # si #----
admin.site.register(TEmpresa)  # no
admin.site.register(TIdentificacion)
admin.site.register(Tiptrata)
admin.site.register(Tratamiento)
admin.site.register(Tsensor)  # si

admin.site.register(AsignacionEncargado)
admin.site.register(CabezaFactura)
admin.site.register(CuerpoFactura)
admin.site.register(Empresa)
admin.site.register(EspecieAbeja)
admin.site.register(EspeciePez)
admin.site.register(ProduccionColmena)
admin.site.register(ProduccionEstanque)
admin.site.register(ReporteColmena)
admin.site.register(ReporteEstanque)
admin.site.register(TContrato)
