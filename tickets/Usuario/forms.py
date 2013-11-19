from django import forms
from django.utils.translation import ugettext as _    #traduccion a otros lenguajes
from django.core.context_processors import csrf
from django.template import RequestContext


class TelForm(forms.Form):
    #Cada nombre de campo debe ser exactamente igual al atributo name de cada elemento del formulario.
    telefono = forms.CharField(max_length=9, initial= 'Ingrese numero')
#caja de texto de tipo char este form va a tener un atributo telefono de tipo char, integer, etc

    def clean(self):
    #si esta definido se ejecuta cuando invoco a li_valid
        cleaned_data = super(TelForm, self).clean()
        tel = cleaned_data.get('telefono')
        mensajes = []
        if tel is not None and not tel.isdigit():
            mensajes.append(_('Ingrese solo numeros'))
        if tel is not None and len(tel) != 9: 
            mensajes.append(_('Largo ({0}) de telefono invalido'.format(len(tel)))) 
        if mensajes:
            raise forms.ValidationError(mensajes)
        return tel
    
    
    '''
       def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        cc_myself = cleaned_data.get("cc_myself")
        subject = cleaned_data.get("subject")

        if cc_myself and subject:
            # Only do something if both fields are valid so far.
            if "help" not in subject:
                raise forms.ValidationError("Did not send for 'help' in "
                        "the subject despite CC'ing yourself.")
    '''
#valido telefono
#... 
#siempre debo retornar el diccionario si redefino el metodo clean, para luego ser accedido desde la vista en cleaned_data


class PinForm(forms.Form):
    pin = forms.CharField(max_length=4)
   
    def clean(self):
        datos = super(PinForm, self).clean()
        pin = cleaned_data.get('pin') 
        if pin is not None and not pin.isdigit():
            raise forms.ValidationError('Ingrese solo numeros') 
        if pin is not None and len(pin) != 4: 
            raise forms.ValidationError(_('Largo ({0}) de PIN invalido'.format(len(pin))))
        return datos
    