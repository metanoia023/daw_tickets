import random

def obtenerNuevoPin (request):
    numero = random.randrange(1000, 9999)
    return numero

def index(request):
    pass
