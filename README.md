# Sistema-de-Cadastro
Sistema de cadastro feito em Python Utilizando o CustomTkInter


# Sistema de Cadastro e Menu de Usuário

Este repositório contém um sistema de cadastro de usuários e um menu de usuário, desenvolvidos utilizando a biblioteca `customtkinter` em Python.

## Visão Geral

O projeto consiste em duas partes principais:

1. **Cadastro de Usuários (`Cadastro_Sistema.py`)**: Interface gráfica para cadastro de novos usuários e salvamento das informações em um arquivo de texto.
2. **Menu de Usuário (`MenuUsuario.py`)**: Interface gráfica para o menu de interação com o usuário.

## Funcionalidades

### Cadastro_Sistema.py

- **Carregamento de Usuários**: Carrega os usuários salvos a partir de um arquivo de texto (`usuarios.txt`).
- **Cadastro de Usuários**: Permite o cadastro de novos usuários.
- **Salvamento de Usuários**: Salva os usuários cadastrados em um arquivo de texto.
- **Botão Personalizado**: Um botão que muda de imagem ao passar o mouse, utilizando a classe `ImageHoverButton`.

### [MenuUsuario.py](http://menuusuario.py/)

- **Menu de Usuário**: Interface gráfica personalizada para interação com o usuário.
- **Exclusividades de usuários**: Interface gráfica personalizada para cada usuário cadastrado contendo apenas as anotações do usuário em questão
- **Botão Personalizado**: Um botão que muda de imagem ao passar o mouse, semelhante ao do `Cadastro_Sistema.py`.

## Instalação

1. Clone o repositório:
    
    ```bash
    git clone <https://github.com/seu-usuario/sistema-cadastro-menu-usuario.git>
    
    ```
    
2. Navegue até o diretório do projeto:
    
    ```bash
    cd sistema-cadastro-menu-usuario
    
    ```
    
3. Instale as dependências:
    
    ```bash
    pip install -r requirements.txt
    
    ```
    

## Uso

Execute o Cadastro_Sistema.py crie um novo usuário e após isso faça o seu login.

Para executar o sistema de cadastro de usuários:

```bash
python Cadastro_Sistema.py

```

## Contribuição

1. Faça um fork do projeto.
2. Crie uma branch para a sua feature (`git checkout -b feature/fooBar`).
3. Commit suas alterações (`git commit -am 'Add some fooBar'`).
4. Faça o push para a branch (`git push origin feature/fooBar`).
5. Crie um novo Pull Request.
