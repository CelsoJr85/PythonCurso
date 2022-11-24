""" Map, Partial"""
# Map - Mapear dados
# Imports
from functools import partial

# Função
def print_iter(iterator):
    print(*list(iterator), sep="\n")
    print()

# Produtos
produtos = [
    {"nome": "Produto 5", "preco": 10.00},
    {"nome": "Produto 1", "preco": 22.32},
    {"nome": "Produto 3", "preco": 10.11},
    {"nome": "Produto 4", "preco": 105.87},
    {"nome": "Produto 2", "preco": 69.90},
]

# Funções complementares
def aumentar_porcentagem(valor, porcentagem):
    return round(valor * porcentagem, 2)

aumentar_dez_porcento = partial(
    aumentar_porcentagem,
    porcentagem = 1.5
)

def muda_preco_produtos(produto):
    return {
        **produto,
        "preco": aumentar_dez_porcento(
            produto["preco"]
        )
    }

novos_produtos = list(map(
    muda_preco_produtos,
    produtos
))

# Saída
print_iter(produtos)
print_iter(novos_produtos)
