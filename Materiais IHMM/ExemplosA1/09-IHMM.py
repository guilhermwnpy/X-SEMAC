"""
- Widgets Principais -
-- Label --
Usos do widget Label
"""

import customtkinter as ctk

class LabelDinamica:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.geometry("400x100")
        self.window.title("Label Dinâmica")


        entry_str = ctk.StringVar()
        entry = ctk.CTkEntry(self.window, textvariable=entry_str)
        entry.pack()

        ctk.CTkLabel(self.window, textvariable=entry_str).pack()

    def run(self):
        self.window.mainloop()

app = LabelDinamica()
app.run()