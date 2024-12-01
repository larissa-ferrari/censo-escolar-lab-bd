from src.models.dashboards import get_schools_data, get_turmas_data, get_docentes_data, get_schools_geolocation

# Função para preparar os dados das escolas
def process_schools_data():
    df = get_schools_data()
    df['TP_SITUACAO_FUNCIONAMENTO'] = df['TP_SITUACAO_FUNCIONAMENTO'].map({
        1: 'Ativa', 
        2: 'Paralisada', 
        3: 'Extinta'
    })
    return df

# Função para preparar os dados das turmas
def process_turmas_data():
    df = get_turmas_data()
    df['TP_ETAPA_ENSINO'] = df['TP_ETAPA_ENSINO'].map({
        1: 'Educação Infantil',
        2: 'Ensino Fundamental',
        3: 'Ensino Médio'
    })
    return df

# Função para preparar os dados dos docentes
def process_docentes_data():
    df = get_docentes_data()
    df['TP_TIPO_DOCENTE'] = df['TP_TIPO_DOCENTE'].map({
        1: 'Professor Regular',
        2: 'Coordenador Pedagógico',
        3: 'Supervisor Escolar'
    })
    return df

# Função para preparar a geolocalização
def process_schools_geolocation():
    df = get_schools_geolocation()
    # Simular geolocalização (real seria obtida de APIs externas)
    df['LAT'] = df['CO_UF'].apply(lambda x: -14.235004)  # Exemplo de latitude
    df['LNG'] = df['CO_MUNICIPIO'].apply(lambda x: -51.92528)  # Exemplo de longitude
    return df
