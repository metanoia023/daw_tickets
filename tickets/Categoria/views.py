from obligatorio import settings
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext


def busqueda(request, id): 
    from django.shortcuts import render_to_response
    from tickets.espectaculo import Espectaculo
    from django.template import RequestContext
    
    busqueda = request.POST.get('buscar')
    if busqueda:
        categorias = Categoria.objects.filter(nombre__icontains = busqueda)
    else:
        categorias = Categoria.objects.all()
    return  render_to_response('{0}/Categoria/templates/index.html'.format(settings.INSTALLED_APPS[6]),{'categorias':categorias,'busqueda':busqueda})


def index(request):
    from tickets.categoria import Categoria
    categorias = Categoria.objects.all()
    return render_to_response('tickets/Categoria/templates/index.html', {'categorias':categorias})        
    

def detalle(request, id, nom):
    from tickets.espectaculo import Espectaculo
    espectaculos = Espectaculo.objects.filter(categoria_id = id)
    return  render_to_response('tickets/Categoria/templates/detalle.html', {'espectaculos':espectaculos})


def busqueda(request, id): 
    from django.shortcuts import render_to_response 
    from tickets.categoria import Categoria 
    from django.template import RequestContext 
    
    busqueda = request.POST.get('buscar') 
    if busqueda: 
        categorias = Categoria.objects.filter(nombre__icontains = busqueda)
    else: 
        categorias = Categoria.objects.all() 
    return render_to_response('{0}/Categoria/templates/index.html'.format(settings.INSTALLED_APPS[6]), {'categorias':categorias,'busqueda':busqueda}, context_instance = RequestContext(request))
    
    
def buscarTodos (request):
        categorias = Categoria.objects.all() 
    