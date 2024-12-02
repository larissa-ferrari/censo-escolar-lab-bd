import streamlit as st
from src.controllers.schools import get_schools_qtd_dashboard_with_docente
import pandas as pd

st.title("Escolas da Cidade")
st.subheader("Visão da Escola")
    
with st.spinner("Carregando Escolas..."):
    bookmarks = get_schools_qtd_dashboard_with_docente()

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