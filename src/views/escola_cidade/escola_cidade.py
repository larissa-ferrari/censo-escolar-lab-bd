import streamlit as st
from src.controllers.schools import list_schools, list_school_dashboard
import pandas as pd

st.title("Escolas da Cidade")
st.subheader("Lista de Escolas da Cidade")
    
with st.spinner("Carregando Escolas..."):
    bookmarks = list_school_dashboard()

df = pd.DataFrame(bookmarks)

if df.empty:
    st.info("Nenhuma Escola Encontrada!")
else:
    df = df.rename(columns={
        "CO_ENTIDADE": "Código",
        "NO_ENTIDADE": "Nome",
        "TP_SITUACAO_FUNCIONAMENTO": "Status de Funcionamento",
        "CO_MUNICIPIO": "Município",
        "TP_LOCALIZACAO": "Localização",
        "TP_DEPENDENCIA": "Dependência",
        "Níveis_Atendidos": "Níveis Atendidos",
    })

    df = df.reset_index(drop=True)

    st.dataframe(df, use_container_width=True)