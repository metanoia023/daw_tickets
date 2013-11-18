from django.conf.urls import patterns, include, url



urlpatterns = patterns('tickets',
                   # url(r'(?P<id>\d+)/?$','Usuario.views.detalle'),
                    url(r'/?$', 'Usuario.views.index'),
              )
