from src.models.turmas import get_class_by_school_id

def list_class(filters=None):
    return get_class_by_school_id(filters)