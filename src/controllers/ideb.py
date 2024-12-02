from src.models.ideb import get_ideb_grades_by_school

# Função para buscar o número de alunos por nível de ensino
def list_ideb_grades_by_school():
    df = get_ideb_grades_by_school()    
    return df

