"""
- Widgets Principais -
-- Entry --
Usos do widget Entry
"""

import customtkinter as ctk

class EntrySenha:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.geometry("400x100")
        self.window.title("Entrada de Senha")

        entry = ctk.CTkEntry(self.window, show="*")
        entry.pack()

    def run(self):
        self.window.mainloop()

app = EntrySenha()
app.run()