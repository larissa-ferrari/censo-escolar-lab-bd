from src.models.schools import get_all_schools, get_school_by_city

# Função para listar todas as cidades
def list_schools(filters=None):
    return get_all_schools(filters)

# Função para listar escola por cidade
def list_schools_by_city(city):
    return get_school_by_city(city)