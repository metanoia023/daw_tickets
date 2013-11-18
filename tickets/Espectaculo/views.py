from obligatorio import settings
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext


def index(request):
    from tickets.espectaculo import Espectaculo
    espectaculos = Espectaculo.objects.all()   
    return render_to_response('tickets/Espectaculo/templates/index.html', {'espectaculos':espectaculos})


def detalle(request, id):
    from tickets.espectaculo import Espectaculo
    espectaculos = Espectaculo.objects.filter(id__icontains = id)
    return  render_to_response('tickets/Espectaculo/templates/detalle.html', {'espectaculos':espectaculos})


def busqueda(request, id): 
    from django.shortcuts import render_to_response
    from tickets.espectaculo import Espectaculo
    from django.template import RequestContext
    
    busqueda = request.POST.get('buscar')
    if busqueda:
        espectaculos = Espectaculo.objects.filter(nombre__icontains = busqueda)
    else:
        espectaculos = Espectaculo.objects.all()
    return  render_to_response('{0}/Espectaculo/templates/index.html'.format(settings.INSTALLED_APPS[6]),{'espectaculos':espectaculos,'busqueda':busqueda}, context_instance = RequestContext(request))


   