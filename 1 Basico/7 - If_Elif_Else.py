"""IF ELIF ELSE"""
"""SE, SE NÃO SE, SE NÃO"""
'''Condição que recebe uma entrada e verifica ela parte a parte, se não for a primeira
 pula para a proxima ate que se encaixa em uma.'''

# Recebendo uma entrada
numero = int(input("digite um numero de 0 a 1: "))

# Se o numero for igual a 0, imprima seu numero é zero.
if numero == 0:
    print(f"Seu número é {numero}" )
# Senão for 0, tente ver se é 1.
elif numero == 1:
    print(f"Seu número é {numero}")
# Senão for nenhum dos ateriores.
else:
    print(f"{numero} não é um número válido.")


# Condição verdadeiro ou falso.
num = 10

if num == 10:
    print("Verdadeiro.")
else:
    print("Falso.")
