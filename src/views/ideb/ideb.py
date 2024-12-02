import streamlit as st
from src.controllers.ideb import list_ideb_grades_by_school
import pandas as pd

st.title("Notas do Ideb por Escola")

# Carregar as escolas com base no filtro
with st.spinner("Carregando as notas do Ideb por escola..."):
    ideb_grades_by_school = list_ideb_grades_by_school()

# Converter para DataFrame
df = pd.DataFrame(ideb_grades_by_school)

# Mostrar os resultados
if df.empty:
    st.info("O número de escolas com nota no Ideb é zero!")
else:
    df.rename(columns={
    "NO_ENTIDADE": "Escola",
    "IDEB_AI": "Ensino Infantil",
    "IDEB_AF": "Ensino Fundamental",
    "IDEB_EM": "Ensino Médio"
    }, inplace=True)
    st.dataframe(df, use_container_width=True)