import streamlit as st
from views.login import login_view, logout_view
from views.dashboards import show_dashboard
from views.admin import show_admin
from views.user import user_management_view

# Configuração da página
st.set_page_config(page_title="Censo Escolar", layout="wide")

# Gerenciar estado de login
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

# Verifica se o usuário está autenticado
if not st.session_state["logged_in"]:
    login_view()
else:
    # Menu de navegação principal
    menu = st.sidebar.selectbox("Menu", ["Dashboard", "Administração", "Users"])
    logout_view()  # Botão de logout na sidebar

    if menu == "Dashboard":
        show_dashboard()
    elif menu == "Administração":
        show_admin()
    elif menu == "Users":
        user_management_view()
