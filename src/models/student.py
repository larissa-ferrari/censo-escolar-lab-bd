from src.core.connection import get_connection

# Função READ (Buscar número de alunos por nível de ensino)
def get_number_students_by_level():
    connection = get_connection()
    try:
        with connection.cursor(dictionary=True) as cursor:
            query = """
                SELECT TP_ETAPA_ENSINO, SUM(NU_MATRICULAS) as SUM_MATRICULAS
                FROM turma
                GROUP BY TP_ETAPA_ENSINO
                ORDER BY SUM_MATRICULAS DESC;
            """
            cursor.execute(query)
            return cursor.fetchall()
    finally:
        connection.close()