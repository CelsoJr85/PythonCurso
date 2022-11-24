# Imports
import json

# Criando o caminho do arquivo JSON
arq_path = "agendasimples.json"

# Criando POO
class Pessoa1:
    def __init__(self, nome, sobrenome, idade, endereco, telefone, email):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.endereco = endereco
        self.telefone = telefone
        self.email = email

# Entradas de Dados
a = Pessoa1("celso", "custodio junior", 37, "estevão fernandes", "(11)9999-9999", "celso@mss.com.br")
b = Pessoa1("fernanda", "pereira custodio", 46, "estevão fernandes", "(11)8888-8888", "fefe@mss.com.br")
c = Pessoa1("isabel", "custodio", 8, "macuco", "(11)7777-7777", "isabel@mss.com.br")


# Salvando em uma variavél
pessoa = [vars(a), b.__dict__, vars(c)]

# Criando o arquivo JSON
with open(arq_path, 'w') as arquivo:
    json.dump(pessoa, arquivo, ensure_ascii=False, indent=2)