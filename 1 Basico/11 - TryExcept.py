""" TRY EXCEPT"""
"""Enquanto no If Else se tiver algum erro ele segue em frente, no try 
quando tem um erro ele pula direto para o except e finaliza."""

numero = input("Vou dobrar o número que digitar: ")
# Try tentar executar o código
try:
    numero_float = float(numero)
    print("Float: ", numero_float)
    # Se escrever uma letra, ele pula daqui para o except e finaliza.
    print(f"O dobro de {numero} é {numero_float * 2:.2f}")
# Except exceto ou erro no código
except:
    print("Isto não é um número.")