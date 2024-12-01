import sys
from src.controllers.user import create_super_user

def main():
    # Solicita o nome de usuário e senha para o super usuário
    if len(sys.argv) != 4:
        print("Uso: python create_super_user.py <name> <email> <password>")
        sys.exit(1)

    name = sys.argv[1]
    email = sys.argv[2]
    password = sys.argv[3]
    
    # Cria o super usuário
    result = create_super_user(name, email, password)
    print(result)

if __name__ == "__main__":
    main()
