import streamlit as st
from src.controllers.turmas import list_all_classes
import pandas as pd

st.title("Gerenciamento de Turmas")
st.subheader("Lista de Turmas")

with st.spinner("Carregando Turmas..."):
    bookmarks = list_all_classes()

df = pd.DataFrame(bookmarks)

if df.empty:
    st.info("Nenhuma Turma Encontrada!")
else:
    df = df.rename(columns={
        "NO_ENTIDADE": "Escola",
        "ID_TURMA": "Código",
        "NO_TURMA": "Nome",
        "NU_DURACAO_TURMA": "Duração da Turma",
        "NU_MATRICULAS": "Numero de Matriculas"
    })

    df = df.reset_index(drop=True)

    st.dataframe(df, use_container_width=True)