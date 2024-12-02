import streamlit as st
from src.views.login import login_view

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
            st.Page("src/views/dashboards.py", title="Dashboard",
                    icon=":material/dashboard:", default=True),
            st.Page("src/views/escola_cidade/escola_cidade.py", title="Escolas da Cidade",
                    icon=":material/dashboard:"),
            st.Page("src/views/visao_escola/visao_escola.spy", title="Visão da Escola",
                    icon=":material/dashboard:"),
            st.Page("src/views/visao_escola/visao_escola_docente.py", title="Visão da Escola (com docentes)",
                    icon=":material/dashboard:"),
            st.Page("src/views/visao_turmas/visao_turmas.py", title="Visão das Turmas",
                    icon=":material/dashboard:"),            
            st.Page("src/views/students_level/students_level.py", title="Alunos por Nível",
                icon=":material/dashboard:"),
            st.Page("src/views/schools/teacher_student.py", title="Professores e Alunos da Escola",
                icon=":material/dashboard:"),
            st.Page("src/views/ideb/ideb.py", title="Notas do Ideb",
                icon=":material/dashboard:"),
        ],
        "Usuários": [
            st.Page("src/views/users/user-list.py",
                    title="Listagem", icon=":material/group:"),
            st.Page("src/views/users/user-create.py",
                    title="Cadastro", icon=":material/person_add:"),
            st.Page("src/views/users/user-update.py",
                    title="Alteração", icon=":material/person_edit:"),
        ],
        "Bookmarks": [
            st.Page("src/views/bookmarks/bookmark-list.py",
                    title="Listagem", icon=":material/bookmark:"),
            st.Page("src/views/bookmarks/bookmark-create.py",
                    title="Cadastro", icon=":material/bookmark_add:")
        ],
        "Escolas": [
            st.Page("src/views/schools/school-list.py",
                    title="Listagem", icon=":material/school:")
        ],

        "Matrículas": [
            st.Page("src/views/student/student-list.py",
                    title="Listagem", icon=":material/school:")
        ],            
        "Turmas": [
            st.Page("src/views/turmas/turmas-list.py",
                    title="Listagem", icon=":material/school:")
        ],
        "Perfil": [
            st.Page("src/views/logout.py", title="Sair",
                    icon=":material/logout:")
        ]
    }

    if not st.session_state.user.get("administrador"):
        pages.pop("Usuários", None) 
        
    pg = st.navigation(pages)
    pg.run()
