import tkinter as tk
from tkinter import font

# Cria uma janela raiz
root = tk.Tk()

# Obtém todas as fontes de texto disponíveis
available_fonts = list(font.families())

# Imprime todas as fontes disponíveis
for f in available_fonts:
    print(f)

# Fecha a janela raiz
root.destroy()


import tkinter as tk
from tkinter import font

# Cria a janela principal
root = tk.Tk()
root.title("Visualizador de Fontes")

# Obtém todas as fontes de texto disponíveis
available_fonts = list(font.families())

# Adiciona um Scrollbar para permitir a rolagem
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Cria um Canvas para os labels de fonte
canvas = tk.Canvas(root, yscrollcommand=scrollbar.set)
scrollbar.config(command=canvas.yview)

# Adiciona o Canvas à janela principal
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Cria um Frame dentro do Canvas para organizar os labels
frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor="nw")

# Adiciona um label para cada fonte disponível
for f in available_fonts:
    label = tk.Label(frame, text=f"{f}: Exemplo de texto", font=(f, 16))
    label.pack(anchor="w")

# Atualiza o Canvas para ajustar o tamanho do conteúdo
frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

# Inicia o loop principal da interface
root.mainloop()
