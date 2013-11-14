from django import forms


class TelForm(forms.Form):
    #Cada nombre de campo debe ser exactamente igual al atributo name de cada elemento del formulario.
    telefono = forms.CharField(max_length=9, initial = 'Ingrese numero')
#caja de texto de tipo char este form va a tener un atributo telefono de tipo char, integer, etc

def clean(self):
    #si esta definido se ejecuta cuando invoco a li_valid
    datos = super(TelForm, self).clean()
    tel = datos.get('telefono')
    datos['telefono'] = int(tel) 
    if not tel.isdigit() or len(tel) !=9:
        raise forms.ValidationError('El telefono no es valido')
#valido telefono
#... 
#siempre debo retornar el diccionario si redefino el metodo clean, para luego ser accedido desde la vista en cleaned_data
return datos


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