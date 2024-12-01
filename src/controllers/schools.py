from src.models.schools import get_all_schools

# Função para listar todas as cidades
def list_schools(filters=None):
    return get_all_schools(filters)