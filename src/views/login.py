import streamlit as st
from src.controllers.user import authenticate_user, get_user

# Tela de login
def login_view():
    st.title("Login")

    email = st.text_input("E-mail")
    password = st.text_input("Senha", type="password")
    login_button = st.button("Entrar")

    if login_button:
        with st.spinner("Autenticando Usuário..."):
            id_user = authenticate_user(email, password)

            if not id_user:
                return st.error("Usuário ou senha inválidos.")
            
            st.success("Login realizado com sucesso!")
            st.session_state["logged_in"] = True
            st.session_state["user"] = get_user(id_user)
            st.rerun()

# Tela de logout
def logout_view():
    if st.sidebar.button("Sair"):
        st.session_state["logged_in"] = False
        st.rerun()
