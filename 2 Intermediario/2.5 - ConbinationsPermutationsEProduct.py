""" COMBINATIONS PERMUTATIONS E PRODUCT"""
# Combinação - a ordem não importa
# Permutação - a ordem importa
# Produto - a ordem importa e repete valores únicos

# Imports
from itertools import combinations, permutations, product

# Funções
def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


# Listas
pessoas = [
    'João', 'Joana', 'Luiz', 'Letícia'
]

camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['masculino', 'feminino', 'unisex'],
    ['algodão', 'poliéster'],
]

# Saída
print_iter(combinations(pessoas, 2))
print_iter(permutations(pessoas, 2))
print_iter(product(*camisetas))