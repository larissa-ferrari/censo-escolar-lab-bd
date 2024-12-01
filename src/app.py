import streamlit as st
from views.login import login_view, logout_view
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
    pages = {
        "Dashboard": [
            st.Page("views/dashboards.py", title="Dashboard", icon=":material/dashboard:", default=True),
        ],
        "Usuários": [
            st.Page("views/users/list.py", title="Listagem", icon=":material/group:"),
            st.Page("views/users/create.py", title="Cadastro", icon=":material/person_add:"),
            st.Page("views/users/update.py", title="Alteração", icon=":material/person_edit:"),
        ],
        "Bookmarks": [
            # st.Page("usuarios/cadastro_usuario.py", title="Cadastro Usuário", icon=":material/person_add:"),
            # st.Page("usuarios/alteracao_usuario.py", title="Alteração Usuário", icon=":material/person_edit:")
        ],
        "Escolas": [
            # st.Page("views/users/list.py", title="Usuários", icon=":material/group:"),
            # st.Page("usuarios/cadastro_usuario.py", title="Cadastro Usuário", icon=":material/person_add:"),
            # st.Page("usuarios/alteracao_usuario.py", title="Alteração Usuário", icon=":material/person_edit:")
        ],
        "Perfil": [ st.Page("views/logout.py", title="Sair", icon=":material/logout:") ]
        # "Escolas": [
        #     st.Page("escolas/alunos_professores_por_escola.py", title="Alunos e Professores", icon=":material/dashboard:"),
        #     st.Page("escolas/escolas_por_numero_de_alunos.py", title="Ordenar por Número de Alunos", icon=":material/dashboard:"),
        #     st.Page("escolas/turmas_por_escola.py", title="Turmas", icon=":material/dashboard:"),
        #     st.Page("escolas/professores_e_alunos_por_escola.py", title="Professores e Alunos", icon=":material/dashboard:"),
        #     st.Page("escolas/alunos_por_nivel_de_ensino.py", title="Alunos por Nível", icon=":material/dashboard:"),
        # ]
    }



    # Navegação com ícones e páginas
    pg = st.navigation(pages)
    pg.run()