import streamlit as st
from src.controllers.schools import list_schools
import pandas as pd

st.title("Gerenciamento de Escolas")
st.subheader("Lista de Escolas")

with st.spinner("Carregando Escolas..."):
    bookmarks = list_schools({
        "TP_SITUACAO_FUNCIONAMENTO": 1
    })

df = pd.DataFrame(bookmarks)

if df.empty:
    st.info("Nenhuma Escola Encontrada!")
else:
    df = df.rename(columns={
        "NO_ENTIDADE": "Escola",
        "CO_ENTIDADE": "Número x", # TODO: Validar here
        "DT_ANO_LETIVO_INICIO": "Inicio Ano Letivo",
        "DT_ANO_LETIVO_TERMINO": "Fim Ano Letivo"
    })

    df = df.drop(columns=["TP_SITUACAO_FUNCIONAMENTO"])

    df = df.reset_index(drop=True)

    st.dataframe(df, use_container_width=True)