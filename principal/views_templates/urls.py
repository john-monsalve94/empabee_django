from django.urls import path, include
from .pais import urls as pais_urls
from .colmena import urls as colmena_urls
from .estanque import urls as estanque_urls
from .ciudad import urls as ciudad_urls
from .persona import urls as persona_urls
from .contrato import urls as contrato_urls
from .cultivo import urls as cultivo_urls
from .departamentos import urls as departamentos_urls
from .direccion import urls as direccion_urls
from .infotratacolmena import urls as infotratacolmena_urls
from .infotrataestanque import urls as infotrataestanque_urls
from .msensorcolmena import urls as msensorcolmena_urls
from .msensorestanque import urls as msensorestanque_urls
from .sensor import urls as sensor_urls
from .tempresa import urls as tempresa_urls
from .tidentificacion import urls as tidentificacion_urls
from .tiptrata import urls as tiptrata_urls
from .tratamiento import urls as tratamiento_urls
from .tsensor import urls as tsensor_urls

from .asignacionencargado import urls as asignacionencargado_urls
from .cabezafactura import urls as cabezafactura_urls
from .cuerpofactura import urls as cuerpofactura_urls
from .empresa import urls as empresa_urls
from .especieabeja import urls as especieabeja_urls
from .especiepez import urls as especiepez_urls
from .produccioncolmena import urls as produccioncolmena_urls
from .produccionestanque import urls as produccionestanque_urls
from .reportecolmena import urls as reportecolmena_urls
from .reporteestanque import urls as reporteestanque_urls
from .tcontrato import urls as tcontrato_urls


urlpatterns = [


    # rutas para la tabla pais
    path('pais/', include(pais_urls)),
    path('colmena/', include(colmena_urls)),
    path('estanque/', include(estanque_urls)),
    path('ciudad/', include(ciudad_urls)),
    path('persona/', include(persona_urls)),
    path('contrato/', include(contrato_urls)),
    path('cultivo/', include(cultivo_urls)),
    path('departamentos/', include(departamentos_urls)),
    path('direccion/', include(direccion_urls)),
    path('infotratacolmena/', include(infotratacolmena_urls)),
    path('infotrataestanque/', include(infotrataestanque_urls)),
    path('msensorcolmena/', include(msensorcolmena_urls)),
    path('msensorestanque/', include(msensorestanque_urls)),
    path('sensor/', include(sensor_urls)),
    path('tempresa/', include(colmena_urls)),
    path('tidentificacion/', include(tidentificacion_urls)),
    path('tiptrata/', include(tiptrata_urls)),
    path('tratamiento/', include(tratamiento_urls)),
    path('tsensor/', include(tsensor_urls)),

    path('asignacionencargado/', include(asignacionencargado_urls)),
    path('cabezafactura/', include(cabezafactura_urls)),
    path('cuerpofactura/', include(cuerpofactura_urls)),
    path('empresa/', include(empresa_urls)),
    path('especieabeja/', include(especieabeja_urls)),
    path('especiepez/', include(especiepez_urls)),
    path('produccioncolmena/', include(produccioncolmena_urls)),
    path('produccionestanque/', include(produccionestanque_urls)),
    path('reportecolmena/', include(reportecolmena_urls)),
    path('reporteestanque/', include(reporteestanque_urls)),
    path('tcontrato/', include(tcontrato_urls)),
]
