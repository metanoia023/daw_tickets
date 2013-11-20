from django import forms
from django.utils.translation import ugettext as _    #traduccion a otros lenguajes
from django.core.context_processors import csrf
from django.template import RequestContext


class TelForm(forms.Form):
    telefono = forms.CharField(max_length=9, initial= 'Ingrese numero')

    def clean(self):
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
    