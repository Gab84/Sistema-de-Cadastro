import customtkinter as ctk
from tkinter import StringVar

# Inicializar a aplicação CTk
ctk.set_appearance_mode("dark")  # "System" (default), "Dark", "Light"
ctk.set_default_color_theme("blue")  # "blue" (default), "green", "dark-blue"

# Criar a janela principal
root = ctk.CTk()

# Definir o título da janela
root.title("Exemplo de textvariable no CTk")

# Definir tamanho da janela
root.geometry("400x300")

# Criar uma StringVar para armazenar o texto do campo de entrada
text_var = StringVar()

# Função de callback para exibir o valor atual da StringVar
def on_change(*args):
    print("Valor atual:", text_var.get())

# Associar a função de callback à StringVar
text_var.trace_add("write", on_change)

# Criar um campo de entrada e associá-lo à StringVar
entry = ctk.CTkEntry(master=root, textvariable=text_var)
entry.pack(pady=20)

# Criar um botão para modificar o valor da StringVar
def set_text():
    text_var.set("Novo Texto")

button = ctk.CTkButton(master=root, text="Definir Texto", command=set_text)
button.pack(pady=20)

# Iniciar o loop principal
root.mainloop()
