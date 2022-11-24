import sqlite3
import json

DB = "D:\\Python Projetos\\PythonCurso2022\\3 Avancado\\BANCO DE DADOS\\agenda.db"

def get_all_users(json_str=False):
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    db = conn.cursor()
    rows = db.execute('SELECT * FROM agenda').fetchall()
    conn.commit()
    conn.close()

    if json_str:
        return json.dump([dict(ix) for ix in rows])

    return rows


