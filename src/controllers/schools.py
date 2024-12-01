from src.models.schools import get_all_schools, get_school_by_city, get_cities

# Função para listar todas as cidades
def list_schools(filters=None):
    return get_all_schools(filters)

# Função para listar escola por cidade
def list_schools():
    return get_school()