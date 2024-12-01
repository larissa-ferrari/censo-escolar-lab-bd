from src.core.connection import get_connection

# Função READ (Buscar escola por ID)
def get_school_by_id(school_id):
    connection = get_connection()
    try:
        with connection.cursor(dictionary=True) as cursor:
            query = "SELECT * FROM escola WHERE id = %s"
            cursor.execute(query, (school_id,))
            
            return cursor.fetchone()
    finally:
        connection.close()

# Função READ (Listar todos as escolas)
def get_all_schools(filters=None):
    connection = get_connection()
    try:
        with connection.cursor(dictionary=True) as cursor:
            query = "SELECT * FROM escola"

            values = []

            # Adiciona filtros, se fornecidos
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