from django.conf.urls import patterns, include, url

urlpatterns = patterns('tickets',
                    url(r'(?P<id>\d+)/?$','Espectaculo.views.detalle'),
                    url(r'/?$', 'Espectaculo.views.index'),
              )





