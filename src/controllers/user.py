from models.user import get_user_by_email, check_password, create_user, get_all_users, get_user_by_id, update_user as model_update_user, delete_user

# Função para adicionar um novo usuário
def add_user(name, email, password, is_adm=False, birthday=None):
    create_user(name, email, password, is_adm, birthday)
    return f"Usuário {name} ({email}) criado com sucesso."

# Função para listar todos os usuários
def list_users():
    return get_all_users()

# Função para buscar usuário por ID
def get_user(user_id):
    return get_user_by_id(user_id)

# Função para atualizar um usuário
def update_user(user_id, name, email, password=None, is_adm=False, birthday=None):
    model_update_user(user_id, name, email, password, is_adm, birthday)
    return f"Usuário {user_id} atualizado com sucesso."

# Função para excluir um usuário
def delete_user(user_id):
    delete_user(user_id)
    return f"Usuário {user_id} excluído com sucesso."

# Lógica para autenticar o usuário
def authenticate_user(email, password):
    user = get_user_by_email(email)
    if user and check_password(password, user["senha"]):
        return user["id"]
    return False

def create_super_user(name, email, password):
    create_user(name, email, password, is_adm=True)
    return f"Super usuário {name} criado com sucesso."