import streamlit as st
from src.controllers.turmas import list_class
from src.controllers.schools import list_schools
import pandas as pd

st.title("Escolas da Cidade")
st.subheader("Visão da Turma")

with st.spinner("Carregando Escolas..."):
    schools = list_schools(filters=None)

schools_df = pd.DataFrame(schools)

if not schools_df.empty:
    selected_school = st.selectbox(
        "Selecione a Escola", 
        options=schools_df['NO_ENTIDADE'].unique(),
        index=0
    )

    selected_co_entidade = schools_df[schools_df['NO_ENTIDADE'] == selected_school]['CO_ENTIDADE'].values[0]

    with st.spinner("Carregando Turmas..."):
        filtered_turmas = list_class(filters={"CO_ENTIDADE": selected_co_entidade})

    if filtered_turmas:
        df = pd.DataFrame(filtered_turmas)
        df = df.rename(columns={
            "ID_TURMA": "Código",
            "NO_TURMA": "Nome"
        })

        df = df.reset_index(drop=True)

        st.dataframe(df, use_container_width=True)
    else:
        st.info(f"Nenhuma Turma Encontrada para a Escola {selected_school}")
else:
    st.info("Nenhuma Escola Encontrada!")