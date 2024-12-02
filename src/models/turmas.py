from src.core.connection import get_connection

def get_class_by_school_id(school_name):
    connection = get_connection()
    try:
        with connection.cursor(dictionary=True) as cursor:
            query = """                
                SELECT     
                    t.ID_TURMA,
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
                FROM turmas
                JOIN escolas ON t.CO_ENTIDADE = escolas.CO_ENTIDADE
                WHERE escolas.NO_ENTIDADE = %s
            """

            # Executa a query
            cursor.execute(query, (school_name))
            return cursor.fetchall()
    finally:
        connection.close()
