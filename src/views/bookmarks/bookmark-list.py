import streamlit as st
from src.controllers.bookmarks import list_bookmarks
import pandas as pd

st.title("Gerenciamento de Bookmarks")
st.subheader("Lista de Bookmarks")

# Obter os bookmarks do usuário logado
bookmarks = list_bookmarks({
    "id_usuario": st.session_state.user.get("id")
})

df = pd.DataFrame(bookmarks)

if df.empty:
    st.info("Nenhum Bookmark Encontrado!")
else:
    df = df.rename(columns={
        "escola_nome": "Nome da Escola"
    })

    df = df.drop(columns=["id", "id_usuario", "id_escola"])

    df = df.reset_index(drop=True)

    st.dataframe(df, use_container_width=True)