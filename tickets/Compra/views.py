from obligatorio import settings
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext 
from django.core.context_processors import csrf
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
    
    capacidad = 0
    capacidades = {}
    for unPrecio in precios:
        sector = Sector.objects.filter(id = unPrecio.sector_id)
        for unSector in sector:
            capacidad = unSector.asientos
            ticketsVendidos = (Ticket.objects.filter(espectaculo_id = id, sector = unSector.id)).count
            capacidades[unPrecio.sector_id] =  int(capacidad) - int(ticketsVendidos())

    return  render_to_response('tickets/Compra/templates/paso1.html', {'espectaculos':espectaculos, 'precios':precios, 'capacidades':capacidades}, context_instance = RequestContext(request))


def paso2(request):
    
    idSector = request.POST.get('selSector')
    cantidad = request.POST.get('selCantidad')
    idEspectaculo = request.POST.get('idEspectaculo')
    return  render_to_response('tickets/Compra/templates/paso2.html', {"idSector":idSector, "cantidad":cantidad, "idEspectaculo":idEspectaculo}, context_instance = RequestContext(request))


def paso3(request):
    
    idSector = request.POST.get('idSector')
    cantidad = request.POST.get('cantidad')
    idEspectaculo = request.POST.get('idEspectaculo')
    numTel = request.POST.get('telefono')
    return  render_to_response('tickets/Compra/templates/paso3.html', {"idSector":idSector, "cantidad":cantidad, "idEspectaculo":idEspectaculo, 'numTel':numTel}, context_instance = RequestContext(request))


def paso4(request):
    
    idSector = request.POST.get('idSector')
    cantidad = request.POST.get('cantidad')
    idEspectaculo = request.POST.get('idEspectaculo')
    return  render_to_response('tickets/Compra/templates/paso4.html', {"idSector":idSector, "cantidad":cantidad, "idEspectaculo":idEspectaculo}, context_instance = RequestContext(request))



def solicitarTelefono(request):
    from tickets.Usuario.forms import TelForm
    msg = ''
    if request.method == 'POST':
        form = TelForm(request.POST) 
        if form.is_valid():
            TelForm.clean()
            tel = form.cleaned_data.get('telefono')
            msg = 'Es valido {0}'.format(type(tel))
        else:
            msg = 'No es valido'
    else:
        form = TelForm()
    return render_to_response('tickets/Usuario/templates/telefono.html', {'form': form, 'msg':msg}, context_instance = RequestContext(request)) 


