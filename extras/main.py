from customtkinter import *

janela = CTk() #criadno a janela

#Configurando janela
janela.title("Primeira Janela") #definir nome da janela

janela.geometry("500x500") #Proporção inicial da janela

#AULA SOBRE ENTRY

entry = CTkEntry(master=janela,
                 width=200,
                 placeholder_text="Digite o seu nome",
                 )




entry.pack()


def pegar():
    x = entry.get()
    entry.delete(0,END)
    pass

btn = CTkButton(janela,width=200,
                text="Pegar texto",
                command=pegar)
btn.pack()


#Abrir a janela
janela.mainloop()