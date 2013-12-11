from django.contrib import admin

from categoria import Categoria
from espectaculo import Espectaculo 
from lugar import Lugar
from precio import Precio 
from sector import Sector
from usuario import Usuario

admin.site.register(Categoria) 
admin.site.register(Espectaculo)
admin.site.register(Lugar)
admin.site.register(Precio)
admin.site.register(Sector)
admin.site.register(Usuario)
