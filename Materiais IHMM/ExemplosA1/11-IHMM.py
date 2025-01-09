"""
- Widgets Principais -
-- Button --
Usos do widget Button
"""

import customtkinter as ctk
import os

class ButtonActions:
    def __init__(self):
        os.system("cls")
        self.window = ctk.CTk()
        self.window.geometry("400x100")
        self.window.title("Ações do Botão")

        bLambda = ctk.CTkButton(
            self.window, 
            text="Botão Lambda", 
            command=lambda: print("Botão com função lambda clicado!")
        )
        bLambda.pack(pady=10)

        def bfunc_callback():
            print("Botão com função definida clicado!")

        bFunc = ctk.CTkButton(
            self.window, 
            text="Botão Função", command=bfunc_callback
        )
        bFunc.pack()
        
    def run(self):
        self.window.mainloop()

app = ButtonActions()
app.run()