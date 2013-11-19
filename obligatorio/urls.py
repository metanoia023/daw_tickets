from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from obligatorio import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

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
	url(r'^usuario/', include('tickets.Usuario.urls')),
    url(r'^static/(.*)$', 'django.views.static.serve', {'tickets': '/static/css/style.css'}),


    #url(r'^categoria/Musica', include('tickets.Categoria.urls', 'tickets.Categoria.url')),
    # Examples:
    # url(r'^$', 'obligatorio.views.home', name='home'),
    # url(r'^obligatorio/', include('obligatorio.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)


 
