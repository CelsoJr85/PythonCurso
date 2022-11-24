# Importações
import json
from Pessoa import arq_path, Pessoa1

# Abrindo o arquivo
with open(arq_path, "r") as arquivo:
    pessoas = json.load(arquivo)
    print(pessoas)
