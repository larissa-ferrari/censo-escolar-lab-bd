from src.core.connection import get_connection

def get_class_by_school_id(filters=None):
    connection = get_connection()
    try:
        with connection.cursor(dictionary=True) as cursor:
            query = """                
                SELECT     
                    ID_TURMA,
                    NO_TURMA, 
                    IN_DISC_QUIMICA,
                    IN_DISC_FISICA,
                    IN_DISC_MATEMATICA,
                    IN_DISC_BIOLOGIA,
                    IN_DISC_CIENCIAS,
                    IN_DISC_LINGUA_PORTUGUESA,
                    IN_DISC_LINGUA_INGLES,
                    IN_DISC_LINGUA_ESPANHOL,
                    IN_DISC_LINGUA_FRANCES,
                    IN_DISC_LINGUA_OUTRA,
                    IN_DISC_LINGUA_INDIGENA,
                    IN_DISC_ARTES,
                    IN_DISC_EDUCACAO_FISICA,
                    IN_DISC_HISTORIA,
                    IN_DISC_GEOGRAFIA,
                    IN_DISC_FILOSOFIA,
                    IN_DISC_ENSINO_RELIGIOSO,
                    IN_DISC_ESTUDOS_SOCIAIS,
                    IN_DISC_SOCIOLOGIA,
                    IN_DISC_EST_SOCIAIS_SOCIOLOGIA,
                    IN_DISC_INFORMATICA_COMPUTACAO,
                    IN_DISC_PROFISSIONALIZANTE,
                    IN_DISC_ATENDIMENTO_ESPECIAIS,
                    IN_DISC_DIVER_SOCIO_CULTURAL,
                    IN_DISC_LIBRAS,
                    IN_DISC_PEDAGOGICAS,
                    IN_DISC_OUTRAS
                FROM turmas
            """

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
