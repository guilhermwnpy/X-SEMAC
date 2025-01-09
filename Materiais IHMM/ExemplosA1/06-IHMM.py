"""
- Introdução a Classes -
-- Demonstração AmpOp em OOP Tkinter --
Inteface da "Calculadora Amplificador Operacional"
usando Tkinter e em formato Orientado a Objetos com 
definição de classe
"""

import os
import tkinter as tk
from tkinter import ttk

class AmplificadorOpCalculadora:
    def __init__(self, window: tk.Tk):
        # Limpa o terminal ao iniciar o programa
        os.system("cls")

        # Configuração da janela principal
        self.window = window
        self.window.title("Calculadora Amplificador Operacional")
        self.window.geometry("600x250")
        self.window.resizable(0, 0)

        # Configuração de layout da janela principal
        self.window.columnconfigure(0, weight=1)        
        self.window.rowconfigure(0, weight=3)  # Uma linha com peso 3
        self.window.rowconfigure(1, weight=1)  # Uma linha com pesos 1
        # Variáveis
        self.r1 = tk.DoubleVar(value=1)
        self.r1_unit = tk.StringVar(value="ohm")
        self.r2 = tk.DoubleVar(value=0)
        self.r2_unit = tk.StringVar(value="ohm")
        self.ganho = tk.DoubleVar()

        # Criação dos frames e widgets
        self._criar_frame_superior()
        self._criar_frame_inferior()

    def _criar_frame_superior(self):
        """
        Cria o frame superior, que contém os campos de entrada e o botão de cálculo.
        """
        up = ttk.Frame(self.window)
        up.grid(column=0, row=0, sticky="nsew", padx=20)

        up.columnconfigure((0, 1), weight=1)
        up.rowconfigure((0, 1), weight=1)

        # Sub-frame superior esquerdo (dados do resistor 1)
        up_left = ttk.Frame(up)
        up_left.grid(column=0, row=0, sticky="nsew")

        ttk.Label(up_left, text="Valor do resistor 1").pack()
        ttk.Spinbox(up_left, from_=1, to=10**6, textvariable=self.r1).pack()
        ttk.Label(up_left, text="Unidade do resistor 1").pack()
        ttk.Combobox(up_left, values=["ohm", "kohm"], textvariable=self.r1_unit).pack()

        # Sub-frame superior direito (dados do resistor 2)
        up_right = ttk.Frame(up)
        up_right.grid(column=1, row=0, sticky="nsew")

        ttk.Label(up_right, text="Valor do resistor 2").pack()
        ttk.Spinbox(up_right, from_=1, to=10**6, textvariable=self.r2).pack()
        ttk.Label(up_right, text="Unidade do resistor 2").pack()
        ttk.Combobox(up_right, values=["ohm", "kohm"], textvariable=self.r2_unit).pack()

        # Sub-frame inferior (botão de cálculo)
        up_bottom = ttk.Frame(up)
        up_bottom.grid(column=0, row=1, columnspan=2, sticky="nsew")

        ttk.Button(
            up_bottom,
            text="CALCULAR",
            command=self._executar_calculo
        ).pack(expand=True, fill="both")

    def _criar_frame_inferior(self):
        """
        Cria o frame inferior, que exibe os resultados.
        """
        bottom = ttk.Frame(self.window)
        bottom.grid(column=0, row=1, sticky="nsew", padx=20)

        bottom.columnconfigure((0, 1, 2), weight=1)

        # Títulos
        ttk.Label(bottom, text="R1").grid(row=0, column=0, sticky="n")
        ttk.Label(bottom, text="R2").grid(row=0, column=1, sticky="n")
        ttk.Label(bottom, text="Ganho").grid(row=0, column=2, sticky="n")

        # Valores
        self.r1_label = ttk.Label(bottom, text=self._formatar_labels(self.r1.get(), self.r1_unit.get()), font=("Arial", 16))
        self.r1_label.grid(row=1, column=0, sticky="n")

        self.r2_label = ttk.Label(bottom, text=self._formatar_labels(self.r2.get(), self.r2_unit.get()), font=("Arial", 16))
        self.r2_label.grid(row=1, column=1, sticky="n")

        ttk.Label(bottom, textvariable=self.ganho, font=("Arial", 16)).grid(row=1, column=2, sticky="n")

    def _executar_calculo(self):
        """
        Executa o cálculo e atualiza os valores exibidos na interface.
        """
        self.ganho.set(self._calcular())
        self.r1_label.config(text=self._formatar_labels(self.r1.get(), self.r1_unit.get()))
        self.r2_label.config(text=self._formatar_labels(self.r2.get(), self.r2_unit.get()))

    def _calcular(self) -> float:
        """
        Calcula o ganho do amplificador operacional.
        """
        r1_value = self.r1.get() * (1000 if self.r1_unit.get() == "kohm" else 1)
        r2_value = self.r2.get() * (1000 if self.r2_unit.get() == "kohm" else 1)
        return round(-(r2_value / r1_value), 3)

    def _formatar_labels(self, valor: float, unidade: str) -> str:
        """
        Formata os valores dos resistores com a unidade correta.
        """
        if unidade == "kohm":
            return f"{valor}ΩK"
        return f"{valor}Ω"

# Instancia e inicia o programa
app = tk.Tk()
AmplificadorOpCalculadora(app)
app.mainloop()
