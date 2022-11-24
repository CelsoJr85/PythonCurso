"""Login com dicionários"""

# Dicionário
login = {
    "usuario": "admin",
    "senha": 1234,
    "gerente": "celso",
    "senha_gerente": 1985,
}

# Tela login
print("==========LOGIN=========")
user = input("Digite seu usuário: ")
senha = int(input("Digite sua senha: "))
print("------------------------")

if user == login["usuario"]:
    if senha == login["senha"]:
        print("Bem vindo ", user)
    else:
        print("Senha errada!")
else:
    print("Digite um usuário válido.")