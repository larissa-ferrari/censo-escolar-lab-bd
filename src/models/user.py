
import bcrypt
from core.connection import get_connection


# Função CREATE (Inserir usuário)
def create_user(username, password):
    hashed_password = hash_password(password)
    conn = get_connection()
    cursor = conn.cursor()
    query = "INSERT INTO users (username, password) VALUES (%s, %s)"
    cursor.execute(query, (username, hashed_password))
    conn.commit()
    cursor.close()
    conn.close()

# Função READ (Buscar usuário por ID)
def get_user_by_id(user_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM users WHERE id = %s"
    cursor.execute(query, (user_id,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user

# Função READ (Listar todos os usuários)
def get_all_users():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM users"
    cursor.execute(query)
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return users

# Função UPDATE (Atualizar usuário)
def update_user(user_id, username, password):
    hashed_password = hash_password(password)
    conn = get_connection()
    cursor = conn.cursor()
    query = "UPDATE users SET username = %s, password = %s WHERE id = %s"
    cursor.execute(query, (username, hashed_password, user_id))
    conn.commit()
    cursor.close()
    conn.close()

# Função DELETE (Excluir usuário)
def delete_user(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    query = "DELETE FROM users WHERE id = %s"
    cursor.execute(query, (user_id,))
    conn.commit()
    cursor.close()
    conn.close()

# Função para buscar usuário no banco
def get_user_by_username(username):
    connection = get_connection()
    try:
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute(
                "SELECT * FROM users WHERE username = %s", (username,))
            return cursor.fetchone()
    finally:
        connection.close()

# Função para criar hash da senha
def hash_password(password):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode("utf-8"), salt)

# Função para verificar senha
def check_password(password, hashed_password):
    return bcrypt.checkpw(password.encode("utf-8"), hashed_password.encode("utf-8"))
    # return True
