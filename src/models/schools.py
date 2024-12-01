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
            query = "SELECT NO_ENTIDADE, CO_ENTIDADE, DT_ANO_LETIVO_INICIO, DT_ANO_LETIVO_TERMINO, TP_SITUACAO_FUNCIONAMENTO FROM escola"

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

def get_schools_dashboard():
    connection = get_connection()
    try:
        with connection.cursor(dictionary=True) as cursor:
            query = """
                SELECT 
                    e.CO_ENTIDADE, 
                    e.NO_ENTIDADE,
                    e.TP_SITUACAO_FUNCIONAMENTO,
                    e.CO_MUNICIPIO,
                    e.TP_LOCALIZACAO,
                    e.TP_DEPENDENCIA,
                    GROUP_CONCAT(DISTINCT Etapa_Ensino(t.TP_ETAPA_ENSINO) SEPARATOR ', ') AS Níveis_Atendidos
                FROM 
                    escola e
                LEFT JOIN 
                    turma t
                ON 
                    e.CO_ENTIDADE = t.CO_ENTIDADE
                GROUP BY 
                    e.CO_ENTIDADE, 
                    e.NO_ENTIDADE,
                    e.TP_SITUACAO_FUNCIONAMENTO,
                    e.CO_MUNICIPIO,
                    e.TP_LOCALIZACAO,
                    e.TP_DEPENDENCIA;
            """

            # Executa a query
            cursor.execute(query,)
            return cursor.fetchall()
    finally:
        connection.close()
