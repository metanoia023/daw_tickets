from obligatorio import settings
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import timezone
 

def index(request):
    from tickets.categoria import Categoria
    categorias = Categoria.objects.all()
    return render_to_response('tickets/Categoria/templates/index.html', {'categorias':categorias}, context_instance = RequestContext(request))      
    

def detalle(request, id, nom):
    from tickets.espectaculo import Espectaculo
    espectaculos = Espectaculo.objects.filter(categoria_id = id)
    now = timezone.now()
    nombreCat = nom
    return  render_to_response('tickets/Categoria/templates/detalle.html', {'espectaculos':espectaculos, 'now': now, 'nom': nom, 'idCat':id})


def busqueda(request):
    from tickets.categoria import Categoria 
    busqueda = request.POST.get('busqueda')
    if busqueda: 
        categorias = Categoria.objects.filter(nombre__icontains = busqueda)
    else: 
        categorias = Categoria.objects.all() 
    return render_to_response('tickets/Categoria/templates/index.html', {'categorias':categorias,'busqueda':busqueda}, context_instance = RequestContext(request))
    
    
def buscarTodos (request):
        categorias = Categoria.objects.all() 
    