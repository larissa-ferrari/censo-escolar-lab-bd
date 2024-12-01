import streamlit as st
from src.controllers.bookmarks import list_bookmarks, delete_bookmark
import pandas as pd

st.title("Gerenciamento de Bookmarks")
st.subheader("Lista de Bookmarks")

with st.spinner("Carregando Bookmarks..."):
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

    df = df.drop(columns=["id_usuario", "id_escola"])

    df = df.reset_index(drop=True)
   
    st.dataframe(df, use_container_width=True)

    st.divider()
    st.subheader("Remover Bookmark")

    select_bookmark = st.selectbox(
        "Selecione um usuário para alterar",
        options=df.itertuples(index=False),
        format_func=lambda u: f"{u.NO_ENTIDADE}"  
    )

    if select_bookmark:
        with st.form("remove_bookmark_form"):
            st.subheader(f"Remover Bookmark: {select_bookmark[1]} ({select_bookmark.id})")
            submitted = st.form_submit_button("Remover")

            if submitted and select_bookmark.id:
                with st.spinner(f"Removendo Bookmark..."):
                    delete_bookmark(select_bookmark.id)
                    st.success("Bookmark removido com sucesso!")
                    st.rerun()
    else:
        st.warning("Bookmark Não Encontrado!")