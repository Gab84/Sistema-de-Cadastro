from customtkinter import *

from PIL import Image

import os

FILENAME = "usuarios.txt"


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
        self.cadastroImage = CTkImage(light_image=Image.open("Bottoes Img\iregistroImg.png"),dark_image=Image.open("Bottoes Img\iregistroImg.png"),size=(150,55))
        self.loginImage = CTkImage(light_image=Image.open("Bottoes Img\loginImg.png"),dark_image=Image.open("Bottoes Img\loginImg.png"),size=(150,55))
        self.lbHomeImage = CTkLabel(master=self.frameEscolha,image=self.homeImage,text=None)
        self.lbHomeImage.place(x=10,y=15)
        self.voltImage = CTkImage(light_image=Image.open("Bottoes Img\homeImg.png"),dark_image=Image.open("Bottoes Img\homeImg.png"),size=(100,37))
        self.apllyImg = CTkImage(light_image=Image.open("Bottoes Img\continuaImg.png"),dark_image=Image.open("Bottoes Img\continuaImg.png"),size=(150,55))
    

        
        CTkButton(master=self.frameEscolha,
                  command=self.login,
                  text=None,
                  image=self.loginImage,
                  fg_color="transparent",
                  hover=False
                  ).place(x=320,y=90)
        
        CTkButton(master=self.frameEscolha,
                  text=None,
                  image=self.cadastroImage,
                  fg_color="transparent",
                  hover=False,
                  command=self.cadastro
                  ).place(x=320,y=170)
        
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

        self.animlogin -=20
        self.animEscolha -=20

        
        if self.animlogin > 59:
            
            self.janela.after(10,self.login)
            self.frameLogin.place(x=self.animlogin,y=40)
            self.frameEscolha.place(x=self.animEscolha,y=40)
            self.frameLogin.lift()
            print(self.animlogin)
            
        if self.animlogin == 300:
                        
            self.loginCanva = CTkImage(light_image=Image.open("loginimg.png"),dark_image=Image.open("loginimg.png"),size=(120,120))
            self.lbLogCanva = CTkLabel(master=self.frameLogin,
                                       image=self.loginCanva,
                                       text=None,
                                       bg_color="#1A1926",fg_color="transparent")
            self.lbLogCanva.place(x=183,y=55)

            CTkLabel(master=self.frameLogin,text="BEM VINDO A TELA DE LOGIN",text_color="#F2F2F2",font=("Impact",20)).place(x=137,y=10)
            CTkButton(master=self.frameLogin,
                    height=30,
                    width=30,
                    text=None,
                    fg_color="transparent",
                    hover=False,
                    command=self.volthome,
                    image=self.voltImage,
                    ).place(x=378,y=5)
            
            self.usuario = CTkEntry(master=self.frameLogin,width=200,placeholder_text="Usuario",border_color="#1A1926",corner_radius=20)
            self.usuario.place(x=142,y=185)
            
            self.senha = CTkEntry(master=self.frameLogin,width=200,placeholder_text="Senha",border_color="#1A1926",corner_radius=20)
            self.senha.place(x=142,y=215)
            
            self.lbLogCanva.lift()
        
            CTkButton(master=self.frameLogin,
                    height=30,
                    width=30,
                    text=None,
                    fg_color="transparent",
                    hover=False,
                    command=self.validacao,
                    image=self.apllyImg
                    ).place(x=157,y=250)
        
        
        
    def cadastro(self):
        self.animcadastro -=20
        self.animEscolha -=20

        
        if self.animcadastro > 59:
            
            self.janela.after(10,self.cadastro)
            self.frameCadastro.place(x=self.animcadastro,y=40)
            self.frameEscolha.place(x=self.animEscolha,y=40)
            self.frameCadastro.lift()
            
        if self.animcadastro ==300:
            
            self.loginCanva = CTkImage(light_image=Image.open("loginimg.png"),dark_image=Image.open("loginimg.png"),size=(120,120))
            self.lbLogCanva = CTkLabel(master=self.frameCadastro,
                                       image=self.loginCanva,
                                       text=None,
                                       bg_color="#1A1926",fg_color="transparent")
            self.lbLogCanva.place(x=183,y=55)
            CTkLabel(master=self.frameCadastro,text="BEM VINDO A TELA DE CADASTRO",text_color="#F2F2F2",font=("Impact",20)).place(x=127,y=10)
            CTkButton(master=self.frameCadastro,
                    height=30,
                    width=30,
                    text=None,
                    fg_color="transparent",
                    hover=False,
                    command=self.volthome,
                    image=self.voltImage,
                    ).place(x=378,y=5)
            
            self.nusuario = CTkEntry(master=self.frameCadastro,width=200,placeholder_text="Usuario",border_color="#1A1926",corner_radius=20)
            self.nusuario.place(x=142,y=185)
            
            self.nsenha = CTkEntry(master=self.frameCadastro,width=200,placeholder_text="Senha",border_color="#1A1926",corner_radius=20)
            self.nsenha.place(x=142,y=215)
            
            self.lbLogCanva.lift()
        
            CTkButton(master=self.frameCadastro,
                    height=30,
                    width=30,
                    text=None,
                    fg_color="transparent",
                    hover=False,
                    command=self.cadastrar_usuario,
                    image=self.apllyImg
                    ).place(x=157,y=250)


wind = Janela()

wind.home()