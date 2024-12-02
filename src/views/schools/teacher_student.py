import streamlit as st 
from src.controllers.schools import list_teachers_students
import pandas as pd

st.title("Professores e Alunos por Escola")

# Converter para DataFrame

# Preencher o selectbox com os nomes das escolas
escolas_nomes = escolas_df["nome"].tolist()
escola_selecionada = st.selectbox("Selecione a escola:", escolas_nomes)

# Carregar as escolas com base no filtro
# with st.spinner("Carregando o número de alunos por nível de ensino..."):
#     escolas_df = list_teachers_students(escola_selecionada)

df = pd.DataFrame(escolas_df)

# Mostrar os resultados
if escola_selecionada:
  st.info("Selecione uma escola!")
elif escolas_df.empty:
    st.info("O número de docentes é zero!")
else:
    st.dataframe(escolas_df, use_container_width=True)