import streamlit as st
from controllers.user import get_all_users, create_user, delete_user


def show_admin():
    # Definindo o título da página
    st.title("Área Administrativa")
    st.markdown("### Gerenciamento de Módulos")
    
    # Verificando se o usuário está logado
    if 'logged_in' not in st.session_state or not st.session_state['logged_in']:
        st.sidebar.write("Por favor, faça login para acessar esta página.")
        return

    # Verifica se o usuário é um administrador
    current_user = st.session_state.get("user", {})
    is_admin = current_user.get('administrador', False)

    print(is_admin)

    


    # Sidebar com links de navegação
    if is_admin:  # Se for administrador
        pass
    else:  # Se for um usuário normal
        pass

    # # Formulário para adicionar usuário
    # with st.form("add_user_form"):
    #     username = st.text_input("Nome do Usuário")
    #     password = st.text_input("Senha", type="password")
    #     submitted = st.form_submit_button("Adicionar Usuário")
    #     if submitted and username and password:
    #         create_user(username, password)
    #         st.success("Usuário adicionado com sucesso!")

    # # Listar usuários
    # st.markdown("### Usuários Cadastrados")
    # users = get_all_users()
    # for user in users:
    #     st.write(f"Usuário: {user['nome']}")
