import streamlit as st
from src.controllers.student import list_number_students_by_level
import pandas as pd

st.title("Número de Alunos por Nível de Ensino")

# Carregar as escolas com base no filtro
with st.spinner("Carregando o número de alunos por nível de ensino..."):
    number_students_by_level = list_number_students_by_level()

# Converter para DataFrame
df = pd.DataFrame(number_students_by_level)

# Mostrar os resultados
if df.empty:
    st.info("O número de alunos é zero!")
else:
    df.rename(columns={
    'TP_ETAPA_ENSINO': 'Etapa de ensino',
    'SUM_MATRICULAS': 'Quantidade de alunos'
    }, inplace=True)
    st.dataframe(df, use_container_width=True)