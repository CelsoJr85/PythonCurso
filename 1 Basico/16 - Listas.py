""" LISTAS """
# Guarda informação
# Métodos: append, insert, pop, del, clear, extend
# Simbolo usado é []

# posição:   0    1    2    3    4
lista_01 = ["a", "b", "c", "d", "e"]

# para acessar a posição usar [n] sendo n o numero da posição.
print(lista_01[1]) # b
print(lista_01[4]) # e

numero = lista_01[2]
print(numero) # c

# Alterando uma parte da lista
lista_01[0] = "A"
print(lista_01[0]) # A

# Apagar uma parte da lista
del lista_01[4]
print(lista_01) # ['A', 'b', 'c', 'd']

# Adicionar no final
lista_01.append("f")
print(lista_01) # ['A', 'b', 'c', 'd', 'f']

# Remover o final da lista
lista_01.pop()
print(lista_01) # ['A', 'b', 'c', 'd']    removeu o f

# Adicionando em qualquer lugar da lista
#              (indice, nova coisa)
lista_01.insert(1,      "a")
print(lista_01) # ['A', 'a', 'b', 'c', 'd']

# Juntar listas
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]

# Juntar via + retorna uma nova lista
lista_c = lista_a + lista_b

# Ou incluir lista_b na lista_a com o extend, não retorna, mas modifica a lista_a
lista_a.extend(lista_b)

print(lista_c)
print(lista_a)


# Enumerar indexes de uma lista
lista_nova = ['c', 'e', 'l', 's', 'o']
lista_enumerada = enumerate(lista_nova)
for item in lista_enumerada:
    print(item)