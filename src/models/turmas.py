from src.core.connection import get_connection

def get_class_by_school_id(filters=None):
    connection = get_connection()
    try:
        with connection.cursor(dictionary=True) as cursor:
            query = """                
                SELECT     
                    ID_TURMA int,
                    NO_TURMA varchar(80), 
                    IN_DISC_QUIMICA bool,
                    IN_DISC_FISICA bool,
                    IN_DISC_MATEMATICA bool,
                    IN_DISC_BIOLOGIA bool,
                    IN_DISC_CIENCIAS bool,
                    IN_DISC_LINGUA_PORTUGUESA bool,
                    IN_DISC_LINGUA_INGLES bool,
                    IN_DISC_LINGUA_ESPANHOL bool,
                    IN_DISC_LINGUA_FRANCES bool,
                    IN_DISC_LINGUA_OUTRA bool,
                    IN_DISC_LINGUA_INDIGENA bool,
                    IN_DISC_ARTES bool,
                    IN_DISC_EDUCACAO_FISICA bool,
                    IN_DISC_HISTORIA bool,
                    IN_DISC_GEOGRAFIA bool,
                    IN_DISC_FILOSOFIA bool,
                    IN_DISC_ENSINO_RELIGIOSO bool,
                    IN_DISC_ESTUDOS_SOCIAIS bool,
                    IN_DISC_SOCIOLOGIA bool,
                    IN_DISC_EST_SOCIAIS_SOCIOLOGIA bool,
                    IN_DISC_INFORMATICA_COMPUTACAO bool,
                    IN_DISC_PROFISSIONALIZANTE bool,
                    IN_DISC_ATENDIMENTO_ESPECIAIS bool,
                    IN_DISC_DIVER_SOCIO_CULTURAL bool,
                    IN_DISC_LIBRAS bool,
                    IN_DISC_PEDAGOGICAS bool,
                    IN_DISC_OUTRAS bool 
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