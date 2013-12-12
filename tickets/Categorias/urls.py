from django.conf.urls import patterns, include, url

urlpatterns = patterns('tickets',
                    url(r'(?P<id>\d+)/(?P<nom>\w+)/?$','Categoria.views.detalle'),
                    url(r'/?$', 'Categoria.views.index'),
              )
