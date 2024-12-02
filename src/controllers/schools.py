from src.models.schools import get_all_schools, get_schools_dashboard, get_schools_qtd_dashboard, get_teachers_students

# Função para listar todas as escolas
def list_schools(filters=None):
    return get_all_schools(filters)

# Função para listar escola da cidade
def list_school_dashboard():
    return get_schools_dashboard()

# Função para listar quantidades nas escolas
def list_school_qtd_dashboard():
    return get_schools_qtd_dashboard()

# Função para listar os professores e alunos
def list_teachers_students(id_school):
    return get_teachers_students(id_school)
