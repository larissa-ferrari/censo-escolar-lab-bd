import streamlit as st
from src.controllers.schools import list_schools, list_schools
import pandas as pd

st.title("Escolas da Cidade")
st.subheader("Lista de Escolas por Cidade")
    
with st.spinner("Carregando Escolas..."):
    bookmarks = list_schools()

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