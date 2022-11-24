# Importações
# para instalar usar pip install db-sqlite3
import sqlite3

# Criando conexão
conn = sqlite3.connect('basededados.db')
# Criando um cursor
cursor = conn.cursor()
"""
# Execuntando um comando para criar uma tabela se ela não existir
cursor.execute('CREATE TABLE IF NOT EXISTS clientes ('
        #coluna1   int      chave primária inclemento em ordem crescente
               'id INTEGER PRIMARY KEY AUTOINCREMENT,'
                    #String
               'nome TEXT,'
                    #Float
               'peso REAL'
               ')')

# Inserindo dados na tabela
cursor.execute('INSERT INTO clientes (nome, peso) VALUES ("Celso", 82.5)')
cursor.execute('INSERT INTO clientes (nome, peso) VALUES ("Fernanda", 66.2)')
cursor.execute('INSERT INTO clientes (nome, peso) VALUES ("Isabel", 48.3)')
# Salvar os dados
conn.commit()
"""
# Lendo os dados da tabela
cursor.execute('SELECT * FROM clientes')

# Escolhendo algo na tabela como se fosse um if
#cursor.execute('SELECT nome, peso FROM clientes WHERE peso > 50')
# Mostrando todas linhas da tabela fatchall
for linha in cursor.fetchall():
    print(linha)

# Fechando o cursor e a conexão
cursor.close()
conn.close()