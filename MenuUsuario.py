from customtkinter import *
from PIL import Image, ImageTk
import os
from datetime import datetime

#from Cadastro_Sistema import Janela

class ImageHoverButton(CTkLabel):
    def __init__(self, master, image_path, hover_image_path, command=None, **kwargs):
        super().__init__(master, text="", **kwargs)  # Define o texto como vazio
        self.command = command

        # Carregar imagens
        default_image = Image.open(image_path)
        hover_image = Image.open(hover_image_path)

        # Criar CTkImage com o tamanho original
        self.default_image = CTkImage(light_image=default_image, size=default_image.size)
        self.hover_image = CTkImage(light_image=hover_image, size=hover_image.size)

        # Configurar o label com a imagem padrão
        self.configure(image=self.default_image)
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)
        self.bind("<Button-1>", self.on_click)

    def on_enter(self, event):
        self.configure(image=self.hover_image)

    def on_leave(self, event):
        self.configure(image=self.default_image)

    def on_click(self, event):
        if self.command:
            self.command()



class MenuUser:
    def __init__(self,username):
        self.janela = CTk(fg_color="#F2F2F2")
        self.username = username

    def abrir(self):
        self.janela.geometry("1024x720")
        self.janela.resizable(False,False)
        self.janela.title("Tela Do Usuario")
        self.janela.iconbitmap("./icons/icons8-casa-48.ico")
        self.janela.configure(fg_color="#F2F2F2",bg_color="transparent")
        
        #animação
        self.animahome = 40
        
        if self.username == "nat":
            self.framehome = CTkFrame(master=self.janela,width=940,height=620,fg_color="#1A1A26",corner_radius=30)
            self.framehome.place(x=self.animahome,y=60)
            self.homeImage = CTkImage(light_image=Image.open("./images/imgnats.png"),dark_image=Image.open("./images/imgnats.png"),size=(864,223))
            self.lbHomeImage = CTkLabel(master=self.framehome,image=self.homeImage,text=None)
            self.lbHomeImage.place(x=30,y=30)
        
        else:
            self.framehome = CTkFrame(master=self.janela,width=940,height=620,fg_color="#1A1A26",corner_radius=30)
            self.framehome.place(x=self.animahome,y=60)
            self.homeImage = CTkImage(light_image=Image.open("./images/ImgInicialMenuUsuario.png"),dark_image=Image.open("./images/ImgInicialMenuUsuario.png"),size=(864,223))
            self.lbHomeImage = CTkLabel(master=self.framehome,image=self.homeImage,text=None)
            self.lbHomeImage.place(x=30,y=30)
        
        self.homeImage = CTkImage(light_image=Image.open("./images/imgpost.png"),dark_image=Image.open("./images/imgpost.png"),size=(167,177))
        self.lbHomeImage = CTkLabel(master=self.framehome,image=self.homeImage,text=None)
        self.lbHomeImage.place(x=720,y=290)
        
        
        CTkLabel(master=self.framehome,text=f'Bem vindo de volta {self.username}'.upper(),text_color="black",font=("Impact",30),fg_color="#9F91F2",bg_color="transparent").place(x=255,y=75)

        self.sairimg = "./Bottoes Img/sairbtn.png"
        self.sairimghover = "./Bottoes Img/hover_img/sairbtnhover.png"

        ImageHoverButton(master=self.framehome,
                             image_path=self.sairimg,
                             hover_image_path=self.sairimghover,
                             command=self.sair).place(x=720,y=525)
        
        self.frameanota = CTkFrame(master=self.framehome,width=645,height=315,corner_radius=30,fg_color="transparent",bg_color="transparent")
        self.frameanota.place(x=30,y=275)
        
        self.homeimagenot = CTkImage(light_image=Image.open("./images/imgfundo escolhas.png"),dark_image=Image.open("./images/imgfundo escolhas.png"),size=(645,315))
        self.lbhomeimagenot = CTkLabel(master=self.frameanota,image=self.homeimagenot,text=None)
        self.lbhomeimagenot.place(x=0,y=0)
        
        self.imgsalvarnota = "./Bottoes Img/imgsalvarnota.png"
        self.imgsalvarnotahover = "./Bottoes Img/hover_img/imgsalvarnotashover.png"
        
        ImageHoverButton(master=self.lbhomeimagenot,
                             image_path=self.imgsalvarnota,
                             hover_image_path=self.imgsalvarnotahover,
                             command=self.adicionar_anotacao,fg_color="#9F91F2").place(x=320,y=238)
        
        
        
        self.imgnotas = "./Bottoes Img/imgnotas.png"
        self.imgnotashover = "./Bottoes Img/hover_img/imgnotashover.png"
        
        ImageHoverButton(master=self.lbhomeimagenot,
                             image_path=self.imgnotas,
                             hover_image_path=self.imgnotashover,
                             command=self.visualizar_anotacoes,fg_color="#9F91F2").place(x=540,y=40)
        

        self.anotacao = CTkTextbox(master=self.lbhomeimagenot,height=170,width=225,scrollbar_button_color="blue",activate_scrollbars=True,scrollbar_button_hover_color="green",fg_color="#FFFFFF",bg_color="#FFFFFF",text_color="black")
        self.anotacao.place(x=60,y=105)


        self.anotacoes = CTkTextbox(master=self.lbhomeimagenot,height=130,width=500,text_color="white",scrollbar_button_color="blue",activate_scrollbars=True,scrollbar_button_hover_color="green",border_color="red",border_width=2,state="disabled")

        self.time_label = CTkLabel(self.framehome, text="", font=("Helvetica", 17),fg_color="#FFBB05",bg_color="#FFBB05",text_color="black",corner_radius=30,height=10,width=10)
        self.time_label.place(x=763,y=215)
        self.update_time()
        
        self.janela.mainloop()

    def update_time(self):
        # Obtém a hora atual
        current_time = datetime.now().strftime("%H:%M:%S")
        # Atualiza o texto do Label
        self.time_label.configure(text=current_time)
        # Chama essa função novamente após 1000ms (1 segundo)
        self.janela.after(1000, self.update_time)
    
    def sair(self):
        #self.adicionar_anotacao()
        self.janela.destroy()

    def visualizar_anotacoes(self):
        self.anotimg = CTkImage(light_image=Image.open("./images/imgnotas.png"),
                                dark_image=Image.open("./images/imgnotas.png"), size=(645, 315))
        self.lbanotimg = CTkLabel(master=self.frameanota, image=self.anotimg, text=None)
        self.lbanotimg.place(x=0, y=0)
        
        self.imgbtnvoltar = "./Bottoes Img/imgbtnvoltar.png"
        self.imgbtnvoltarhover = "./Bottoes Img/hover_img/imgbtnvoltarhover.png"
        
        ImageHoverButton(master=self.lbanotimg,
                        image_path=self.imgbtnvoltar,
                        hover_image_path=self.imgbtnvoltarhover,
                        command=self.abrir, fg_color="#9F91F2").place(x=540, y=60)
        
        self.anotacoes = CTkTextbox(master=self.lbanotimg, height=185, width=400, text_color="black",
                                    scrollbar_button_color="blue", activate_scrollbars=True,
                                    scrollbar_button_hover_color="green", state="disabled", 
                                    fg_color="#FFF3DC", bg_color="#FFF3DC")
        self.anotacoes.place(x=75, y=100)
        
        try:
            with open(f"./dir_anotacoes/{self.username}_anotacoes.txt", "r") as file:
                self.anotacoesuser = file.read()
                self.anotacoes.configure(state="normal")
                self.anotacoes.insert("0.0", self.anotacoesuser)
                self.anotacoes.configure(state="disabled")
                
        except FileNotFoundError:
            print("Arquivo de anotações não encontrado!")



    def adicionar_anotacao(self):
        data_hora_atual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        anotacao = self.anotacao.get("1.0", "end-1c")
        self.anotacao.delete("1.0", "end-1c")
        
        # Contar o número de anotações existentes
        if os.path.exists(f"./dir_anotacoes/{self.username}_anotacoes.txt"):
            with open(f"./dir_anotacoes/{self.username}_anotacoes.txt", "r") as file:
                linhas = file.readlines()

            # Filtrar as linhas que contêm "anotação de número" para contar o número exato de anotações
            numero_anotacao = sum(1 for linha in linhas if "anotação de número" in linha) + 1
        else:
            numero_anotacao = 1
        
        # Formatar a anotação com espaçamento e uma divisória
        anotacao_formatada = f"{data_hora_atual} - anotação de número {numero_anotacao} -- {anotacao}\n{'-'*50}\n\n"
        
        with open(f"./dir_anotacoes/{self.username}_anotacoes.txt", "a") as file:
            file.write(anotacao_formatada)
        
        print(f"Anotação de número {numero_anotacao} adicionada com sucesso!")


        

"""sim = MenuUser("adm")

sim.abrir()"""



