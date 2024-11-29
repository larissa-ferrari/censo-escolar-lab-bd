import sqlite3

# Conectar ou criar o banco de dados
conn = sqlite3.connect('censo_escolar.db')
cursor = conn.cursor()

# Criar tabela de usuários
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL
)
''')

# Confirmar e fechar
conn.commit()
conn.close()
