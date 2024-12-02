from src.models.turmas import get_class_by_school_id, get_all_classes

def list_all_classes(filters=None):
    return get_all_classes(filters)

def list_class(school_name):
    return get_class_by_school_id(school_name)