from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from obligatorio import settings

# Si no esta agregar para que pueda editar en el backend:
# admin.autodiscover()
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'tickets.views.index'),
    #Incluyo urls para procesar url de los modelos.
    url(r'^lugar/', include('tickets.Lugar.urls')),
	url(r'^categoria/', include('tickets.Categoria.urls')),
    url(r'^compra/', include('tickets.Compra.urls')),
	url(r'^espectaculo/', include('tickets.Espectaculo.urls')),
	url(r'^sector/', include('tickets.Sector.urls')),
	url(r'^precio/', include('tickets.Precio.urls')),
	url(r'^ticket/', include('tickets.Ticket.urls')),
    url(r'^pin/', include('tickets.Pin.urls')),
	url(r'^usuario/', include('tickets.Usuario.urls')),
    url(r'^static/(.*)$', 'django.views.static.serve', {'tickets': '/static/css/style.css'}),
    url(r'^backend/', include(admin.site.urls)),

    url(r'^afiche/', include('tickets.Espectaculo.urls')),

)


 
