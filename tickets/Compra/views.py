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


# Genero un pin y lo asocio a un telefono (Usuario)
def paso3(request):
    
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



# Compruebo que el pin corresponda al telefono
# Veo que el telefono tenga saldo
# Realizo la venta
def paso4(request):

    from forms import PinForm 
    from tickets.pin import Pin
    import xmlrpclib
    import hashlib
        
    idSector = request.POST.get('idSector')
    cantidad = request.POST.get('cantidad')
    idEspectaculo = request.POST.get('idEspectaculo')
    #pinBD = request.POST.get('pinBD')
    #numTel = request.POST.get('numTel')
    #pinIngresado = request.POST.get('pin')
    
    pinBD = 0000
    verificaPin = False
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
                    saldo = 0
                    proxy = xmlrpclib.ServerProxy(server_url)
                    response = proxy.info(numTel)
                    saldo = response.get('saldo')
                     
                except xmlrpclib.Fault as err: 
                    #print 'Fault', err.faultCode, err.faultString
                    msg = 'Ha ocurrido un error: <br>{0}<br>{1}'.format(err.faultCode, err.faultString) 
                except xmlrpclib.ProtocolError as err: 
                    #print 'Protocol', err.errcode, err.errmsg
                     msg = 'Ha ocurrido un error: <br>{0}<br>{1}'.format(err.errcode, err.errmsg)
                except Exception as e: 
                    #print e 
                    msg = 'Ha ocurrido un error: <br>{0}'.format(e)
                else: 
                    #print response
                    msg = 'Ha ocurrido un error: <br>{0}'.format(response)
                    
                    
                    
                
                
            except Pin.DoesNotExist: 
                # Si el par telefono/pin no estan ingresados
                msg = 'El PIN ingresado no corresponde al enviado al telefono {0}'.format(numTel) 
    else: 
        form = PinForm({'numTel':numTel}) 
        
    #return render_to_response('tickets/Telefono/templates/pin.html', {'form': form, 'msg':msg}, context_instance = RequestContext(request))
    
    return  render_to_response('tickets/Compra/templates/paso4.html', {"idSector":idSector, "cantidad":cantidad, "idEspectaculo":idEspectaculo, 'numTel':numTel, 'pinIngresado':pinIngresado, 'pinBD':pinBD, 'verificaPin':verificaPin, 'msg':msg, 'saldo':saldo}, context_instance = RequestContext(request))



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






#Si el formulario fue enviado(submit)
    from forms import TelForm 
    if request.method == 'POST': 
        #completamos los campos declarados en TelForm con los datos enviados por POST. 
        form = TelForm(request.POST) 
        #se ejecuta metodo clean(a nivel Campo, luego a Nivel Form) 
        #si no se lanzo ninguna exception desde clean. 
        if form.is_valid(): 
            #accedo al diccionario generado por metodo Form.clean o redefinido enTelForm.clean 
            tel = form.cleaned_data.get('telefono') 
            from company_dev.telefono import Telefono 
            T = Telefono() 
            T.numero = tel 
            T.save() 
            from company_dev.pin import Pin
            P = Pin() 
            import random
            P = Pin() 
            P.numero = random.randrange(1000,9999) 
            P.telefono = T 
            P.save() 
            return HttpResponseRedirect('/telefono/pin/{0}/'.format(tel)) 
        else: 
            #instancia vacia de TelForm. 
            form = TelForm() 
        #envio el formulario hacia el HTML. 
        return render_to_response('tickets/Telefono/templates/telefono.html', {'form': form}, context_instance = RequestContext(request)) 
    
def solicitarPin(request, tel): 
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
                return HttpResponseRedirect('/telefono/gracias/') 
            else: 
                msg = 'PIN no corresponde con telefono {0}'.format(tel) 
    else: 
        form = PinForm({'tel':tel}) 
    return render_to_response('tickets/Telefono/templates/pin.html', {'form': form, 'msg':msg}, context_instance = RequestContext(request))


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


