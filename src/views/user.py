import streamlit as st
from controllers.user import (
    add_user,
    list_users,
    get_user,
    update_user,
    delete_user,
)
import pandas as pd


def user_management_view():
    st.title("Gerenciamento de Usuários")

    menu = st.sidebar.radio("Ações", ["Criar", "Listar", "Editar", "Excluir"])

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