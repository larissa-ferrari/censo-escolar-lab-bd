import hashlib
from src.core.connection import get_connection

# Função CREATE (Inserir usuário)
def create_user(name, email, password, is_adm, birthday):
    hashed_password = hash_password(password)
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            query = """
                INSERT INTO usuario (nome, email, senha, administrador, data_nascimento)
                VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(
                query, (name, email, hashed_password, is_adm, birthday))
            connection.commit()
    finally:
        connection.close()

# Função READ (Buscar usuário por ID)
def get_user_by_id(user_id):
    connection = get_connection()
    try:
        with connection.cursor(dictionary=True) as cursor:
            query = "SELECT * FROM usuario WHERE id = %s"
            cursor.execute(query, (user_id,))
            return cursor.fetchone()
    finally:
        connection.close()

# Função READ (Listar todos os usuários)
def get_all_users():
    connection = get_connection()
    try:
        with connection.cursor(dictionary=True) as cursor:
            query = "SELECT * FROM usuario"
            cursor.execute(query)
            return cursor.fetchall()
    finally:
        connection.close()

# Função UPDATE (Atualizar usuário)
def update_user(user_id, name, email, password=None, birthday=None, is_adm=None):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            # Monta a query dinamicamente
            set_clauses = ["nome = %s", "email = %s"]
            values = [name, email]

            if password:
                hashed_password = hash_password(password)
                set_clauses.append("senha = %s")
                values.append(hashed_password)

            if birthday:
                set_clauses.append("data_nascimento = %s")
                values.append(birthday)

            if is_adm is not None:
                set_clauses.append("administrador = %s")
                values.append(is_adm)

            # Adiciona o WHERE
            set_query = ", ".join(set_clauses)
            query = f"UPDATE usuario SET {set_query} WHERE id = %s"
            values.append(user_id)

            # Executa a query
            cursor.execute(query, tuple(values))
            connection.commit()
    finally:
        connection.close()

# Função DELETE (Excluir usuário)
def delete_user(user_id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            query = "DELETE FROM usuario WHERE id = %s"
            cursor.execute(query, (user_id,))
            connection.commit()
    finally:
        connection.close()

# Função para buscar usuário no banco
def get_user_by_email(email):
    connection = get_connection()
    try:
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute(
                "SELECT * FROM usuario WHERE email = %s", (email,))
            return cursor.fetchone()
    finally:
        connection.close()

# Função para criar hash SHA-1s
def hash_password(password):
    sha1_hash = hashlib.sha1()
    sha1_hash.update(password.encode('utf-8'))
    return sha1_hash.hexdigest()

# Função para verificar a senha
def check_password(password, stored_hash):
    # Cria o hash da senha fornecida
    password_hash = hash_password(password)

    # Compara o hash gerado com o hash armazenado
    return password_hash == stored_hash
