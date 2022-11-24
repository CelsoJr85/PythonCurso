"""SPLIT JOIN STRIP"""

frase = "Olha só, que coisa interessante"
# Split tira caracteres
sp_frase = frase.split(",")

for i, frase in enumerate(sp_frase):
    # Strip corta espaços vazios no início e no fim.
    print(sp_frase[i].strip())

# Join insere caracteres
frase_n = "-".join('abc')
print(frase_n)