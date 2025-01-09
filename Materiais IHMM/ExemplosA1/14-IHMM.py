"""
- Widgets Principais -
-- ComboBox --
Usos do widget ComboBox
"""

import customtkinter as ctk
import os

class ComboboxActions:
    def __init__(self):
        os.system("cls")
        self.window = ctk.CTk()
        self.window.geometry("400x150")
        self.window.title("Checkbutton Actions")

        option_selected = ctk.StringVar(value="Opção 1")
        option_menu = ctk.CTkOptionMenu(
            self.window, values=["Opção 1", "Opção 2", "Opção 3"], 
            variable=option_selected,
            command=lambda e: print(option_selected.get())
        )
        option_menu.pack(pady=15)

        option_selected2 = ctk.StringVar()
        option_menu2 = ctk.CTkOptionMenu(
            self.window, values=["Opção 1", "Opção 2", "Opção 3"], 
            command=lambda e: option_selected2.set(e)
        )
        option_menu2.pack()

        ctk.CTkButton(
            self.window, text="Mostrar", 
            command=lambda:print(f"---\nOp1:{option_selected.get()}\nOp2:{option_selected2.get()}\n---")
        ).pack(pady=15)

    def run(self):
        self.window.mainloop()

app = ComboboxActions()
app.run()
