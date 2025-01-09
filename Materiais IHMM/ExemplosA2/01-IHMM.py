import customtkinter as ctk
import threading
import queue
import serial
import serial.tools.list_ports as serial_ports

class Exemplo1:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.geometry("600x400")
        self.window.title("Exemplo 1")
        self.window.resizable(0,0)
        
        self.COM = None
        self.baud = 19200

        self.procurar_com()
        self.ser = None
        self.leitura_thread = threading.Thread(target=self.ler_serial)
        self.queue = queue.Queue()


        def show_readings(self):    
            self.temp = ctk.StringVar()
            ctk.CTkEntry(self.window, textvariable=self.temp).place(relx=0.2, rely=0.2, anchor='c')
            
            self.umidade = ctk.StringVar()
            ctk.CTkEntry(self.window, textvariable=self.umidade).place(relx=0.5, rely=0.2, anchor='c')

            self.corrente = ctk.StringVar()
            ctk.CTkEntry(self.window, textvariable=self.corrente).place(relx=0.8, rely=0.2, anchor='c')

    def procurar_com(self):
        dispositivos = ["Selecionar"]

        ports = list(serial_ports.comports())
        for port, desc, _ in ports:
            dispositivos.append(port + "-" + desc)
        
        def optionmenu_callback(choice:str):
            self.COM = choice.split("-")[0]
            self.ser = serial.Serial(self.COM, self.baud, timeout=3)
            
            if not self.leitura_thread.is_alive():
                self.leitura_thread.start()

        option_var = ctk.StringVar(value="Selecionar")
        option = ctk.CTkOptionMenu(
            self.window, values=dispositivos, 
            command=optionmenu_callback, variable=option_var
        )
        option.pack(pady=20)

    def ler_serial(self):
        while True:
            if self.ser and self.ser.is_open:
                try:
                    dado = self.ser.readline().decode().strip()
                    dado = dado.split()("_")
                    self.queue.put(dado)
                    self.window.after(10, self.atualizar_dados)
                except serial.SerialException:
                    break
    
    def atualizar_dados(self):
        while not self.queue.empty():
            dado = self.queue.get()
            valores = dado
            if len(valores) >= 4:
                V1 = float()
                self.temp.set(f"{V1}ºC")
                V2 = float()
                self.temp.set(f"{V2}")
                V3 = float()
                self.temp.set(f"{V3}")
                V4 = float()
                self.temp.set(f"{V4}")
        
    def run(self):
        self.window.mainloop()

app = Exemplo1()
app.run()
