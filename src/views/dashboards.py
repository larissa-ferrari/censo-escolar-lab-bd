import streamlit as st
import plotly.express as px
from src.controllers.dashboards import (
    process_schools_data,
    process_turmas_data,
    process_docentes_data
)

st.title("Dashboard Educacional")

with st.spinner("Carregando Dados..."):
    # Dados reais do banco
    schools_data = process_schools_data()
    turmas_data = process_turmas_data()
    docentes_data = process_docentes_data()

# Definindo cores específicas para as categorias
situacao_cores = {
    'Ativa': 'green',
    'Paralisada': 'orange',
    'Extinta': 'red',
    'Extinta em Anos Anteriores': 'blue'
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
        names='TP_SITUACAO_FUNCIONAMENTO',
        title="Distribuição de Escolas por Situação",
        color='TP_SITUACAO_FUNCIONAMENTO',        
        color_discrete_map=situacao_cores,
    )
    fig1.update_traces(hovertemplate='%{label}: %{percent} (%{value})')
    st.plotly_chart(fig1, use_container_width=True)

# Gráfico: Turmas por Etapa de Ensino
with col2:
    st.subheader("Turmas por Etapa de Ensino")
    fig2 = px.bar(
        turmas_data_filtrado,
        x='TP_ETAPA_ENSINO',
        y='TOTAL_TURMAS',
        title="Turmas por Etapa de Ensino",
        color='TP_ETAPA_ENSINO',
        color_discrete_map=etapa_cores,
        labels={'TP_ETAPA_ENSINO': 'Etapa de Ensino', 'TOTAL_TURMAS': 'Total de Turmas'}
    )    
    st.plotly_chart(fig2, use_container_width=True)

# Gráfico: Docentes por Função
col3, col4 = st.columns(2)
with col3:
    st.subheader("Docentes por Função")
    fig3 = px.bar(
        docentes_data,
        x='TP_TIPO_DOCENTE',
        y='TOTAL_DOCENTES',
        title="Docentes por Função",
        color='TP_TIPO_DOCENTE',
        color_discrete_map=docente_cores,
        labels={'TP_TIPO_DOCENTE': 'Tipo do Docente', 'TOTAL_DOCENTES': 'Total de Docentes'}
    )
    st.plotly_chart(fig3, use_container_width=True)

# Tabela de Dados
st.markdown("### Dados das Escolas")
schools_data_filtrado.rename(columns={
    'CO_ENTIDADE': 'Código da Escola',
    'NO_ENTIDADE': 'Nome da Escola',
    'CO_UF': 'Código da UF',
    'CO_MUNICIPIO': 'Código do Município',
    'TP_SITUACAO_FUNCIONAMENTO': 'Situação de Funcionamento'
}, inplace=True)

# Exibe o DataFrame com os novos nomes das colunas
st.dataframe(schools_data_filtrado, use_container_width=True)
