import streamlit as st
from src.controllers.student import list_students
import pandas as pd

st.title("Matrículas")
st.subheader("Visão da Matrícula")
    
with st.spinner("Carregando Matrículas..."):
    bookmarks = list_students()

df = pd.DataFrame(bookmarks)

if df.empty:
    st.info("Nenhuma Matrículas Encontrada!")
else:
    df = df.rename(columns={
        "ID_MATRICULA": "Código da matrícula",
        "NU_IDADE": "Idade do aluno",        
    })

    df = df.reset_index(drop=True)

    st.dataframe(df, use_container_width=True)