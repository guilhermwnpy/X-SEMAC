"""
- Introdução a Classes -
-- Demonstração AmpOp em OOP CustomTkinter--
Inteface da "Calculadora Amplificador Operacional"
usando CustomTkinter e em formato Orientado a Objetos com 
definição de classe
"""

import os
import customtkinter as ctk


class AmplificadorOpCalculadora:
    def __init__(self, master:ctk.CTk):
        # Configuração inicial do CustomTkinter
        ctk.set_appearance_mode("System")  # Pode ser "Light" ou "Dark"
        ctk.set_default_color_theme("blue")  # Tema de cores padrão

        # Limpa o terminal ao iniciar o programa
        os.system("cls")

        # Configuração da janela principal
        self.master = master
        self.master.title("Calculadora Amplificador Operacional")
        self.master.geometry("600x250")
        self.master.resizable(0, 0)

        # Configuração de layout da janela principal
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=3)
        self.master.rowconfigure(1, weight=1)

        # Variáveis
        self.r1 = ctk.DoubleVar(value=1)
        self.r1_unit = ctk.StringVar(value="ohm")
        self.r2 = ctk.DoubleVar(value=0)
        self.r2_unit = ctk.StringVar(value="ohm")
        self.ganho = ctk.DoubleVar()

        # Criação dos frames e widgets
        self._criar_frame_superior()
        self._criar_frame_inferior()

    def _criar_frame_superior(self):
        """
        Cria o frame superior, que contém os campos de entrada e o botão de cálculo.
        """
        up = ctk.CTkFrame(self.master)
        up.grid(column=0, row=0, sticky="nsew", padx=20)

        up.columnconfigure((0, 1), weight=1)
        up.rowconfigure((0, 1), weight=1)

        # Sub-frame superior esquerdo (dados do resistor 1)
        up_left = ctk.CTkFrame(up)
        up_left.grid(column=0, row=0, sticky="nsew")

        ctk.CTkLabel(up_left, text="Valor do resistor 1").pack()
        ctk.CTkEntry(up_left, textvariable=self.r1).pack()
        ctk.CTkLabel(up_left, text="Unidade do resistor 1").pack()
        ctk.CTkOptionMenu(up_left, values=["ohm", "kohm"], variable=self.r1_unit).pack()

        # Sub-frame superior direito (dados do resistor 2)
        up_right = ctk.CTkFrame(up)
        up_right.grid(column=1, row=0, sticky="nsew")

        ctk.CTkLabel(up_right, text="Valor do resistor 2").pack()
        ctk.CTkEntry(up_right, textvariable=self.r2).pack()
        ctk.CTkLabel(up_right, text="Unidade do resistor 2").pack()
        ctk.CTkOptionMenu(up_right, values=["ohm", "kohm"], variable=self.r2_unit).pack()

        # Sub-frame inferior (botão de cálculo)
        up_bottom = ctk.CTkFrame(up)
        up_bottom.grid(column=0, row=1, columnspan=2, sticky="nsew")

        ctk.CTkButton(
            up_bottom,
            text="CALCULAR",
            command=self._executar_calculo
        ).pack(expand=True, fill="both")

    def _criar_frame_inferior(self):
        """
        Cria o frame inferior, que exibe os resultados.
        """
        bottom = ctk.CTkFrame(self.master)
        bottom.grid(column=0, row=1, sticky="nsew", padx=20)

        bottom.columnconfigure((0, 1, 2), weight=1)

        # Títulos
        ctk.CTkLabel(bottom, text="R1").grid(row=0, column=0, sticky="n")
        ctk.CTkLabel(bottom, text="R2").grid(row=0, column=1, sticky="n")
        ctk.CTkLabel(bottom, text="Ganho").grid(row=0, column=2, sticky="n")

        # Valores
        self.r1_label = ctk.CTkLabel(bottom, text=self._formatar_labels(self.r1.get(), self.r1_unit.get()), font=("Arial", 16))
        self.r1_label.grid(row=1, column=0, sticky="n")

        self.r2_label = ctk.CTkLabel(bottom, text=self._formatar_labels(self.r2.get(), self.r2_unit.get()), font=("Arial", 16))
        self.r2_label.grid(row=1, column=1, sticky="n")

        ctk.CTkLabel(bottom, textvariable=self.ganho, font=("Arial", 16)).grid(row=1, column=2, sticky="n")

    def _executar_calculo(self):
        """
        Executa o cálculo e atualiza os valores exibidos na interface.
        """
        self.ganho.set(self._calcular())
        self.r1_label.configure(text=self._formatar_labels(self.r1.get(), self.r1_unit.get()))
        self.r2_label.configure(text=self._formatar_labels(self.r2.get(), self.r2_unit.get()))

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

# Criação da janela e inicialização da aplicação
root = ctk.CTk()
AmplificadorOpCalculadora(root)
root.mainloop()


	