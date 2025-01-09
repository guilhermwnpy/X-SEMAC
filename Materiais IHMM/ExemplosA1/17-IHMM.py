import customtkinter as ctk

class Exemplo:
    def __init__(self, window: ctk.CTk):
        self.window = window
        
        button = ctk.CTkButton(master=self.window)
        button.pack(expand=True)

        self.frame = ctk.CTkFrame(master=self.window, fg_color="red")
        self.frame.pack(expand=False, fill="both")


app = ctk.CTk()
Exemplo(app)
app.mainloop()