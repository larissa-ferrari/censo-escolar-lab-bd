import streamlit as st
from src.controllers.bookmarks import list_bookmarks
import pandas as pd

st.title("Gerenciamento de Bookmarks")

st.subheader("Lista de Bookmarks")

users = list_bookmarks({
    "id_usuario": st.session_state.user.get("id")
})

df = pd.DataFrame(users)

if df.empty:
    st.info("Nenhum Bookmark Encontrado!")
else:
    st.dataframe(df, use_container_width=True)
