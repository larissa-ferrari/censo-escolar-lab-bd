from src.core.connection import get_connection

# Função READ (Buscar número de alunos por nível de ensino)
def get_ideb_grades_by_school():
    connection = get_connection()
    try:
        with connection.cursor(dictionary=True) as cursor:
            query = """
                SELECT
                    e.NO_ENTIDADE,
                    i.IDEB_AI,
                    i.IDEB_AF,
                    i.IDEB_EM
                FROM
                    ideb i
                JOIN escola e ON i.CO_ENTIDADE = e.CO_ENTIDADE;
            """
            cursor.execute(query)
            return cursor.fetchall()
    finally:
        connection.close()