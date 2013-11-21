
import xmlrpclib
import hashlib


user = 'daw'
pwd = 'daw-123'
#enviamos password encriptado en MD5

#creamos objeto md5
m = hashlib.md5(pwd)
#encriptamos valor a hexadecimal
pwd = m.hexdigest()
#url del servidor RPC
server_url = 'http://{0}:{1}@marcelocaiafa.com/daw/rpc/'.format(user, pwd)
try:
#creamos instancia de servidor
    proxy = xmlrpclib.ServerProxy(server_url)
    
    tel = request.POST.get('telefono')
    #invocamos metodo registrado en el servidor
    response = proxy.info('tel')
    #Errores a nivel de aplicacion, por ejemplo invocar un metodo que no esta registrado en el servidor.
except xmlrpclib.Fault as err:
        print 'Fault', err.faultCode, err.faultString
        #Errores a nivel de protocolo de transporte, por ejemplo 404 not found.
except xmlrpclib.ProtocolError as err:
        print 'Protocol', err.errcode, err.errmsg
except Exception as e:
        print e 
else:
        print response