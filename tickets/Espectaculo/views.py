from obligatorio import settings
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

from datetime import datetime, timedelta


def index(request):
    from tickets.espectaculo import Espectaculo
    espectaculos = Espectaculo.objects.all()   
    return render_to_response('tickets/Espectaculo/templates/index.html', {'espectaculos':espectaculos})


def detalle(request, id):
    from tickets.espectaculo import Espectaculo
    espectaculos = Espectaculo.objects.filter(id = id)
    from tickets.precio import Precio
    precios = Precio.objects.filter(espectaculo_id = id)
    from tickets.ticket import Ticket
    ticketsVendidos = (Ticket.objects.filter(espectaculo_id = id)).count

    from tickets.sector import Sector
    capacidad = 0
    for unPrecio in precios:
        sector = Sector.objects.filter(id = unPrecio.sector.id)
        for unSector in sector:
            capacidad += unSector.asientos

    ticketsDisponibles = capacidad - ticketsVendidos()
    
    disponibilidad = (float(ticketsDisponibles) / capacidad) * 100
    
    for unEspectaculo in espectaculos:
        #now  = datetime.now
        #dif = unEspectaculo.hora - now
        #dias = dif.days
        now = datetime.now()
        dias = (unEspectaculo.hora - now).days
        
        
    
    return  render_to_response('tickets/Espectaculo/templates/detalle.html', {'espectaculos':espectaculos, 'precios':precios, 'ticketsVendidos':ticketsVendidos, 'ticketsDisponibles':ticketsDisponibles, 'disponibilidad':disponibilidad, 'dias':dias})
    #return  render_to_response('tickets/Espectaculo/templates/detalle.html', {'espectaculos':espectaculos})


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


   