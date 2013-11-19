from django.conf.urls import patterns, include, url


'''
urlpatterns = patterns('tickets','tickets.Usuario.views',
url(r'^$','solicitarTelefono'), 
)
'''

urlpatterns = patterns('tickets.Usuario.views',
url(r'^$','solicitarTelefono'), 
)
