import json

#pessoa = {
#    'nome': 'Celso',
#    'sobrenome': 'Custodio',
#    'endereço': [
#        {'rua': 'R1', 'número': 32},
#        {'rua': 'R2', 'número': 125},
#    ],
#    'altura': 1.70,
#    'números preferidos': (2, 4, 6, 8, 10),
#    'dev': True,
#    'nada': None,
#}
# Criar arquivo
# with open("Arquivo02.json", "w", encoding='utf-8') as arquivo02:
#    json.dump(
#        pessoa,
#        arquivo02,
#        ensure_ascii=False,
#        indent=2,
#    )

# Lendo arquivo
with open("Arquivo02.json", "r", encoding='utf-8') as arquivo02:
    pessoa1 = json.load(arquivo02)
    # imprime tudo
    print(pessoa1)
    # imprime o valor da chave escolhida
    print(pessoa1['nome'])

    # TESTANDO 
    n = input('Digite seu nome: ')
    if n == pessoa1['nome']:
        print('Bem vindo')
    else:
        print('Errado.')
