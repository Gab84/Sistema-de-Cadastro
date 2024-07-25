import flet as ft

def main(page: ft.Page):
    # Configuração da página
    page.title = "Sistema de Login e Cadastro de Clientes"
    page.window_width = 400
    page.window_height = 600
    page.theme_mode = ft.ThemeMode.LIGHT

    # Função para mostrar a tela de cadastro
    def show_register(e):
        page.controls.pop()
        page.controls.append(register_form)
        page.update()

    # Função para mostrar a tela de login
    def show_login(e):
        page.controls.pop()
        page.controls.append(login_form)
        page.update()

    # Função de login (aqui você pode adicionar lógica de autenticação)
    def login(e):
        print(f"Login: {username_input.value}, Senha: {password_input.value}")

    # Função de cadastro (aqui você pode adicionar lógica de registro)
    def register(e):
        print(f"Nome: {name_input.value}, Email: {email_input.value}, Senha: {password_register_input.value}")

    # Campos de entrada e botões do formulário de login
    username_input = ft.TextField(label="Usuário", width=300)
    password_input = ft.TextField(label="Senha", password=True, width=300)
    login_button = ft.ElevatedButton("Login", on_click=login)
    go_to_register_button = ft.TextButton("Não tem uma conta? Cadastre-se", on_click=show_register)

    # Formulário de login
    login_form = ft.Column(
        controls=[
            ft.Text("Login", size=30, weight=ft.FontWeight.BOLD),
            username_input,
            password_input,
            login_button,
            go_to_register_button
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    # Campos de entrada e botões do formulário de cadastro
    name_input = ft.TextField(label="Nome Completo", width=300)
    email_input = ft.TextField(label="Email", width=300)
    password_register_input = ft.TextField(label="Senha", password=True, width=300)
    register_button = ft.ElevatedButton("Cadastrar", on_click=register)
    go_to_login_button = ft.TextButton("Já tem uma conta? Faça login", on_click=show_login)

    # Formulário de cadastro
    register_form = ft.Column(
        controls=[
            ft.Text("Cadastro", size=30, weight=ft.FontWeight.BOLD),
            name_input,
            email_input,
            password_register_input,
            register_button,
            go_to_login_button
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    # Adicionar o formulário de login na página inicialmente
    page.controls.append(login_form)

    # Atualizar a página
    page.update()

# Executar o aplicativo
ft.app(target=main)
