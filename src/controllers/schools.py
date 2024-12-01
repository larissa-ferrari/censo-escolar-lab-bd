from src.models.schools import get_all_schools, get_schools_dashboard

# Função para listar todas as cidades
def list_schools(filters=None):
    return get_all_schools(filters)

# Função para listar escola por cidade
def list_school_dashboard():
    return get_schools_dashboard()