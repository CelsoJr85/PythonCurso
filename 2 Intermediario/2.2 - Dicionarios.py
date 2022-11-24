""" DICIONÁRIOS """
# DICT
# estruturado com {chave : valor,}

pessoa = {
#   Chave : Valor
    "nome": "Celso",
    "sobrenome": "Custodio",
    "idade": 37,
    "altura": 1.70,
    # uma chave que recebe uma lista de chaves e valores
    "endereço": [
        {"rua": "Um", "número": 542},
        {"rua": "Dois", "número": 352},
    ],
}
# para acessar um valor usamos a chave que serve como indice
print(pessoa["nome"])


# MÉTODOS
metodo = {
#   Chave : Valor
    "nome": "Celso",
    "sobrenome": "Custodio",
    "idade": 37,
    "altura": 1.70,
}
# Lens
print(len(metodo))