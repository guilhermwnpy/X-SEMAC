"""
- Interface final do minicurso -
Interface simplificada da Calculadora de 
ganho do amplificador operacional não inversor
"""

import customtkinter as ctk

class AmpopCalc:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.title("Calculadora AmpOp")
        self.window.geometry("400x350")
        self.window.resizable(False, False)

        self.r1 = ctk.DoubleVar()
        self.r2 = ctk.DoubleVar()
        self.ganho = ctk.StringVar()

        self._frame_superior()
        self._frame_inferior()

    def _frame_superior(self):
        frame = ctk.CTkFrame(self.window, height=80)
        frame.pack(
            side="top", expand=True, fill="both", 
            pady=10, padx=10
        )

        ctk.CTkLabel(frame, text="Resistência R1:").pack(
            anchor="w", padx=10, pady=5
        )

        r1 = ctk.CTkEntry(frame, textvariable=self.r1)
        r1.pack(fill="x", padx=10, pady=5)

        ctk.CTkLabel(frame, text="Resistência R2:").pack(
            anchor="w", padx=10, pady=5
        )
        r2 = ctk.CTkEntry(frame, textvariable=self.r2)
        r2.pack(fill="x", padx=10, pady=5)

        def escrever_ganho():
            try:
                ganho = 1 + (self.r2.get() / self.r1.get())  # Exemplo de cálculo
                self.ganho.set(f"Ganho: {ganho:.2f}")
            except ZeroDivisionError:
                self.ganho.set("Erro: Divisão por zero")
            except Exception as e:
                self.ganho.set(f"Erro: {e}")

        ctk.CTkButton(
            frame, text="Calcular Ganho", 
            command=escrever_ganho
        ).pack(pady=10)

    def _frame_inferior(self):
        frame = ctk.CTkFrame(self.window, height=100)
        frame.pack(side="bottom", fill="both", pady=10, padx=10)

        ctk.CTkLabel(
            frame, text="Resultado do Ganho:", 
            font=("Arial", 14)
        ).pack(pady=10)

        ctk.CTkLabel(
            frame, textvariable=self.ganho, 
            font=("Arial", 16, "bold")
        ).pack(pady=5)

    def run(self):
        self.window.mainloop()

app = AmpopCalc()
app.run()
