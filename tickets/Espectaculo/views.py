from obligatorio import settings
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext



def info(request, id):
    from tickets.espectaculo import Espectaculo
    espectaculos = Espectaculo.objects.all()   
    return render_to_response('tickets/Espectaculo/templates/index.html', {'espectaculos':espectaculos})


def busqueda(request, id): 
    from django.shortcuts import render_to_response
    from tickets.espectaculo import Espectaculo
    from django.template import RequestContext

    
    #me agarro lo que me escriben en el campo de texto para buscar espectaculos
    busqueda = request.POST.get('buscar')
    #si viene algo en busqueda
    if busqueda:
        espectaculos = Espectaculo.objects.filter(nombre__icontains = busqueda)
    else:
        espectaculos = Espectaculo.objects.all()
    return  render_to_response('{0}/Espectaculo/templates/index.html'.format(settings.INSTALLED_APPS[6]),{'espectaculos':espectaculos,'busqueda':busqueda}, context_instance = RequestContext(request))
    #el return siempre tiene que devolver render to response
    #devuelve lo que tiene en template index
   