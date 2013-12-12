from obligatorio import settings
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import timezone

#from django.core.context_processors import csrf

def muestro_afiche(request, id):
    from tickets.espectaculo import Espectaculo
    espectaculos = Espectaculo.objects.filter(id = id)
    #return render_to_response('afiche.html', {'espectaculos': espectaculos})
    return render_to_response('tickets/Espectaculo/templates/afiche.html', {'espectaculos': espectaculos})


def listado_afiches(request):
    from tickets.espectaculo import Espectaculo
    espectaculos = Espectaculo.objects.all()
    return render_to_response('tickets/Espectaculo/templates/afiches.html', {'espectaculos': espectaculos})


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
    
    disponibilidad = 0
    if capacidad != 0:
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
    msg = ''
    strID = ''
    id = 0

    meses = {'01':'Enero', '02':'Febrero', '03':'Marzo', '04':'Abril', '05':'Mayo', '06':'Junio', '07':'Julio', '08':'Agosto', '09':'Setiembre', '10':'Octubre', '11':'Noviembre', '12':'Diciembre'}
        
    if request.method == 'POST':
        msg = 'Es un POST'
        
        variables = request.POST.items()
        for value in variables:
            if value[1]=='Actualizar':
                id = value[0]
        
        #Ahora veo si ingreso nuevo o actualizo
        E = Espectaculo()
        

        if id != 0:
            strID = str(id)
            E.id = id

        for value in variables:
            key = value[0]
            if key == 'nombre' + strID:
                E.nombre = value[1]
                #msg += 'Key:' + key + ' -- '
            if key == 'selCategoria' + strID:
                E.categoria = Categoria.objects.get(id = value[1])
                #msg += value[1] + ' -- '
            if key == 'descripcion' + strID:
                E.descripcion = value[1]
                #msg += value[1] + ' -- '
            if key == 'estado' + strID:
                E.estado = value[1]
                #msg += value[1] + ' -- '
            if key == 'selLugar' + strID:
                E.lugar = Lugar.objects.get(id = int(value[1]))
                #msg += 'SelLugar:' + value[1] + ' -- '
                #msg += '(' + str(E.lugar.id) + ' - ' + E.lugar.nombre + ')'
            if key == 'selDia' + strID:
                dia = value[1]
            if key == 'selMes' + strID:
                mes = value[1]
            if key == 'selAnio' + strID:
                anio = value[1]
            if key == 'selHora' + strID:
                hora = value[1]
            if key == 'selMinutos' + strID:
                min = value[1]
        E.hora = anio + '-' + mes + '-' + dia + ' ' + hora + ':' + min
            
        #E.hora = '2015-02-02 18:00:00'
        #E.hora = "2015-02-02T18:00:00-03:00"
            
        E.save()
        
        return render_to_response('tickets/Espectaculo/templates/crud.html', {'espectaculos':espectaculos, 'categorias':categorias, 'lugares':lugares, 'msg':msg, 'meses':meses}, context_instance = RequestContext(request))

    else:
        msg = 'No es post'
        return render_to_response('tickets/Espectaculo/templates/crud.html', {'espectaculos':espectaculos, 'categorias':categorias, 'lugares':lugares, 'msg':msg, 'meses':meses}, context_instance = RequestContext(request))
    
    #return render_to_response('tickets/Espectaculo/templates/crud.html', {'espectaculos':espectaculos, 'categorias':categorias, 'lugares':lugares, 'msg':msg}, context_instance = RequestContext(request))

        







    
    
    
   