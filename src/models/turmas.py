from src.core.connection import get_connection

def get_all_classes(filters=None):
    connection = get_connection()
    try:
        with connection.cursor(dictionary=True) as cursor:
            query = """
                SELECT 
                    ID_TURMA,
                    NO_TURMA,
                    CO_ENTIDADE,
                    TX_HR_INICIAL,
                    TX_MI_INICIAL,
                    NU_DURACAO_TURMA,
                    NU_MATRICULAS
                FROM turma"""

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

def get_class_by_school_id(school_name):
    connection = get_connection()
    try:
        with connection.cursor(dictionary=True) as cursor:
            query = """                
                SELECT
                    t.NO_TURMA, 
                    t.IN_DISC_QUIMICA,
                    t.IN_DISC_FISICA,
                    t.IN_DISC_MATEMATICA,
                    t.IN_DISC_BIOLOGIA,
                    t.IN_DISC_CIENCIAS,
                    t.IN_DISC_LINGUA_PORTUGUESA,
                    t.IN_DISC_LINGUA_INGLES,
                    t.IN_DISC_LINGUA_ESPANHOL,
                    t.IN_DISC_LINGUA_FRANCES,
                    t.IN_DISC_LINGUA_OUTRA,
                    t.IN_DISC_LINGUA_INDIGENA,
                    t.IN_DISC_ARTES,
                    t.IN_DISC_EDUCACAO_FISICA,
                    t.IN_DISC_HISTORIA,
                    t.IN_DISC_GEOGRAFIA,
                    t.IN_DISC_FILOSOFIA,
                    t.IN_DISC_ENSINO_RELIGIOSO,
                    t.IN_DISC_ESTUDOS_SOCIAIS,
                    t.IN_DISC_SOCIOLOGIA,
                    t.IN_DISC_EST_SOCIAIS_SOCIOLOGIA,
                    t.IN_DISC_INFORMATICA_COMPUTACAO,
                    t.IN_DISC_PROFISSIONALIZANTE,
                    t.IN_DISC_ATENDIMENTO_ESPECIAIS,
                    t.IN_DISC_DIVER_SOCIO_CULTURAL,
                    t.IN_DISC_LIBRAS,
                    t.IN_DISC_PEDAGOGICAS,
                    t.IN_DISC_OUTRAS
                FROM turma t
                JOIN escola e ON t.CO_ENTIDADE = e.CO_ENTIDADE
                WHERE e.NO_ENTIDADE = %s
            """

            # Executa a query
            cursor.execute(query, (str(school_name),))

            return cursor.fetchall()
    finally:
        connection.close()