"""
- Hello World -
Hello World usando Tkinter 
"""

from tkinter import *
from tkinter import ttk

window = Tk()

def hello():
    print("Hello World")

ttk.Button(window, text="Hello World!", command=hello).pack()

window.mainloop()
