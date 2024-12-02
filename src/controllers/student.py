from src.models.student import get_number_students_by_level

# Função para buscar o número de alunos por nível de ensino
def list_number_students_by_level():
    df = get_number_students_by_level()    
    return df

