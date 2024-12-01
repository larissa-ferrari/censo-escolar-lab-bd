from src.core.connection import get_connection

# Função CREATE (Inserir bookmark)
def create_bookmark(user_id, school_id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            query = "INSERT INTO bookmark (id_usuario, id_escola) VALUES (%s, %s)"
            cursor.execute(query, (user_id, school_id))
            connection.commit()
    finally:
        connection.close()

# Função READ (Buscar bookmark por ID)
def get_bookmark_by_id(bookmark_id):
    connection = get_connection()
    try:
        with connection.cursor(dictionary=True) as cursor:
            query = "SELECT * FROM bookmark WHERE id = %s"
            cursor.execute(query, (bookmark_id,))
            return cursor.fetchone()
    finally:
        connection.close()

# Função READ (Listar todos os bookmarks)
def get_all_bookmarks(filters=None):
    connection = get_connection()
    try:
        with connection.cursor(dictionary=True) as cursor:
            query = """
                SELECT 
                    bookmark.*,
                    escola.NO_ENTIDADE AS escola_nome
                FROM 
                    bookmark
                LEFT JOIN 
                    escola ON bookmark.id_escola = escola.CO_ENTIDADE
            """

            values = []

            if filters:
                where_clauses = []
                for column, value in filters.items():
                    where_clauses.append(f"{column} = %s")
                    values.append(value)

                query += " WHERE " + " AND ".join(where_clauses)

            # Executa a query
            cursor.execute(query, tuple(values))
            return cursor.fetchall()
    finally:
        connection.close()


# Função DELETE (Excluir bookmark)
def delete_bookmark(bookmark_id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            query = "DELETE FROM bookmark where id = %s"
            cursor.execute(query, (bookmark_id,))
            connection.commit()
    finally:
        connection.close()
        
        
# Função para verificar se o bookmark já existe
def bookmark_exists(user_id, school_id):
    connection = get_connection()
    try:
        with connection.cursor(dictionary=True) as cursor:
            query = """
                SELECT 1
                FROM bookmark
                WHERE id_usuario = %s AND id_escola = %s
                LIMIT 1
            """
            cursor.execute(query, (user_id, school_id))
            return cursor.fetchone() is not None
    finally:
        connection.close()
