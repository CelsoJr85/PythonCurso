"""VARIÁVEL E CONSTANTE"""

# Variável muda de valor.
# É escrita em minúscula.
velocidade = 61
local_do_carro = 98


# Constante não existe no Python, tudo é variável.
# Porém, pode usar uma variável simbolizando uma constante.
# É escrita em Maiúscula.
RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

if velocidade > RADAR_1:
    print("Multado.")


if (LOCAL_1 - RADAR_RANGE) <= local_do_carro <= (LOCAL_1 + RADAR_RANGE):
    print("Multado 2.")
