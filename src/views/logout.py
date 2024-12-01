import streamlit as st 

st.title("Sair")
st.write("Você tem certeza que deseja sair?")

if st.button("Sair"):
  st.session_state["logged_in"] = False
  st.session_state.user = None
  st.success("Logout realizado com sucesso!")
  st.rerun()