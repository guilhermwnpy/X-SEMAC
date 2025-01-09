"""
- Widgets Principais -
-- Scale --
Usos do widget Scale
"""


import customtkinter as ctk
import os

class ScaleActions:
    def __init__(self):
        os.system("cls")
        self.window = ctk.CTk()
        self.window.geometry("400x330")
        self.window.title("Checkbutton Actions")

        frame3 = ctk.CTkFrame(self.window)
        frame3.pack(side="bottom", padx=5, pady=5, expand=True, fill="both")

        frame1 = ctk.CTkFrame(self.window)
        frame1.pack(side="left", padx=5, pady=5, expand=True, fill="both")

        frame2 = ctk.CTkFrame(self.window)
        frame2.pack(side="left", padx=5, pady=5, expand=True, fill="both")

        scale_value1 = ctk.IntVar(value=0)
        ctk.CTkLabel(frame1, textvariable=scale_value1).pack()
        scale = ctk.CTkSlider(frame1, from_=0, to=100, variable=scale_value1)
        scale.pack(padx=10, pady=10)

        scale_value2 = ctk.IntVar(value=0)
        scale2_label = ctk.CTkLabel(frame2, text="Scale 0")
        scale2_label.pack()
        scale2 = ctk.CTkSlider(
            frame2, from_=0, to=100, variable=scale_value2,
            command=lambda e: scale2_label.configure(
                text=f"Scale: {scale_value2.get()}"
            )
        )
        scale2.pack(padx=10, pady=10)

        scale_value3 = ctk.IntVar(value=0)
        ctk.CTkLabel(frame3, textvariable=scale_value3).pack()
        scale3 = ctk.CTkSlider(
            frame3, from_=0, to=100, variable=scale_value3, 
            orientation="vertical"
        )
        scale3.pack()

    def run(self):
        self.window.mainloop()

app = ScaleActions()
app.run()
