import streamlit as st
from dashboards import show_dashboard
from admin import show_admin

# Configuração da Página
st.set_page_config(page_title="Censo Escolar", layout="wide")

# Navegação
menu = st.sidebar.selectbox("Menu", ["Dashboard", "Administração"])

if menu == "Dashboard":
    show_dashboard()
elif menu == "Administração":
    show_admin()
