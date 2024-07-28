from customtkinter import *

from PIL import Image, ImageTk

import os

FILENAME = "usuarios.txt"

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


class Janela:
    def __init__(self):
        self.janela = CTk()
        #self.jlogin = CTk()
        #self.jcadastro = CTk()
        carregar_user = self.carregar_usuarios()
        print(self.usuarios)

    def carregar_usuarios(self):
        self.usuarios = {}
        if os.path.exists(FILENAME):
            with open(FILENAME, "r") as file:
                for line in file:
                    self.usuario, self.senha = line.strip().split(",")
                    self.usuarios[self.usuario] = self.senha
                    
    def salvar_usuarios(self):
        with open(FILENAME, "w") as file:
            for self.nusuariox, self.password in self.usuarios.items():
                file.write(f"{self.nusuariox},{self.password}\n")

    def cadastrar_usuario(self):
        self.nusuariox = self.nusuario.get()
        if self.nusuariox in self.usuarios:
            print("Usuário já existe!")
        else:
            self.password = self.nsenha.get()
            self.usuarios[self.nusuariox] = self.password
            wind.salvar_usuarios()
            print("Usuário cadastrado com sucesso!")

    
    def home(self):
        self.janela.geometry("620x400")
        self.janela._set_appearance_mode("system")
        self.janela.resizable(False,False)
        self.janela.title("Tela Inicial")
        self.janela.iconbitmap("icons\icons8-casa-48.ico")
        self.janela.configure(fg_color="#F2F2F2",bg_color="transparent")
        
        self.frameEscolha = CTkFrame(master=self.janela,width=500,height=320,fg_color="#1A1926",corner_radius=20,)
        self.homeImage = CTkImage(light_image=Image.open("homeImage.png"),dark_image=Image.open("homeImage.png"),size=(280,300))
        self.lbHomeImage = CTkLabel(master=self.frameEscolha,image=self.homeImage,text=None)
        self.lbHomeImage.place(x=10,y=15)
        
        self.cadastroImage = "Bottoes Img\iregistroImg.png"
        self.cadastroImagehover = "Bottoes Img\hover_img\hover_cadastro.png"

        self.loginImage = "Bottoes Img\loginImg.png"
        self.loginImagehover = "Bottoes Img\hover_img\hover_login.png"
        
        
        self.voltImage = "Bottoes Img\homeImg.png"
        self.voltImagehove = "Bottoes Img\hover_img\hover_home.png"
        
        self.apllyImg = "Bottoes Img\continuaImg.png"
        self.apllyImghover = "Bottoes Img\hover_img\hover_avanca.png"

        ImageHoverButton(master=self.frameEscolha,
                         image_path=self.loginImage,
                         hover_image_path=self.loginImagehover,
                         command=self.login).place(x=320,y=90)
        
        ImageHoverButton(master=self.frameEscolha,
                         image_path=self.cadastroImage,
                         hover_image_path=self.cadastroImagehover,
                         command=self.cadastro).place(x=320,y=170)
        
        self.animlogin = 700
        self.animcadastro = 700
        self.animEscolha = 60
        
        self.frameLogin = CTkFrame(master=self.janela,width=500,height=320,fg_color="#1A1926",corner_radius=20,)
        self.frameCadastro = CTkFrame(master=self.janela,width=500,height=320,fg_color="#1A1926",corner_radius=20,)
        
        self.frameEscolha.place(x=self.animEscolha,y=40)
        self.frameLogin.place(x=self.animlogin,y=100)
        self.frameCadastro.place(x=self.animcadastro,y=100)
        
        
        
        self.janela.mainloop()
    
    
    def volthome(self):
        
        if self.animlogin < 699:
            self.animlogin +=20
        
        if  self.animcadastro < 699:
            self.animcadastro += 20
        
        if self.animEscolha < 60:
            self.animEscolha += 20.6
            
        if self.animEscolha > 60:
            self.animEscolha = 60
        
        
        if self.animlogin < 699:
            
            self.janela.after(10,self.volthome)
            self.frameLogin.place(x=self.animlogin,y=40)
            self.frameEscolha.place(x=self.animEscolha,y=40)
            self.frameLogin.lift()
            
        if  self.animcadastro < 699:
            
            self.janela.after(10,self.volthome)
            self.frameCadastro.place(x=self.animcadastro,y=40)
            self.frameEscolha.place(x=self.animEscolha,y=40)
            self.frameCadastro.lift()
        
        
        


    def validacao(self):
        
        usuario = self.usuario.get()
        senha = self.senha.get()
        
        validado1 = False
        validado2 = False
         
        if usuario in self.usuarios:
            validado1 = True
            
        elif usuario not in self.usuarios:
            print("Usuario não cadastrado !")
            return
        
        if validado1 and self.usuarios[usuario] == senha:
            validado2 = True
            print("certo")
            self.usuario.delete(0,END)
            self.senha.delete(0,END)
        else:
            print("usuário ou senha incorretos")
            self.senha.delete(0,END)
        
        
    def login(self):
        
        loginCanvalado = CTkImage(light_image=Image.open("icons\salvas.png"),dark_image=Image.open("icons\salvas.png"),size=(30,320))
        lbLogCanvalado = CTkLabel(master=self.frameLogin,
                                    image=loginCanvalado,
                                    text=None,
                                    bg_color="#F2F2F2",fg_color="transparent")
        
        lbLogCanvalado.place(x=226,y=0) 
        
        
        self.animlogin -=20
        self.animEscolha -=20

        
        if self.animlogin > 59:
            lbLogCanvalado.lift()
            self.janela.after(10,self.login)
            self.frameLogin.place(x=self.animlogin,y=40)
            self.frameEscolha.place(x=self.animEscolha,y=40)
            self.frameLogin.lift()
            print(self.animlogin)

        if self.animlogin == 660:
        
        

            
        
             
            self.loginCanva = CTkImage(light_image=Image.open("loginimg.png"),dark_image=Image.open("loginimg.png"),size=(120,120))
            self.lbLogCanva = CTkLabel(master=self.frameLogin,
                                       image=self.loginCanva,
                                       text=None,
                                       bg_color="#1A1926",fg_color="transparent")
            self.lbLogCanva.place(x=320,y=55)
        
        
        
            
            self.loginCanvalado = CTkImage(light_image=Image.open("icons\imgfundo_login2.png"),dark_image=Image.open("icons\imgfundo_login2.png"),size=(250,320))
            self.lbLogCanvalado = CTkLabel(master=self.frameLogin,
                                       image=self.loginCanvalado,
                                       text=None,
                                       bg_color="#F2F2F2",fg_color="transparent")
            
            self.lbLogCanvalado.place(x=0,y=0)
            

            
            
            ImageHoverButton(master=self.frameLogin,
                             image_path=self.voltImage,
                             hover_image_path=self.voltImagehove,
                             command=self.volthome).place(x=395,y=5)
            
            self.usuario = CTkEntry(master=self.frameLogin,width=200,placeholder_text="Usuario",border_color="#1A1926",corner_radius=20)
            self.usuario.place(x=280,y=185)
            
            self.senha = CTkEntry(master=self.frameLogin,width=200,placeholder_text="Senha",border_color="#1A1926",corner_radius=20)
            self.senha.place(x=280,y=215)
            
            

            ImageHoverButton(master=self.frameLogin,
                             image_path=self.apllyImg,
                             hover_image_path=self.apllyImghover,
                             command=self.validacao,
                             ).place(x=320,y=250)
        
        
        
    def cadastro(self):
        self.animcadastro -=20
        self.animEscolha -=20

        
        if self.animcadastro > 59:
            
            self.janela.after(10,self.cadastro)
            self.frameCadastro.place(x=self.animcadastro,y=40)
            self.frameEscolha.place(x=self.animEscolha,y=40)
            self.frameCadastro.lift()
            
        if self.animcadastro ==660:
            
            self.loginCanva = CTkImage(light_image=Image.open("loginimg.png"),dark_image=Image.open("loginimg.png"),size=(120,120))
            self.lbLogCanva = CTkLabel(master=self.frameCadastro,
                                       image=self.loginCanva,
                                       text=None,
                                       bg_color="#1A1926",fg_color="transparent")
            self.lbLogCanva.place(x=183,y=55)
            CTkLabel(master=self.frameCadastro,text="BEM VINDO A TELA DE CADASTRO",text_color="#F2F2F2",font=("Impact",20)).place(x=127,y=10)
            
            ImageHoverButton(master=self.frameCadastro,
                             image_path=self.voltImage,
                             hover_image_path=self.voltImagehove,
                             command=self.volthome).place(x=395,y=5)
            
            self.nusuario = CTkEntry(master=self.frameCadastro,width=220,placeholder_text="Usuario",border_color="#1A1926",corner_radius=20)
            self.nusuario.place(x=140,y=185)
            
            self.nsenha = CTkEntry(master=self.frameCadastro,width=220,placeholder_text="Senha",border_color="#1A1926",corner_radius=20)
            self.nsenha.place(x=140,y=215)
            
            self.lbLogCanva.lift()
        
            ImageHoverButton(master=self.frameCadastro,
                             image_path=self.apllyImg,
                             hover_image_path=self.apllyImghover,
                             command=self.cadastrar_usuario,
                             ).place(x=175,y=250)


wind = Janela()

wind.home()