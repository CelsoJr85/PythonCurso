""" Funções Def (Definição) """

# def nome da função(com parâmetro):
#    ação que irá retornar
#
# def nome da função(sem parâmetro):
#    não retorna nada
#    ação executa algo, como fechar tela ou ir para outra tela,
#        imprimir algo, ou computar algo.
d = 5

# Com parâmetros e variavel interno somente para esta função:
def conta_soma(a, b):
    resultado = a + b
    print(" = ", resultado)

# Sem parâmetros:
c = []
def cadastrar():
    c.append("Celso")
    print(c)

# usando uma variavel global
def global_soma():
    global d
    print("global = ", d + 5)

# chamando uma função dentro de outra função
def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar

s1 = criar_saudacao('Bom dia')
s2 = criar_saudacao('Olá')
print(s1('Fernanda'))
print(s2('Celso'))

if __name__ == "__main__":
    # começa com a saudação e depois vai para:
    a = float(input("Digite um numero: "))
    b = float(input("Digite um número: "))
    # chamar o def conta_soma usando o input
    conta_soma(a, b)
    # chamar a mesma conta_soma só que passando um valor direto como argumento
    conta_soma(3, 5)

    # chama a seguna def como exemplo que acrescentou algo
    cadastrar()

    # chamar a def global
    global_soma()


