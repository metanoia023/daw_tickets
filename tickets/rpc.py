
class RPC:

    def consultaSaldo(self, telefono):
        
        import xmlrpclib
        import hashlib

        user = 'daw'
        pwd = 'daw-123'

        m = hashlib.md5(pwd)
        pwd = m.hexdigest()
        server_url = 'http://{0}:{1}@marcelocaiafa.com/daw/rpc/'.format(user, pwd)
        try:
            proxy = xmlrpclib.ServerProxy(server_url)
            response = proxy.info(telefono)
            saldo = response.get('saldo')
            return saldo
        except xmlrpclib.Fault as err: 
            msg += 'Ha ocurrido un error (1): \n{0} -- {1}'.format(err.faultCode, err.faultString) 
        except xmlrpclib.ProtocolError as err: 
            msg += 'Ha ocurrido un error (2): {0} -- {1}'.format(err.errcode, err.errmsg)
        except Exception as e: 
            msg += 'Ha ocurrido un error (3): {0}'.format(e)
        else: 
            #msg += 'Ha ocurrido un error (4): {0}'.format(response)
            return msg
