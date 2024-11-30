from models.user import get_user_by_username, check_password, create_user, get_all_users, get_user_by_id, update_user, delete_user

# Função para adicionar um novo usuário
def add_user(username, password):
    create_user(username, password)
    return f"Usuário {username} criado com sucesso."

# Função para listar todos os usuários
def list_users():
    return get_all_users()

# Função para buscar usuário por ID
def get_user(user_id):
    return get_user_by_id(user_id)

# Função para atualizar um usuário
def update_user(user_id, username, password):
    update_user(user_id, username, password)
    return f"Usuário {user_id} atualizado com sucesso."

# Função para excluir um usuário
def delete_user(user_id):
    delete_user(user_id)
    return f"Usuário {user_id} excluído com sucesso."

# Lógica para autenticar o usuário
def authenticate_user(username, password):
    user = get_user_by_username(username)
    if user and check_password(password, user["password"]):
        return True
    return False
