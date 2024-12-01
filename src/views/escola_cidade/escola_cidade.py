import streamlit as st
from src.controllers.schools import list_schools, list_schools_by_city
import pandas as pd

st.title("Escolas da Cidade")
st.subheader("Lista de Escolas")

# Campo para o usuário digitar o código do município
codigo_municipio = st.text_input("Digite o código do município para filtrar:")

# Convertendo o código do município para consulta (apenas se preenchido)
if codigo_municipio.isdigit():
    filtro = {"CO_MUNICIPIO": int(codigo_municipio)}
else:
    filtro = {}

# Carregar as escolas com base no filtro
with st.spinner("Carregando Escolas..."):
    bookmarks = list_schools_by_city(filtro)

# Converter para DataFrame
df = pd.DataFrame(bookmarks)

# Mostrar os resultados
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