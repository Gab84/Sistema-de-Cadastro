import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk, ImageDraw

def create_gradient(width, height, colors, direction='vertical'):
    base = Image.new('RGB', (width, height), colors[0])
    top = Image.new('RGB', (width, height), colors[-1])
    
    mask = Image.new('L', (width, height))
    mask_data = []

    if direction == 'vertical':
        for y in range(height):
            mask_data.extend([int(255 * (y / height))] * width)
    elif direction == 'horizontal':
        for x in range(width):
            mask_data.extend([int(255 * (x / width))] * height)
    elif direction == 'diagonal':
        for y in range(height):
            for x in range(width):
                mask_data.append(int(255 * ((x + y) / (width + height))))

    mask.putdata(mask_data)
    
    gradient = Image.composite(base, top, mask)
    return ImageTk.PhotoImage(gradient)

# Inicializa a aplicação
app = ctk.CTk()

# Define o tamanho da janela
app.geometry("400x400")

# Cria um frame
frame = ctk.CTkFrame(app, width=300, height=300)
frame.place(relx=0.5, rely=0.5, anchor="center")

# Cria o gradiente de cor
colors = ["#FF0000", "#0000FF"]
direction = 'horizontal'  # Pode ser 'vertical', 'horizontal', ou 'diagonal'
gradient_image = create_gradient(300, 300, colors, direction)

# Cria um Canvas e insere o gradiente
canvas = tk.Canvas(frame, width=300, height=300)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, anchor="nw", image=gradient_image)

# Executa a aplicação
app.mainloop()
