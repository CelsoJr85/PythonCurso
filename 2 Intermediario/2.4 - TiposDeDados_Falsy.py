# Mutáveis [], {}, set()
# Imutáveis (), " ", 0, 0.00, None, False, range(0, 10)
lista = []
dicionario = {}
conjunto = set()
tupla = ()
string = ""
int = 0
float = 0.00
nada = None
falso = False
intervalo = range(0, 10)

# Todos itens acima são falsy, pois não há nada dentro.
# A partir do momento que tem algo dentro passa a ser truthy

def falsy(valor):
    return 'falsy' if not valor else 'truthy'