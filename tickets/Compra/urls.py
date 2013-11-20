from django.conf.urls import patterns, include, url

urlpatterns = patterns('tickets',
                    url(r'paso2/?$', 'Compra.views.paso2'),
                    url(r'paso3/?$', 'Compra.views.paso3'),
                    url(r'paso4/?$', 'Compra.views.paso4'),
                    url(r'(?P<id>\d+)/?$','Compra.views.paso1'),
                    url(r'/?$', 'Categorias.views.index'),
              )

