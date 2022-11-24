"""WHILE ( Enquanto )"""
# Repetição
# While executa o código enquanto este for verdadeiro.

# Digite nome e ele volta ao início, sair ele para.
while True:
    nome = input(" Digite seu nome, ou sair para sair: ")
    if nome != "sair":
        print(f"Seu nome é {nome}")
    else:
        break

# Repetição para contar de 0 a 10.
contador = 0
while contador < 10:
    contador = contador + 1
    print(contador)
