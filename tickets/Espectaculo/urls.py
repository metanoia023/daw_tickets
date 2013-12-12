from django.conf.urls import patterns, include, url

urlpatterns = patterns('tickets',
                    url(r'backend/?$', 'Espectaculo.views.crud'),
                    url(r'(?P<id>\d+)/?$','Espectaculo.views.detalle'),
                    url(r'/?$', 'Espectaculo.views.index'),
					
					
					url(r'/afiche/(?P<nombre>\w+)', 'Espectaculo.views.muestro_afiche', name="nombre"),
              )





