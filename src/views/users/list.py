import streamlit as st
from controllers.user import list_users
import pandas as pd

st.title("Gerenciamento de Usuários")

st.subheader("Lista de Usuários")
users = list_users()
df = pd.DataFrame(users)

# Remover a coluna 'senha' caso exista
df = df.drop(columns=["senha", "data_cadastro", "data_nascimento"])

# Substituir os valores da coluna 'administrador' de 1/0 por Sim/Não
if 'administrador' in df.columns:
    df['administrador'] = df['administrador'].replace({1: 'Sim', 0: 'Não'})

# Exibir a tabela no Streamlit
st.dataframe(df, use_container_width=True)
