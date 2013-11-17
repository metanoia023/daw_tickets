from django.conf.urls import patterns, include, url

urlpatterns = patterns('tickets',
                    url(r'(?P<id>\d+)?/?$','Espectaculo.views.info'),)