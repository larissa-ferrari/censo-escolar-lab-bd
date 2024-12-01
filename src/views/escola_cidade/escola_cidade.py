import streamlit as st
from src.controllers.schools import list_schools, list_schools_by_city, list_cities_from_schools
import pandas as pd

st.title("Escolas da Cidade")
st.subheader("Lista de Escolas por Cidade")

with st.spinner("Carregando lista de municípios..."):
    cities = list_cities_from_schools()

if not cities:
    st.error("Nenhum município disponível no momento.")
else:
    city_options = [city["CO_MUNICIPIO"] for city in cities]
    selected_city_code = st.selectbox(
        "Selecione um município para filtrar as escolas:",
        options=city_options,
        format_func=lambda x: f"Código do Município: {x}",
    )

if selected_city_code:
    with st.spinner("Carregando Escolas..."):
        bookmarks = list_schools_by_city(selected_city_code)

    df = pd.DataFrame(bookmarks)

    if df.empty:
        st.info("Nenhuma Escola Encontrada!")
    else:
        df = df.rename(columns={
            "NO_ENTIDADE": "Nome",
            "TP_SITUACAO_FUNCIONAMENTO": "Status de Funcionamento",
            "CO_MUNICIPIO": "Município",
            "TP_LOCALIZACAO": "Localização",
            "TP_DEPENDENCIA": "Dependência",
            "Níveis_Atendidos": "Níveis Atendidos",
        })

        df = df.reset_index(drop=True)

        st.dataframe(df, use_container_width=True)