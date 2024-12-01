import streamlit as st
from src.controllers.bookmarks import add_bookmark
from src.controllers.schools import list_schools
from datetime import date
import pandas as pd

st.title("Gerenciamento de Bookmarks")
st.subheader("Criação de Bookmark")

schools = list_schools()

if schools:
    df = pd.DataFrame(schools)
    user_id = st.session_state.user.get("id")

    with st.form("add_bookmark_form"):
        selected_school = st.selectbox(
            "Selecione Sua Escola Favorita",
            options=df.itertuples(index=False),
            format_func=lambda u: u.NO_ENTIDADE
        )
        submitted = st.form_submit_button("Adicionar Bookmark")
        
        if submitted and selected_school and user_id:
            school_id = selected_school.CO_ENTIDADE
            try:
                with st.spinner("Adicionando Bookmark..."):
                    add_bookmark(user_id, school_id)
                    st.success("Bookmark adicionado com sucesso!")
            except ValueError as e:
                st.error(str(e)) 
            except Exception as e:
                st.error(f"Erro inesperado: {e}")  
