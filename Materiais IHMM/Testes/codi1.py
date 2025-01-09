import customtkinter as ctk
from tkinter import *
import serial
import threading
import queue
import serial.tools.list_ports

baud = 115200 
global COM    # usar em qualquer parte do codigo

class Exemplo:
    def __init__(self, window: ctk.CTk):
        self.window = window
        window.title("Aula 2")
        window.geometry("600x500")
        # window.resizable(False, False)

        self.ser = None    
        self.leitura_thread = threading.Thread(target=self.ler_serial)
        self.queue = queue.Queue()

        self._frame_um()
        self._frame_dois()
        self._frame_tres()
            
    def _frame_um(self):
            frame = ctk.CTkFrame(self.window,width=300,height=150)
            frame.place(x=10,y=10)

            ctk.CTkLabel(frame, text="Frequência:",font=("Robolo",20), width=120, height= 50).place(x=10,y=10)

            self.temp = ctk.StringVar()
            mostrar_temp = ctk.CTkEntry(
                master=frame,
                textvariable=self.temp,
                font=("Robolo",15),
                width=130,
                height=50,
                justify="center"
            )
            mostrar_temp.place(x=50,y=100)


    def _frame_dois(self):
        frame = ctk.CTkFrame(self.window,width=300,height=300)
        frame.place(x=10,y=170)  

    def _frame_tres(self):
        frame = ctk.CTkFrame(self.window,width=200,height=300)
        frame.place(x=320,y=10)  

        
        def procurarCOM(self):
            dispositivos = ["Selecionar dispositivo"]

            # pega a lista de COM disponíveis
            ports = list(serial.tools.list_ports.comports())
            for port, desc, hwid in ports:
                dispositivos.append(port + " - " + desc)
            
            def optionmenu_callback(choice):
                global COM
                COM = choice.split(" - ")[0]   #escolher a COM

                self.ser = serial.Serial(COM, baud, timeout=3)  #iniciar a conexao serial na COM escolhida
                # dispositivo.clear()
                # dispositivo.append(choice)
                if not self.leitura_thread.is_alive():   # testar se está ativa
                    self.leitura_thread.start()
            
            optionmenu_var = ctk.StringVar(value="Selecionar dispositivo")
            optionmenu = ctk.CTkOptionMenu(
                master=frame,
                values=dispositivos,
                command=optionmenu_callback,
                variable=optionmenu_var,
                width=150,
                corner_radius=1,
                fg_color="#e52b50",
                text_color="#faebd7",
            )
            optionmenu.place(x=700, y=200, anchor="ne")
        procurarCOM(self)
    

        # self.umi = ctk.StringVar()
        # mostrar_umi = ctk.CTkEntry(
        #     master=self.window,
        #     textvariable=self.umi,
        #     font=("Robolo",15),
        #     width=130,
        #     height=50,
        #     justify="center"
        # )
        # mostrar_umi.place(x=400,y=200)

        # self.corrente = ctk.StringVar()
        # mostrar_corrente = ctk.CTkEntry(
        #     master=self.window,
        #     textvariable=self.corrente,
        #     font=("Robolo",15),
        #     width=130,
        #     height=50,
        #     justify="center"
        # )
        # mostrar_corrente.place(x=100,y=300)

        self.uw = ctk.StringVar()
        mostrar_uw = ctk.CTkEntry(
            master=self.window,
            textvariable=self.uw,
            font=("Robolo",15),
            width=130,
            height=50,
            justify="center"
        )
        mostrar_uw.place(x=400,y=300)

        def enviar():
            self.ser.write("teste".encode())
        botao = ctk.CTkButton(master=self.window,text="ENVIAR",command=lambda:enviar())
        botao.place(x= 250, y=400)

        def enviar():
            self.ser.write("teste".encode())
        botao = ctk.CTkButton(master=self.window,text="ENVIAR",command=lambda:enviar())
        botao.place(x= 250, y=400)




    def ler_serial(self):
        while True:
            if self.ser and self.ser.is_open:
                try:
                    dado = self.ser.readline().decode().strip()
                    dado = dado.split('_')
                    self.queue.put(dado)
                    self.window.after(10, self.atualizar_dados)
                except serial.SerialException:
                    break
    
    def atualizar_dados(self):
        while not self.queue.empty():
            dado = self.queue.get()
            valores = dado
            if len(valores) >= 4:
                V1 = float(valores[0])
                V2 = float(valores[1])
                V3 = float(valores[2])*1000
                V4 = float(valores[3])
            
            self.temp.set(str(V1) + "°C")
            self.umi.set(str(V2) + "%")
            self.corrente.set(str(V3) + "mA")



app = ctk.CTk()
Exemplo(app)
app.mainloop()
