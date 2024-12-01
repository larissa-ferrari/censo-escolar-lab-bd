import streamlit as st
from datetime import date
from src.controllers.user import list_users, get_user, update_user
import pandas as pd

st.title("Gerenciamento de Usuários")
st.subheader("Editar Usuário")

# Seleção do usuário para alteração
users = list_users()

if users:

  df = pd.DataFrame(users)
    
  # Use 'itertuples()' para criar as opções no selectbox
  select_user = st.selectbox(
      "Selecione um usuário para alterar",
      options=df.itertuples(index=False),  # Utilizando itertuples após converter para DataFrame
      format_func=lambda u: f"{u.nome} ({u.email})"  # Supondo que 'nome' seja o nome do usuário na tupla
  )

  if select_user:
    user_id = select_user.id
    user_data = get_user(user_id)

    if user_data is not None:
      st.subheader(f"Editar Dados do Usuário: {user_data['nome']}")

      with st.form("update_user_form"):

        name = st.text_input("Nome do Usuário", value=user_data["nome"])
        email = st.text_input("E-mail do Usuário", value=user_data["email"])
        birthday = st.date_input("Data de Nascimento", min_value=date(1900, 1, 1), max_value=date.today(), value=user_data["data_nascimento"])
        is_adm = st.checkbox("Administrador?", value=bool(user_data["administrador"]))
        password = st.text_input("Senha", type="password")

        submitted = st.form_submit_button("Salvar")

        if submitted and name and email:
          update_user(user_id, name, email, password, is_adm, birthday)
          st.success("Usuário atualizado com sucesso!")

    else:
      st.warning("Usuário Não Encontrado!")

else:
  st.warning("Nenhum Usuário Encontrado!")