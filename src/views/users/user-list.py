import streamlit as st
from src.controllers.user import list_users, get_user, delete_user
import pandas as pd

st.title("Gerenciamento de Usuários")
st.subheader("Lista de Usuários")

with st.spinner("Listando Usuários..."):
    users = list_users()

df = pd.DataFrame(users)

if df.empty:
    st.info("Nenhum Usuário Encontrado!")
else:
    # Remover a coluna 'senha' caso exista
    df = df.drop(columns=["senha", "data_cadastro", "data_nascimento"])

    # Substituir os valores da coluna 'administrador' de 1/0 por Sim/Não
    if 'administrador' in df.columns:
        df['administrador'] = df['administrador'].replace({1: 'Sim', 0: 'Não'})

    # Exibir a tabela no Streamlit
    st.dataframe(df, use_container_width=True)


    st.divider()
    st.subheader("Remover Usuário")

    select_user = st.selectbox(
        "Selecione um usuário para alterar",
        options=df.itertuples(index=False),
        format_func=lambda u: f"{u.nome} ({u.email})"
    )

    if select_user:
        user_id = select_user.id

        with st.spinner("Recuperando Usuário..."):
            user_data = get_user(user_id)

        if user_data is not None:

            with st.form("remove_user_form"):
                st.subheader(f"Remover Usuário: {user_data['nome']} ({user_data['email']})")
                submitted = st.form_submit_button("Remover")

                if submitted and user_data:
                    with st.spinner(f"Removendo Usuário: {user_data['nome']}..."):
                        delete_user(user_data["id"])
                        st.success("Usuário removido com sucesso!")
                        st.rerun()
        else:
            st.warning("Usuário Não Encontrado!")
