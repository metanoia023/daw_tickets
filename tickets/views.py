# Create your views here.
from obligatorio import settings
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext


def index(request):
    from tickets.categoria import Categoria
    categorias = Categoria.objects.all()   

    return  render_to_response('tickets/Categoria/templates/index.html',{'categorias':categorias}, context_instance = RequestContext(request))
    #el return siempre tiene que devolver render to response
    #devuelve lo que tiene en template index
    
