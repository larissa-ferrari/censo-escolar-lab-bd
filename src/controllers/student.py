from src.models.student import get_number_students_by_level, get_students

# Função para buscar o número de alunos por nível de ensino
def list_number_students_by_level():
    df = get_number_students_by_level()    
    return df

def list_students():
    return get_students();
