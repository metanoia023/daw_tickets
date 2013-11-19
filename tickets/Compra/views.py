from obligatorio import settings
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import timezone


def index(request):
    from tickets.categoria import Categoria
    categorias = Categoria.objects.all()   
    return  render_to_response('tickets/Categoria/templates/index.html',{'categorias':categorias})

def paso1(request, id):
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

    return  render_to_response('tickets/Compra/templates/paso1.html', {'espectaculos':espectaculos, 'precios':precios}, context_instance = RequestContext(request))


def paso2(request):
    
    sect = request.POST.get('selSector')
    cant = request.POST.get('selCantidad')
    idEs = request.POST.get('idEspectaculo')
        
    
    return  render_to_response('tickets/Compra/templates/paso2.html', {"sect":sect, "cant":cant, "idEs":idEs})




