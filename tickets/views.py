# Create your views here.
from company import settings
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):

    return  render_to_response('{0}/Categoria/templates/index.html'.format(settings.INSTALLED_APPS[6]), context_instance = RequestContext(request))
    #el return siempre tiene que devolver render to response
    #devuelve lo que tiene en template index
