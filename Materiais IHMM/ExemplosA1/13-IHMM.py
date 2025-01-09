"""
- Widgets Principais -
-- RadioButton --
Usos do widget RadioButton
"""

import customtkinter as ctk
import os

class RadioActions:
    def __init__(self):
        os.system("cls")
        self.window = ctk.CTk()
        self.window.geometry("400x150")
        self.window.title("Checkbutton Actions")

        def radio_func():
            print(f"---\nGrupo 1:{g1_selected.get()}\nGrupo 2:{g2_selected.get()}\n---")

        # Frame para o Grupo 1
        frame_g1 = ctk.CTkFrame(self.window)
        frame_g1.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        # Grupo 1
        g1_selected = ctk.StringVar()
        ctk.CTkLabel(frame_g1, text="Grupo 1").pack(pady=5)
        ctk.CTkRadioButton(
            frame_g1, text="Opção 1", value=1,
            variable=g1_selected, command=radio_func
        ).pack()
        ctk.CTkRadioButton(
            frame_g1, text="Opção 2", value=2,
            variable=g1_selected, command=radio_func
        ).pack(pady=10)

        # Frame para o Grupo 2
        frame_g2 = ctk.CTkFrame(self.window)
        frame_g2.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        # Grupo 2
        g2_selected = ctk.StringVar()
        ctk.CTkLabel(frame_g2, text="Grupo 2").pack(pady=5)
        ctk.CTkRadioButton(
            frame_g2, text="Opção 1", value=3, 
            variable=g2_selected, command=radio_func
        ).pack()
        ctk.CTkRadioButton(
            frame_g2, text="Opção 2", value=4, 
            variable=g2_selected, command=radio_func
        ).pack(pady=10)

    def run(self):
        self.window.mainloop()

app = RadioActions()
app.run()
