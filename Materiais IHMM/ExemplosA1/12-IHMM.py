"""
- Widgets Principais -
-- CheckButton --
Usos do widget CheckButton
"""

import customtkinter as ctk
import os

class CheckActions:
    def __init__(self):
        os.system("cls")
        self.window = ctk.CTk()
        self.window.geometry("400x100")
        self.window.title("Checkbutton Actions")

        def check_func():
            print(f"---\nC1:{c1_var.get()}\nC2:{c2_var.get()}\n---")

        c1_var = ctk.BooleanVar()
        check1 = ctk.CTkCheckBox(
            self.window, text="Opção 1",
            variable=c1_var,
            onvalue=True,
            offvalue=False,
            command=check_func
        )
        check1.pack()
        
        c2_var = ctk.IntVar()
        check2 = ctk.CTkCheckBox(
            self.window, text="Opção 2",
            variable=c2_var,
            onvalue=10,
            offvalue=5,
            command=check_func
        )
        check2.pack()

    def run(self):
        self.window.mainloop()

app = CheckActions()
app.run()