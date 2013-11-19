from django.conf.urls import patterns, include, url

urlpatterns = patterns('tickets',
                    url(r'paso2/?$', 'Compra.views.paso2'),
                    url(r'(?P<id>\d+)/?$','Compra.views.paso1'),
                    url(r'/?$', 'Categorias.views.index'),
              )

