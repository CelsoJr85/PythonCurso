# Importações
import sqlite3

# Criando uma Classe Agenda
class AgendaDB:
    def __init__(self, arquivo):
        self.conn = sqlite3.connect(arquivo)
        self.cursor = self.conn.cursor()

    # Criando métodos
    def inserir(self, nome, telefone):
        consulta = 'INSERT OR IGNORE INTO agenda (nome, telefone) VALUES (?, ?)'
        self.cursor.execute(consulta, (nome, telefone))
        self.conn.commit()

    def editar(self, nome, telefone, id):
        consulta = 'UPDATE OR IGNORE agenda SET nome=?, telefone=? WHERE id=?'
        self.cursor.execute(consulta, (nome, telefone, id))
        self.conn.commit()

    def excluir(self, id):
        consulta = 'DELETE FROM agenda WHERE id=?'
        self.cursor.execute(consulta, (id,))
        self.conn.commit()

    def listar(self):
        self.cursor.execute('SELECT * FROM agenda')
        for linha in self.cursor.fetchall():
            print(linha)

    def buscar(self, valor):
        consulta = 'SELECT * FROM agenda WHERE nome LIKE ?'
        self.cursor.execute(consulta, (f'%{valor}%',))
        for linha in self.cursor.fetchall():
            print(linha)

    def fechar(self):
        self.cursor.close()
        self.conn.close()

# Criando um iniciador
if __name__ == '__main__':
    # Abrindo o arquivo DB
    agenda = AgendaDB('agenda.db')
    # Inserindo um nome e telefone
    agenda.inserir("Nome", "00000000")
    # Editando um nome, telefone que esteja no id...
    agenda.editar("nome2", "99999999", 17)
    # Buscando um contato
    agenda.buscar('Celso')
    # Listando todos contatos
    agenda.listar()
