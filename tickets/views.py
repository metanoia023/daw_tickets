# Create your views here.
from obligatorio import settings
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext


def index(request):
    from tickets.categoria import Categoria
    busqueda = request.POST.get('busqueda')
    if busqueda: 
        categorias = Categoria.objects.filter(nombre__icontains = busqueda)
    else: 
        categorias = Categoria.objects.all() 
    return render_to_response('tickets/Categoria/templates/index.html', {'categorias':categorias,'busqueda':busqueda, 'pantalla':'pantalla 3'}, context_instance = RequestContext(request))
