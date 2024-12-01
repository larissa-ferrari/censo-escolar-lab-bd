import streamlit as st
from controllers.user import (
    add_user,
    list_users,
)
import pandas as pd


def user_management_view():
    st.title("Gerenciamento de Usuários")

    menu = st.sidebar.selectbox("Ações", ["Criar", "Listar", "Editar", "Deletar"])

    if menu == "Criar":
        st.subheader("Criar Novo Usuário")
        username = st.text_input("Usuário")
        password = st.text_input("Senha", type="password")
        if st.button("Salvar"):
            message = add_user(username, password)
            st.success(message)

    elif menu == "Listar":
        st.subheader("Lista de Usuários")
        users = list_users()
        df = pd.DataFrame(users)

        if "password" in df.columns:
            df = df.drop(columns=["password"])

        st.dataframe(df, use_container_width=True)

    elif menu == "Editar":
        st.subheader("Editar Usuário")
        users = list_users()
        user_ids = [user["id"] for user in users]
        selected_user_id = st.selectbox("Selecione o usuário para editar", user_ids)
        
        user_to_edit = next(user for user in users if user["id"] == selected_user_id)
        username = st.text_input("Novo Usuário", value=user_to_edit["username"])
        password = st.text_input("Nova Senha", type="password")
        
        if st.button("Atualizar"):
            message = update_user(selected_user_id, username, password)
            st.success(message)

    elif menu == "Deletar":
        st.subheader("Excluir Usuário")
        users = list_users()
        user_ids = [user["id"] for user in users]
        selected_user_id = st.selectbox("Selecione o usuário para deletar", user_ids)

        if st.button("Deletar"):
            message = delete_user(selected_user_id)
            st.success(message)
