from core.connection import get_connection
import pandas as pd

# Função para buscar dados de escolas
def get_schools_data():
    conn = get_connection()
    query = """
        SELECT CO_ENTIDADE, NO_ENTIDADE, CO_UF, CO_MUNICIPIO, TP_SITUACAO_FUNCIONAMENTO 
        FROM escola;
    """
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# Função para buscar dados de turmas
def get_turmas_data():
    conn = get_connection()
    query = """
        SELECT TP_ETAPA_ENSINO, COUNT(ID_TURMA) AS TOTAL_TURMAS
        FROM turma
        GROUP BY TP_ETAPA_ENSINO;
    """
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# Função para buscar dados de docentes
def get_docentes_data():
    conn = get_connection()
    query = """
        SELECT TP_TIPO_DOCENTE, COUNT(CO_PESSOA_FISICA) AS TOTAL_DOCENTES
        FROM docente
        GROUP BY TP_TIPO_DOCENTE;
    """
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# Função para buscar geolocalização (mapa das escolas)
def get_schools_geolocation():
    conn = get_connection()
    query = """
        SELECT CO_ENTIDADE, NO_ENTIDADE, CO_UF, CO_MUNICIPIO 
        FROM escola
        WHERE CO_UF IS NOT NULL AND CO_MUNICIPIO IS NOT NULL;
    """
    df = pd.read_sql(query, conn)
    conn.close()
    return df
