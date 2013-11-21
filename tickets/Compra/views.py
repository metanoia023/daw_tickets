from obligatorio import settings
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext 
from django.core.context_processors import csrf
from django.utils import timezone
import random


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
# Genero un pin y lo asocio a un telefono (Usuario)
    
    from tickets.pin import Pin
    from tickets.usuario import Usuario
    msg = ''
    
    idSector = request.POST.get('idSector')
    cantidad = request.POST.get('cantidad')
    idEspectaculo = request.POST.get('idEspectaculo')
    numTel = request.POST.get('telefono')
    
    try:
        pinGenerado = random.randrange(1000,9999)
        P = Pin() 
        P.numero = pinGenerado
        P.telefono = Usuario.objects.get(telefono = numTel)
        P.save() 
        
    except Usuario.DoesNotExist:
        # El usuario no existe en la BD
        msg = 'El usuario no existe'
    
    return  render_to_response('tickets/Compra/templates/paso3.html', {"idSector":idSector, "cantidad":cantidad, "idEspectaculo":idEspectaculo, 'numTel':numTel, 'pinGenerado':pinGenerado, 'msg':msg}, context_instance = RequestContext(request))



def paso4(request):
    # Compruebo que el pin corresponda al telefono
    # Veo que el telefono tenga saldo
    # Realizo la venta

    from forms import PinForm 
    from tickets.pin import Pin
    from tickets.ticket import Ticket
    from tickets.precio import Precio
    from tickets.sector import Sector
    from tickets.usuario import Usuario
    from tickets.espectaculo import Espectaculo


    import xmlrpclib
    import hashlib
        
    idSector = request.POST.get('idSector')
    cantidad = int(request.POST.get('cantidad'))
    idEspectaculo = request.POST.get('idEspectaculo')
    
    pinBD = 0000
    pre = 0
    saldo = 0
    precio = 0
    verificaPin = False
    verificaSaldo = False
    verificaCompra = False
    user = 'daw' 
    pwd = 'daw-123'
    m = hashlib.md5(pwd) 
    pwd = m.hexdigest()

    server_url = 'http://{0}:{1}@marcelocaiafa.com/daw/rpc/'.format(user, pwd)

    msg = '' 
    if request.method == 'POST': 
        form = PinForm(request.POST) 
        if form.is_valid(): 
            #numTel = form.cleaned_data.get('telefono') 
            #pinIngresado = form.cleaned_data.get('pin') 
            numTel = request.POST.get('numTel')
            pinIngresado = request.POST.get('pin')
            try:
                P = Pin.objects.get(numero = pinIngresado, telefono = numTel)
                pinBD = P.numero
                verificaPin = True
                # Veo si el tel tiene saldo 

                try:
                    proxy = xmlrpclib.ServerProxy(server_url)
                    response = proxy.info(numTel)
                    saldo = int(response.get('saldo'))
                except xmlrpclib.Fault as err: 
                    msg = 'Ha ocurrido un error (id: 1): \n{0} -- {1}'.format(err.faultCode, err.faultString) 
                except xmlrpclib.ProtocolError as err: 
                    msg = 'Ha ocurrido un error (id: 2): {0} -- {1}'.format(err.errcode, err.errmsg)
                except Exception as e: 
                    msg = 'Ha ocurrido un error (id: 3): {0}'.format(e)
                else: 
                    try:
                        precio = int(Precio.objects.get(sector_id = idSector).precio)
                        total = precio * cantidad
                        if int(saldo) >= int(total):
                            for i in range(1, cantidad):
                                T = Ticket()
                                T.espectaculo = Espectaculo.objects.get(id = idEspectaculo)
                                T.sector = Sector.objects.get(id = idSector)
                                T.fecha = timezone.now()
                                T.precio = precio
                                T.usuario = Usuario.objects.get(telefono = numTel)
                                T.save()
                            verificaCompra = True
                        else:
                            msg = 'Su saldo es insuficiente. Intente nuevamente.'
                    except Exception as e: 
                        msg = 'Ha ocurrido un error (id: 4): {0}'.format(e)
                    
            except Pin.DoesNotExist: 
                # Si el par telefono/pin no estan ingresados
                msg = 'El PIN ingresado no corresponde al enviado al telefono {0}'.format(numTel) 

    else: 
        form = PinForm({'numTel':numTel}) 
        
    
    return  render_to_response('tickets/Compra/templates/paso4.html', {"idSector":idSector, "cantidad":cantidad, "idEspectaculo":idEspectaculo, 'numTel':numTel, 'pinIngresado':pinIngresado, 'pinBD':pinBD, 'msg':msg, 'precio':precio, 'saldo':saldo, 'verificaCompra':verificaCompra}, context_instance = RequestContext(request))







def verificarPin(request, tel): 
    from forms import PinForm 
    msg = '' 
    if request.method == 'POST': 
        form = PinForm(request.POST) 
        if form.is_valid(): 
            tel = form.cleaned_data.get('tel') 
            pin = form.cleaned_data.get('pin') 
            from company_dev.pin import Pin 
            P = Pin.objects.get(numero = pin) 
            if P.telefono.numero == tel: 
                return HttpResponseRedirect('/Compra/templates/paso4/') 
            else: 
                msg = 'PIN no corresponde con telefono {0}'.format(tel) 
    else: 
        form = PinForm({'tel':tel}) 
    return render_to_response('tickets/Telefono/templates/pin.html', {'form': form, 'msg':msg}, context_instance = RequestContext(request))


