import streamlit as st
from controllers.user import authenticate_user

# Tela de login


def login_view():
    st.title("Login")

    username = st.text_input("Usuário")
    password = st.text_input("Senha", type="password")
    login_button = st.button("Entrar")

    if login_button:
        if authenticate_user(username, password):
            st.success("Login realizado com sucesso!")
            st.session_state["logged_in"] = True
            st.rerun()
        else:
            st.error("Usuário ou senha inválidos.")

# Tela de logout


def logout_view():
    if st.sidebar.button("Sair"):
        st.session_state["logged_in"] = False
        st.rerun()
