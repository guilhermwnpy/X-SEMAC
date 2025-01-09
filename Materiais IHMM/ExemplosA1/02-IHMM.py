"""
- Hello World -
Hello World usando CustomTkinter
"""

import customtkinter as ctk

window = ctk.CTk()

def hello():
    print("Hello Wolrd")

button = ctk.CTkButton(window, text="Hello World", command=hello)
button.pack()

print(button._text)

window.mainloop()