import sqlite3

# Função para conectar ao banco de dados SQLite


def get_connection():
    return sqlite3.connect('censo_escolar.db')

# Função para pegar todos os usuários


def get_users():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuario")
    users = cursor.fetchall()
    conn.close()
    return users

# Função para adicionar um novo usuário


def insert_user(username, password):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO usuario (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()

# Função para deletar um usuário


def delete_user(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM usuario WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()
