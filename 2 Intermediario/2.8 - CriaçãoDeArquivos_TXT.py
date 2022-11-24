""" CRIAÇÃO DE ARQUIVOS """

''' TXT'''
# Salvando local de criação numa variavel
caminho = "D:\\Python Projetos\\PythonCurso2022\\2 Intermediario\\"
caminho += "arquivo01.txt"
'''
# Criando o arquivo com o w = writer escrever/criar
arquivo = open(caminho, "w")
# Fechando arquivo
arquivo.close()
'''
# Segunda forma, mais usada:
# Escrevendo usando o w, e colocando o w+ tanto para escrever como para ler. utf-8 para caracteres ^ ~ ç.
with open(caminho, "w+", encoding='utf-8') as arquivo:
    # Escrevendo algo no arquivo
    arquivo.write("Linha1\n")
    arquivo.write("Linha2\n")
    arquivo.writelines(
        ("Linha3\n", "Linha4\n")
    )
    # Cursor de onde inicia a leitura
    arquivo.seek(0, 0)
    # Lendo usando o w+
    print(arquivo.read())
    print("Lendo")
    # Ler linha a linha
    arquivo.seek(0, 0)
    print(arquivo.readline(), end="") # Final como nada tira quebra de linha
    print(arquivo.readline().strip()) # Tira os espaços vazios no inicio e final, tira quebra de linha
    print(arquivo.readline())

# Lendo
with open(caminho, "r") as arquivo:
    # Lendo algo no arquivo
    print(arquivo.read())


# OS.REMOVE(ARQUIVO) apaga arquivo por completo