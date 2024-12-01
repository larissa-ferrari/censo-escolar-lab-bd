
import hashlib
from core.connection import get_connection


# Função CREATE (Inserir usuário)
def create_user(name, email, password, is_adm, birthday):
    hashed_password = hash_password(password)
    conn = get_connection()
    cursor = conn.cursor()
    query = "INSERT INTO usuario (nome, email, senha, administrador, data_nascimento) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (name, email, hashed_password, is_adm, birthday))
    conn.commit()
    cursor.close()
    conn.close()

# Função READ (Buscar usuário por ID)
def get_user_by_id(user_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM usuario WHERE id = %s"
    cursor.execute(query, (user_id,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user

# Função READ (Listar todos os usuários)
def get_all_users():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM usuario"
    cursor.execute(query)
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return users

# Função UPDATE (Atualizar usuário)
def update_user(user_id, name, email, password=None, birthday=None, is_adm=False):
    conn = get_connection()
    cursor = conn.cursor()

    # Definir os campos a serem atualizados
    fields = []
    values = []
    
    # Atualiza o nome e o email
    query = "UPDATE usuario SET nome = %s, email = %s"
    fields.append("nome")
    fields.append("email")
    values.extend([name, email])

    # Se a senha for fornecida, inclui no UPDATE
    if password:
        hashed_password = hash_password(password)
        query += ", senha = %s"
        fields.append("senha")
        values.append(hashed_password)
    
    # Se a data de nascimento for fornecida, inclui no UPDATE
    if birthday:
        query += ", data_nascimento = %s"
        fields.append("data_nascimento")
        values.append(birthday)

    # Caso o administrador seja fornecido
    if is_adm is not None:
        query += ", administrador = %s"
        fields.append("administrador")
        values.append(is_adm)

    # Adiciona o filtro de ID
    query += " WHERE id = %s"
    values.append(user_id)

    # Executa o comando de atualização
    cursor.execute(query, tuple(values))
    conn.commit()
    cursor.close()
    conn.close()

# Função DELETE (Excluir usuário)
def delete_user(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    query = "DELETE FROM usuario WHERE id = %s"
    cursor.execute(query, (user_id,))
    conn.commit()
    cursor.close()
    conn.close()

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

# Função para criar hash SHA-1
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