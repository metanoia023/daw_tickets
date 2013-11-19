
def template_base(request):
    from django.conf import settings
#indice 6 puede ser reemplazado por una variable.

    Sapp_name = settings.INSTALLED_APPS[6]
    return {'template_base': '{0}/Base/base.html'.format(app_name)}