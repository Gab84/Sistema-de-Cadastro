import os

# Nome do arquivo onde os dados dos usuários serão salvos
FILENAME = "usuarios.txt"

# Função para carregar os usuários do arquivo
def carregar_usuarios():
    usuarios = {}
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            for line in file:
                username, password = line.strip().split(",")
                usuarios[username] = password
    return usuarios

# Função para salvar os usuários no arquivo
def salvar_usuarios(usuarios):
    with open(FILENAME, "w") as file:
        for username, password in usuarios.items():
            file.write(f"{username},{password}\n")

# Função para cadastrar um novo usuário
def cadastrar_usuario(usuarios):
    username = input("Digite o nome de usuário: ")
    if username in usuarios:
        print("Usuário já existe!")
    else:
        password = input("Digite a senha: ")
        usuarios[username] = password
        salvar_usuarios(usuarios)
        with open(f"anotacoes\{username}_anotacoes.txt", "w") as file:
            file.write("")  # Cria um arquivo de anotações vazio para o usuário
        print("Usuário cadastrado com sucesso!")

# Função para realizar o login de um usuário
def login_usuario(usuarios):
    username = input("Digite o nome de usuário: ")
    if username not in usuarios:
        print("Usuário não encontrado!")
    else:
        password = input("Digite a senha: ")
        if usuarios[username] == password:
            print("Login bem-sucedido!")
            menu_anotacoes(username)
        else:
            print("Senha incorreta!")

# Função para visualizar as anotações de um usuário
def visualizar_anotacoes(username):
    try:
        with open(f"anotacoes\{username}_anotacoes.txt", "r") as file:
            anotacoes = file.read()
            print("\nSuas anotações:")
            print(anotacoes if anotacoes else "Nenhuma anotação encontrada.")
    except FileNotFoundError:
        print("Arquivo de anotações não encontrado!")

# Função para adicionar uma nova anotação
def adicionar_anotacao(username):
    anotacao = input("Digite sua anotação: ")
    with open(f"anotacoes\{username}_anotacoes.txt", "a") as file:
        file.write(anotacao + "\n")
    print("Anotação adicionada com sucesso!")

# Menu para as anotações do usuário
def menu_anotacoes(username):
    while True:
        print("\nMenu de Anotações")
        print("1. Visualizar Anotações")
        print("2. Adicionar Anotação")
        print("3. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            visualizar_anotacoes(username)
        elif escolha == "2":
            adicionar_anotacao(username)
        elif escolha == "3":
            break
        else:
            print("Opção inválida! Tente novamente.")

# Função principal
def main():
    usuarios = carregar_usuarios()
    print(usuarios)
    
    while True:
        print("\nSistema de Login")
        print("1. Cadastrar")
        print("2. Login")
        print("3. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            cadastrar_usuario(usuarios)
        elif escolha == "2":
            login_usuario(usuarios)
        elif escolha == "3":
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
