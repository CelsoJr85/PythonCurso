"""OPERADORES LÓGICOS"""

# And ( e ), Or ( ou ), Not ( não ), In ( em ) e Not In ( Não está em )
# And faz junção entre parametros.
a = 5
b = 6

if a == 5 and b == 6:
    print("Verdadeiro.")

# Or ou um parâmetro OU outro é verdadeiro, ou so dois:

if a == 5 or b != 6:
    print("Verdadeiro.")

# Not inverte a lógica.
if not a == 6:
    print("Falso.")

# In verifica se está no parâmentro.
nome = "Celso"

if "e" in nome:
    print("Verdadeiro")
else:
    print("Falso")

# Not In verifica se o argumento não está em parâmetros
if "b" not in nome:
    print("Vedadeiro.")
else:
    print("Falso")