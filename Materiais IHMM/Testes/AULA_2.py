import tkinter as tk
import customtkinter as ctk
from tkinter import *
from PIL import Image, ImageTk
import serial
import threading
import queue
import serial.tools.list_ports


global diretorio
diretorio = []

janela = ctk.CTk()
global tema_V
tema_V = 1
global tema
tema = "#2f2f2f"
global cond_freq_filtro
cond_freq_filtro = 0
dispositivo = [0]
baud = 115200
global COM

class Aula_2:
   
    def __init__(self):
        self.janela=janela
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        janela.geometry('700x500')
        janela.resizable(False,False)
        janela.title("Aula 2")
        self.tela_inicial()
        self.procurarCOM()
        self.ser = None
        self.leitura_thread = threading.Thread(target=self.ler_serial)
        self.queue = queue.Queue()

        janela.mainloop()

    def tela_inicial(self):
        global tema
        frame = ctk.CTkFrame(master=janela,width=200,height=500, fg_color=tema,border_color="#202123",border_width=3)
        frame.pack(side=RIGHT)

        frame1 = ctk.CTkFrame(master=janela,width=500,height=180, fg_color=tema,border_color="#202123",border_width=3)
        frame1.place(x = 0, y= 0)

        frame2 = ctk.CTkFrame(master=janela,width=500,height=200, fg_color=tema,border_color="#202123",border_width=3)
        frame2.place(x = 0, y= 180)

        frame3 = ctk.CTkFrame(master=janela,width=500,height=120, fg_color=tema,border_color="#202123",border_width=3)
        frame3.place(x = 0, y= 380)

        self.freq = tk.StringVar()
        label_freq = ctk.CTkLabel(master=janela,text="FREQUÊNCIA DA RÁDIO",text_color="white",font=("Impact", 25), fg_color="#2f2f2f").place(x=145,y=55)
        mostrar_freq = ctk.CTkEntry(master = janela,textvariable=self.freq, width= 180, height=50, font=("Roboto",25,"bold"), justify = "center")
        mostrar_freq.place(x = 160, y= 100)

        self.temp = tk.StringVar()
        label_temp = ctk.CTkLabel(master=janela,text="TEMPERATURA",text_color="white",font=("Impact", 18), fg_color="#2f2f2f").place(x=550,y=15)
        mostrar_temp = ctk.CTkEntry(master=janela, textvariable=self.temp,font=("Robolo",15), width=120, height= 50, justify="center")
        mostrar_temp.place(x=540, y=40)

        self.umi=tk.StringVar()
        label_temp = ctk.CTkLabel(master=janela,text="UMIDADE",text_color="white",font=("Impact", 18), fg_color="#2f2f2f").place(x=565,y=105)
        mostrar_umi = ctk.CTkEntry(master=janela,textvariable=self.umi, font=("Robolo",15), width=120, height= 50, justify="center")
        mostrar_umi.place(x=540, y=130)

        self.corrente=tk.StringVar()
        label_corrente = ctk.CTkLabel(master=janela,text="CORRENTE",text_color="white",font=("Impact", 18), fg_color="#2f2f2f").place(x=560,y=195)
        mostrar_corrente = ctk.CTkEntry(master=janela,textvariable=self.corrente, font=("Robolo",15), width=120, height= 50, justify="center")
        mostrar_corrente.place(x=540, y=220)

        caixa_texto = ctk.CTkEntry(master=frame3, font=("Robolo",20), width=240, height= 50)
        caixa_texto.place(x=50, y=35)

        def enviar(caixa_texto):
            freq = caixa_texto.get()
            self.ser.write(freq.encode())
            
        bt_enviar = ctk.CTkButton(master=frame3,text="ENVIAR",command=lambda:enviar(caixa_texto))
        bt_enviar.place(x= 310, y=45)

        def enviar_on():
            self.ser.write("on_off".encode())
            
        bt_VolON = ctk.CTkButton(master=janela,text="On/Off",command=lambda:enviar_on())
        bt_VolON.place(x= 100, y=215)

        def enviar_play():
            self.ser.write("play".encode())

        bt_VolPlay = ctk.CTkButton(master=janela,text="Play/Pause",command=lambda:enviar_play())
        bt_VolPlay.place(x= 260, y=215)

        def enviar_Vmais():
            self.ser.write("V_up".encode())

        bt_VolMais = ctk.CTkButton(master=janela,text="V+",command=lambda:enviar_Vmais())
        bt_VolMais.place(x= 100, y=265)

        def enviar_Vmenos():
            self.ser.write("V_down".encode())

        bt_VolMenos = ctk.CTkButton(master=janela,text="V-",command=lambda:enviar_Vmenos())
        bt_VolMenos.place(x= 260, y=265)

        def enviar_Fmais():
            self.ser.write("F_up".encode())

        bt_FreqMais = ctk.CTkButton(master=janela,text="F+",command=lambda:enviar_Fmais())
        bt_FreqMais.place(x= 100, y=315)

        def enviar_Fmenos():
            self.ser.write("F_down".encode())

        bt_FreqMenos = ctk.CTkButton(master=janela,text="F-",command=lambda:enviar_Fmenos())
        bt_FreqMenos.place(x= 260, y=315)

        def enviar_cooler():
            self.ser.write("cooler".encode())
        bt_cooler = ctk.CTkButton(master=janela,text="COOLER",command=lambda:enviar_cooler())
        bt_cooler.place(x= 530, y=330)


    def procurarCOM(self):
        
        dispositivos = ["Selecionar dispositivo"]

        # Pega a lista de COM disponíveis
        ports = list(serial.tools.list_ports.comports())
        for port, desc, hwid in ports:
            dispositivos.append(port + " - " + desc)

        def optionmenu_callback(choice):
            global COM
            COM = choice.split(" - ")[0]


            self.ser = serial.Serial(COM, baud, timeout=3)
            dispositivo.clear()
            dispositivo.append(choice)
            if not self.leitura_thread.is_alive():
                self.leitura_thread.start()


        optionmenu_var = ctk.StringVar(value="Selecionar dispositivo")
        optionmenu = ctk.CTkOptionMenu(master=janela,values=dispositivos,
                                                command=optionmenu_callback,
                                                variable=optionmenu_var,
                                                width=150, corner_radius=1,fg_color="#ffffff",text_color="#000000")
        optionmenu.place(x=480, y=15, anchor="ne")

    def ler_serial(self):
            while True:
                if self.ser and self.ser.is_open:
                    try:
                        dado = self.ser.readline().decode().strip()
                        dado = dado.split('_')
                        self.queue.put(dado)
                        self.janela.after(10, self.atualizar_dados)
                    except serial.SerialException:
                        break


    def atualizar_dados(self):
            while not self.queue.empty():
                dado = self.queue.get()
                valores = dado
                if len(valores) >= 4:
                    V1 = float(valores[0])
                    V2 = float(valores[1])
                    V3 = float(valores[2])
                    V4 = float(valores[3])
                    M = str(V4) + " MHz"
                    
                    

                self.temp.set(str(V1) + " ºC")
                self.umi.set(str(V2) + " %")
                self.corrente.set(str(V3) + " mA")
                self.freq.set(M)


Aula_2()
