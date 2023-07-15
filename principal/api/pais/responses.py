from principal.models import Pais as table
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

#responses
#@csrf_exempt
def listar_paises(request):
    paises = table.objects.all()
    data = list(paises.values())
    return JsonResponse(data, safe=False)

#@csrf_exempt
def obtener_pais(request, id):
    pais = get_object_or_404(table, id=id)
    data = {
        'id': pais.id,
        'nombre': pais.nombre,
        'codigo': pais.codigo,
    }
    return JsonResponse(data)

@csrf_exempt
def crear_pais(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        codigo = request.POST.get('codigo')
        pais = table(nombre=nombre, codigo=codigo)
        pais.save()
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'message': 'Método no permitido'})

#@csrf_exempt
def actualizar_pais(request, id):
    pais = get_object_or_404(table, id=id)
    if request.method == 'PUT':
        pais.nombre = request.POST.get('nombre')
        pais.codigo = request.POST.get('codigo')
        pais.save()
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'message': 'Método no permitido'})

#@csrf_exempt
def eliminar_pais(request, id):
    pais = get_object_or_404(table, id=id)
    if request.method == 'DELETE':
        pais.delete()
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'message': 'Método no permitido'})
