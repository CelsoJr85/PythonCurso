""" Função Lambda"""

# Uma lista para servir como base.
lista = [
    {"nome": "celso", "sobrenome": "custodio"},
    {"nome": "Fernanda", "sobrenome": "Pereira"},
    {"nome": "Isabel", "sobrenome": "Moraes"},
]

# Como seria uma função def normal:
#def ordenar(item):
#   return item["sobrenome"]

# Como é uma função lambda:
l1 = sorted(lista, key=lambda item: item["nome"])
l2 = sorted(lista, key=lambda item: item["sobrenome"])

for item in lista:
    print(item)
