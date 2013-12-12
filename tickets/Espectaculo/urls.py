from django.conf.urls import patterns, include, url

urlpatterns = patterns('tickets',
                    url(r'backend/?$', 'Espectaculo.views.crud'),

                    #url(r'/afiche/(?P<nombre>\w+)', 'Espectaculo.views.muestro_afiche', name="nombre"),
                    url(r'afiches/?$', 'Espectaculo.views.listado_afiches'),
                    url(r'afiche/(?P<id>\d+)/?$', 'Espectaculo.views.muestro_afiche'),

                    url(r'(?P<id>\d+)/?$','Espectaculo.views.detalle'),
                    url(r'/?$', 'Espectaculo.views.index'),

              )





