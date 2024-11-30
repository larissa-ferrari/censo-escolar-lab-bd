import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np


def show_dashboard():
    # Gerando um DataFrame de exemplo com mais dados
    np.random.seed(42)

    # Definindo as categorias, anos e valores
    categorias = ['A', 'B', 'C', 'D', 'E']
    anos = [2020, 2021, 2022, 2023, 2024]
    status = ['Pendente', 'Concluído']

    # Criando um DataFrame com múltiplas combinações de Ano e Categoria
    data = {
        'Categoria': np.random.choice(categorias, size=100),
        'Valor': np.random.randint(100, 1000, size=100),  # Valores entre 100 e 1000
        'Ano': np.random.choice(anos, size=100),
        'Status': np.random.choice(status, size=100),
    }

    df = pd.DataFrame(data)

    # Definindo as cores para cada categoria
    categoria_cores = {
        'A': 'blue',
        'B': 'green',
        'C': 'red',
        'D': 'orange',
        'E': 'purple'
    }

    # Sidebar - Filtros
    st.sidebar.title("Filtros de Análise")

    # Legenda explicativa na Sidebar sobre as Cores
    st.sidebar.markdown("""
        ### Legenda de Cores para Categorias
        - **Categoria A:** Azul
        - **Categoria B:** Verde
        - **Categoria C:** Vermelho
        - **Categoria D:** Laranja
        - **Categoria E:** Roxo
    """)

    # Filtro de Categoria - Múltipla Seleção
    categoria_filtro = st.sidebar.multiselect(
        "Selecione as Categorias", options=df['Categoria'].unique(), default=df['Categoria'].unique()
    )

    # Filtro de Faixa de Valores
    valor_min, valor_max = st.sidebar.slider(
        "Selecione a Faixa de Valores",
        min_value=int(df['Valor'].min()),
        max_value=int(df['Valor'].max()),
        value=(int(df['Valor'].min()), int(df['Valor'].max()))
    )

    # Filtro de Ano - Múltipla Seleção
    ano_filtro = st.sidebar.multiselect(
        "Selecione os Anos", options=df['Ano'].unique(), default=df['Ano'].unique()
    )

    # Filtrando os Dados com base nos Filtros
    df_filtrado = df[
        (df['Categoria'].isin(categoria_filtro)) &
        (df['Valor'] >= valor_min) &
        (df['Valor'] <= valor_max) &
        (df['Ano'].isin(ano_filtro))
    ]

    # Layout do Dashboard
    st.title("Dashboard de Análise de Dados")

    # Primeira Linha: KPIs
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Total de Valores", value=f'{df_filtrado["Valor"].sum()}')
    with col2:
        st.metric(label="Média de Valores", value=f'{df_filtrado["Valor"].mean():.2f}')
    with col3:
        st.metric(label="Valor Máximo", value=f'{df_filtrado["Valor"].max()}')

    # Corpo do Dashboard

    # Criando 2 colunas para separar o Overview (esquerda) e o Depth Analysis (direita)
    col_left, col_right = st.columns([3, 2])  # 2 para a coluna esquerda e 3 para a coluna direita

    with col_left:
        # Overview: Gráfico de Barras
        st.markdown("## Overview")
        st.write("Aqui você pode incluir gráficos gerais que resumem os dados filtrados.")
        fig = px.bar(df_filtrado, x='Categoria', y='Valor', title="Distribuição dos Valores por Categoria",
                    color='Categoria', color_discrete_map=categoria_cores)
        st.plotly_chart(fig, use_container_width=True)

    with col_right:
        # Análise Profunda: Gráfico de Pizza e Linha
        st.markdown("## Análise Profunda")
        st.write("Gráficos mais profundos para análise detalhada dos dados.")
        
        # Gráfico de Pizza
        fig2 = px.pie(df_filtrado, names='Categoria', values='Valor', title="Distribuição Percentual por Categoria",
                    color='Categoria', color_discrete_map=categoria_cores)
        st.plotly_chart(fig2, use_container_width=True)

        # Gráfico de Linha (Evolução dos Valores ao Longo dos Anos)
        fig3 = px.line(df_filtrado, x='Ano', y='Valor', title="Evolução dos Valores ao Longo dos Anos",
                    color='Categoria', color_discrete_map=categoria_cores)
        st.plotly_chart(fig3, use_container_width=True)

    # Tabela de Dados
    st.markdown("### Tabela de Dados")
    st.dataframe(df_filtrado, use_container_width=True)

    col_left, col_right = st.columns([3, 2])

    with col_left:
        # Action Items
        st.markdown("## Action Items")
        action_items = [
            "Verificar as categorias com maior valor.",
            "Analisar os dados de vendas de 2024.",
            "Implementar ação para aumentar valores nas categorias 'Pendente'."
        ]
        for item in action_items:
            st.write(f"- {item}")

    with col_right:
        # Row-level Data
        st.markdown("## Row-level Data")
        st.write(
            "Aqui estão os dados detalhados para cada linha, conforme os filtros aplicados:")
        st.dataframe(df_filtrado, use_container_width=True)