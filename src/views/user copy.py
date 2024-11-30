import streamlit as st
from controllers.user import (
    list_users,
    delete_user,
    update_user,
    get_user,
    add_user
)
from st_aggrid import AgGrid, GridOptionsBuilder
import pandas as pd

def user_management_view():
    st.title("Gerenciamento de Usuários")

    menu = st.sidebar.radio("Ações", ["Listar", "Criar"])

    if menu == "Listar":
        st.subheader("Lista de Usuários")

        # Obter dados dos usuários
        users = list_users()

        # Criar DataFrame excluindo a coluna 'password'
        df = pd.DataFrame(users)
        if "password" in df.columns:
            df = df.drop(columns=["password"])

        # Configuração da tabela interativa
        gb = GridOptionsBuilder.from_dataframe(df)
        gb.configure_default_column(editable=False)  # Colunas não editáveis
        gb.configure_selection(selection_mode="single", use_checkbox=True)  # Seleção de uma linha
        gb.configure_column("id", headerCheckboxSelection=True)  # Permite seleção por ID
        grid_options = gb.build()

        # Renderizar a tabela com AgGrid
        grid_response = AgGrid(
            df,
            gridOptions=grid_options,
            height=300,
            update_mode="MANUAL",
            allow_unsafe_jscode=True,
        )

        # Capturar a linha selecionada
        selected_row = grid_response["selected_rows"]

        # Exibir botões para Editar ou Excluir
        if selected_row:
            user_id = selected_row[0]["id"]
            col1, col2 = st.columns(2)

            with col1:
                if st.button("Editar Usuário"):
                    edit_user_form(user_id)

            with col2:
                if st.button("Excluir Usuário"):
                    delete_user(user_id)
                    st.success(f"Usuário {user_id} excluído com sucesso.")
                    st.rerun()  # Recarregar a página para atualizar os dados

    elif menu == "Criar":
        st.subheader("Criar Novo Usuário")
        username = st.text_input("Usuário")
        password = st.text_input("Senha", type="password")
        if st.button("Salvar"):
            add_user(username, password)
            st.success(f"Usuário {username} criado com sucesso.")

def edit_user_form(user_id):
    st.subheader(f"Editar Usuário ID: {user_id}")

    # Buscar informações do usuário atual
    user = get_user(user_id)
    if user:
        username = st.text_input("Novo Usuário", value=user["username"])
        password = st.text_input("Nova Senha", type="password")

        if st.button("Atualizar"):
            update_user(user_id, username, password)
            st.success(f"Usuário {user_id} atualizado com sucesso.")
            st.rerun()  # Recarregar a página

