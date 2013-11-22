from obligatorio import settings
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import timezone


def index(request):
    from tickets.espectaculo import Espectaculo
    espectaculos = Espectaculo.objects.all()   
    return render_to_response('tickets/Espectaculo/templates/index.html', {'espectaculos':espectaculos})


def detalle(request, id):
    from tickets.espectaculo import Espectaculo
    from tickets.precio import Precio
    from tickets.ticket import Ticket
    from tickets.sector import Sector

    espectaculos = Espectaculo.objects.filter(id = id)
    precios = Precio.objects.filter(espectaculo_id = id)
    ticketsVendidos = (Ticket.objects.filter(espectaculo_id = id)).count

    capacidad = 0
    for unPrecio in precios:
        sector = Sector.objects.filter(id = unPrecio.sector.id)
        for unSector in sector:
            capacidad += unSector.asientos

    ticketsDisponibles = capacidad - ticketsVendidos()
    
    disponibilidad = (float(ticketsDisponibles) / capacidad) * 100
    
    for unEspectaculo in espectaculos:
        now = timezone.now()
        dias = (unEspectaculo.hora - now).days


    return  render_to_response('tickets/Espectaculo/templates/detalle.html', {'espectaculos':espectaculos, 'precios':precios, 'ticketsVendidos':ticketsVendidos, 'ticketsDisponibles':ticketsDisponibles, 'disponibilidad':disponibilidad, 'dias':dias})


#===============================================================================
# def busqueda(request, id): 
#     from django.shortcuts import render_to_response
#     from tickets.espectaculo import Espectaculo
#     from django.template import RequestContext
#     
#     busqueda = request.POST.get('buscar')
#     if busqueda:
#         espectaculos = Espectaculo.objects.filter(nombre__icontains = busqueda)
#     else:
#         espectaculos = Espectaculo.objects.all()
#     return  render_to_response('{0}/Espectaculo/templates/index.html'.format(settings.INSTALLED_APPS[6]),{'espectaculos':espectaculos,'busqueda':busqueda}, context_instance = RequestContext(request))
#===============================================================================


def crud(request):
    from tickets.espectaculo import Espectaculo
    from tickets.categoria import Categoria
    from tickets.lugar import Lugar
    
    espectaculos = Espectaculo.objects.all()
    categorias = Categoria.objects.all()
    lugares = Lugar.objects.all()
    
    
    return render_to_response('tickets/Espectaculo/templates/crud.html', {'espectaculos':espectaculos, 'categorias':categorias, 'lugares':lugares})




    
    
    
   