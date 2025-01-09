import tkinter as tk
import customtkinter as ctk
from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
# import sounddevice as sd

janela = ctk.CTk()


class Aula_1:
    freq = []
    amp = []
    amostragem = []
    offset = []
    duracao = []
    def __init__(self):
        self.janela=janela

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")
        
        janela.geometry('700x500')
        janela.resizable(False,False)
        janela.title("Aula 1")
        
        self.tela_inicial()
        janela.mainloop()
    
    def tela_inicial(self):
        frame = ctk.CTkFrame(master=janela,width=700,height=500, fg_color="#f2f2f2",border_color="black",border_width=3)
        frame.pack(side=TOP)

        ctk.CTkLabel(master=frame,text="Gerador de Sinal",font=("Impact",40,"bold"),text_color="black").place(x=200,y=60)
        
        freq = ctk.CTkEntry(master=frame, width=200,height=30, placeholder_text="Frequência(Hz)", font=("Roboto",20,"bold"),text_color="white",corner_radius=50,fg_color="#444444",border_color="black", justify="center")
        freq.place(x=110,y=130)
        
        amp = ctk.CTkEntry(master=frame, width=200,height=30, placeholder_text="Amplitude", font=("Roboto",20,"bold"),text_color="white",corner_radius=50,fg_color="#444444",border_color="black", justify="center")
        amp.place(x=110,y=180)
        
        amostragem = ctk.CTkEntry(master=frame, width=200,height=30, placeholder_text="Amostragem(Hz)", font=("Roboto",20,"bold"),text_color="white",corner_radius=50,fg_color="#444444",border_color="black", justify="center")
        amostragem.place(x=380,y=130)
        
        offset = ctk.CTkEntry(master=frame, width=200,height=30, placeholder_text="Offset", font=("Roboto",20,"bold"),text_color="white",corner_radius=50,fg_color="#444444",border_color="black", justify="center")
        offset.place(x=380,y=180)
        
        duracao = ctk.CTkEntry(master=frame, width=200,height=30, placeholder_text="Duração(s)", font=("Roboto",20,"bold"),text_color="white",corner_radius=50,fg_color="#444444",border_color="black", justify="center")
        duracao.place(x=250,y=230)

        self.exibir = tk.StringVar()
        
        ctk.CTkEntry(master=frame,textvariable=self.exibir,font=("Robolo",20,"italic"),width=300,height=50,placeholder_text_color="black", justify="center").place(x=200,y=420)

        def gerar_sinal(freq,amp,amostragem,offset,ouvir,duracao):
            ouvir = ouvir.get()
            offset = offset.get()
            duracao = duracao.get()
            amp = amp.get()
            amostragem = amostragem.get()
            freq = freq.get()

            exibir = "SIN(" + offset + " " + amp + " " + freq + ")"
            self.exibir.set(exibir)

            T = 1/int(amostragem)
            t = np.arange(0, int(duracao), T)
            x = int(amp) * np.sin(2 * np.pi * int(freq) * t) + int(offset)

            plt.plot(t, x)
            plt.xlabel('Tempo (s)')
            plt.ylabel('Amplitude')
            plt.title('Sinal Senoidal')
            plt.show()

            # if ouvir == 1:
            #     sd.play(x, int(amostragem))
            #     sd.wait()
                
       
        
        ctk.CTkButton(master=frame,width=100,height=50,text="GERAR",font=("Roboto",15),fg_color="black",command=lambda:gerar_sinal(freq,amp,amostragem,offset,ouvir,duracao)).place(x=300,y=320)
        
        ouvir = tk.IntVar()
        ctk.CTkCheckBox(master=frame,text="OUVIR",font=("Roboto",20,"bold"),variable=ouvir,text_color="black").place(x=550,y=330)

Aula_1()
