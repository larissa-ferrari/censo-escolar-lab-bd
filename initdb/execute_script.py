import pandas as pd
import pymysql

# Configuração do banco de dados
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'censo_escolar',
    'port': 3306,
}

# Função para carregar e normalizar os dados do Excel para o banco de dados
def load_excel_to_db(file_path, table_name, sep=";"):
    try:
        # Carregar o CSV
        print("Carregando dados do CSV...")
        df = pd.read_csv(file_path, sep=sep)

        df = df.fillna(0)

        # Conectar ao banco de dados
        print("Conectando ao banco de dados...")
        connection = pymysql.connect(**db_config)
        cursor = connection.cursor()

        # Preparar o INSERT
        columns = ", ".join(df.columns)
        placeholders = ", ".join(["%s"] * len(df.columns))
        sql_insert = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"

        # Inserir cada linha no banco
        for _, row in df.iterrows():
            values = tuple(row)  # Cada linha como uma tupla

            # Verificar valores antes de inserir
            print(f"Inserindo linha {values}:")

            # Inserir os dados na tabela
            cursor.execute(sql_insert, values)

        # Confirmar a inserção
        connection.commit()
        print(f"{cursor.rowcount} registros inseridos na tabela {table_name}!")

    except Exception as err:
        print(f"Erro ao processar o arquivo {file_path}: {err}")
    finally:
        if 'connection' in locals():
            cursor.close()
            connection.close()

# Arquivos e tabelas a serem processados
files_and_tables = [
    {"file_path": "escolas.csv", "table_name": "escola"},
    {"file_path": "turmas.csv", "table_name": "turma"}, 
    {"file_path": "docentes.csv", "table_name": "docentes"},
    {"file_path": "matriculas.csv", "table_name": "matricula"},
    {"file_path": "ideb.csv", "table_name": "ideb", "separator": ";"},
]

# Processar os arquivos
for file_info in files_and_tables:
    load_excel_to_db(file_info["file_path"], file_info["table_name"], file_info.get("separator", "|"))