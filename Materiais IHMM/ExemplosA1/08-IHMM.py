"""
- Introdução a Classes -
-- Hello World em OOP --
Hello world criado a partir da declaração de uma classe
"""

import customtkinter as ctk

class HelloWorld:
    def __init__(self, window: ctk.CTk):

        self.window = window

        def hello():
            print("Hello World")

        ctk.CTkButton(self.window, text="my button", command=hello).pack()


app = ctk.CTk()
HelloWorld(app)
app.mainloop()
