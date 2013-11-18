
from obligatorio import settings
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
    from tickets.usuario import Usuario  
    return render_to_response('tickets/Usuario/templates/telefono.html')

def solicitarTelefono(request):
#Si el formulario fue enviado (submit)
    from tickets.Usuario.forms import TelForm
    msg = ''
    if request.method == 'POST':
#completamos los campos declarados en TelForm con los datos enviados por POST.
        form = TelForm(request.POST)
#se ejecuta metodo clean(a nivel Campo, luego a Nivel Form)
#si no se lanzo ninguna exception desde Form.clean().
        if form.is_valid():
#accedo al diccionario generado por metodo Form.clean () o redefinido en 
            TelForm.clean()
            tel = form.cleaned_data.get('telefono')
            msg = 'Es valido {0}'.format(type(tel))
        else:
            msg = 'No es valido'
    else:
#instancia vacia de TelForm.
        form = TelForm()
#envio la instancia formulario hacia el HTML.
return render_to_response('{0}/Usuario/templates/telefono.html'.format(settings.INSTALLED_APPS[6]), {'form': form, 'msg':msg}, context_instance = RequestContext(request)) 


# aca empiezo a probar estoy con Gabriela

