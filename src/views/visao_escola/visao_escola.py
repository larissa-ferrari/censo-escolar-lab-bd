import streamlit as st
from src.controllers.schools import list_school_qtd_dashboard
import pandas as pd

st.title("Escolas da Cidade")
st.subheader("Visão da Escola")
    
with st.spinner("Carregando Escolas..."):
    bookmarks = list_school_qtd_dashboard()

df = pd.DataFrame(bookmarks)

if df.empty:
    st.info("Nenhuma Escola Encontrada!")
else:
    df = df.rename(columns={
        "CO_ENTIDADE": "Código",
        "NO_ENTIDADE": "Nome",
        "Docentes": "Qtd. Professores",
        "Matricula": "Qtd. Alunos",
        "Turmas": "Qtd. Turmas",
    })

    df = df.reset_index(drop=True)

    st.dataframe(df, use_container_width=True)