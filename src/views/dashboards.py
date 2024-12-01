import streamlit as st
import plotly.express as px
from src.controllers.dashboards import (
    process_schools_data,
    process_turmas_data,
    process_docentes_data,
    process_schools_geolocation
)
import folium
from folium.plugins import MarkerCluster


st.title("Dashboard Educacional")

# Dados reais do banco
schools_data = process_schools_data()
turmas_data = process_turmas_data()
docentes_data = process_docentes_data()
geolocation_data = process_schools_geolocation()

# Definindo cores específicas para as categorias
situacao_cores = {
    'Ativa': 'green',
    'Paralisada': 'orange',
    'Extinta': 'red'
}
etapa_cores = {
    'Educação Infantil': 'blue',
    'Ensino Fundamental': 'purple',
    'Ensino Médio': 'cyan'
}
docente_cores = {
    'Professor Regular': 'blue',
    'Coordenador Pedagógico': 'green',
    'Supervisor Escolar': 'red'
}

# Sidebar - Filtros
st.sidebar.title("Filtros de Análise")

# Filtro de Categoria de Escolas
categorias_filtro = st.sidebar.multiselect(
    "Selecione Situações das Escolas",
    options=schools_data['TP_SITUACAO_FUNCIONAMENTO'].unique(),
    default=schools_data['TP_SITUACAO_FUNCIONAMENTO'].unique()
)

# Filtro de Etapas de Ensino
etapas_filtro = st.sidebar.multiselect(
    "Selecione as Etapas de Ensino",
    options=turmas_data['TP_ETAPA_ENSINO'].unique(),
    default=turmas_data['TP_ETAPA_ENSINO'].unique()
)

# Filtrando os Dados
schools_data_filtrado = schools_data[schools_data['TP_SITUACAO_FUNCIONAMENTO'].isin(categorias_filtro)]
turmas_data_filtrado = turmas_data[turmas_data['TP_ETAPA_ENSINO'].isin(etapas_filtro)]

# Primeira Linha: KPIs
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Total de Escolas", value=f'{len(schools_data_filtrado)}')
with col2:
    st.metric(label="Total de Turmas", value=f'{turmas_data_filtrado["TOTAL_TURMAS"].sum()}')
with col3:
    st.metric(label="Total de Docentes", value=f'{docentes_data["TOTAL_DOCENTES"].sum()}')

# Corpo do Dashboard

# Gráfico: Distribuição de Escolas por Situação
col1, col2 = st.columns(2)
with col1:
    st.subheader("Distribuição de Escolas por Situação")
    fig1 = px.pie(
        schools_data_filtrado,
        names='Situação de Funcionamento',
        title="Distribuição de Escolas por Situação",
        color='TP_SITUACAO_FUNCIONAMENTO',
        color_discrete_map=situacao_cores
    )
    st.plotly_chart(fig1, use_container_width=True)

# Gráfico: Turmas por Etapa de Ensino
with col2:
    st.subheader("Turmas por Etapa de Ensino")
    fig2 = px.bar(
        turmas_data_filtrado,
        x='Etapa de Ensino',
        y='Número de Turmas',
        title="Turmas por Etapa de Ensino",
        color='TP_ETAPA_ENSINO',
        color_discrete_map=etapa_cores
    )
    st.plotly_chart(fig2, use_container_width=True)

# FIXME:
# Gráfico: Docentes por Função e Mapa de Geolocalização
col3, col4 = st.columns(2)
with col3:
    st.subheader("Docentes por Função")
    fig3 = px.bar(
        docentes_data,
        x='Tipo de Docente',
        y='Número de Docentes',
        title="Docentes por Função",
        color='TP_TIPO_DOCENTE',
        color_discrete_map=docente_cores
    )
    st.plotly_chart(fig3, use_container_width=True)

# Mapa de Geolocalização na Coluna Direita
with col4:
    st.subheader("Mapa de Geolocalização das Escolas")
    st.text("Informações coletadas do dataset adicional fornecido no classroom")

    # Criando o mapa inicial (usando coordenadas médias do Brasil)
    mapa = folium.Map(location=[-14.235004, -51.92528], zoom_start=4)

    # Adicionando os pontos ao mapa usando MarkerCluster
    marker_cluster = MarkerCluster().add_to(mapa)

    # Iterando pelos dados e adicionando marcadores
    for _, row in geolocation_data.iterrows():
        folium.Marker(
            location=[row['LAT'], row['LNG']],
            popup=f"{row['NO_ENTIDADE']} ({row['LAT']}, {row['LNG']})"
        ).add_to(marker_cluster)

    # Exibindo o mapa no Streamlit
    st.components.v1.html(mapa._repr_html_(), height=500)

# Tabela de Dados
st.markdown("### Dados das Escolas")
st.dataframe(schools_data_filtrado, use_container_width=True)

# Análise Profunda
st.markdown("## Análise Profunda")
st.write("Gráficos detalhados baseados nos dados filtrados.")

# Gráfico Evolução (Exemplo com dummy data)
fig5 = px.line(
    turmas_data_filtrado,
    x='Etapa de Ensino',
    y='Número de Turmas',
    title="Evolução de Turmas por Etapa de Ensino",
)
st.plotly_chart(fig5, use_container_width=True)
