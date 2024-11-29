import streamlit as st
from database import get_users, insert_user, delete_user


def show_admin():
    st.title("Área Administrativa")
    st.markdown("### Gerenciamento de Usuários")

    # Formulário para adicionar usuário
    with st.form("add_user_form"):
        username = st.text_input("Nome do Usuário")
        password = st.text_input("Senha", type="password")
        submitted = st.form_submit_button("Adicionar Usuário")
        if submitted and username and password:
            insert_user(username, password)
            st.success("Usuário adicionado com sucesso!")

    # Listar usuários
    st.markdown("### Usuários Cadastrados")
    users = get_users()
    for user in users:
        st.write(f"Usuário: {user['username']}")
