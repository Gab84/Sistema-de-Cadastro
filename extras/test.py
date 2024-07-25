import customtkinter as ctk
from datetime import datetime

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Relógio em Tempo Real")
        self.geometry("300x200")

        # Criação do Label para exibir a hora
        self.time_label = ctk.CTkLabel(self, text="", font=("Helvetica", 24))
        self.time_label.pack(pady=20)

        # Chama a função update_time pela primeira vez
        self.update_time()

    def update_time(self):
        # Obtém a hora atual
        current_time = datetime.now().strftime("%H:%M:%S")
        # Atualiza o texto do Label
        self.time_label.configure(text=current_time)
        # Chama essa função novamente após 1000ms (1 segundo)
        self.after(1000, self.update_time)

if __name__ == "__main__":
    app = App()
    app.mainloop()
