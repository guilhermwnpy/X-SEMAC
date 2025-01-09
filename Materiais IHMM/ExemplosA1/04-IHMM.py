"""
- Demonstração AmpOp -
Inteface da "Calculadora Amplificador Operacional"
usando CustomTkinter e em formato Script
"""

import os
import customtkinter as ctk

# Configura o tema do CustomTkinter
ctk.set_appearance_mode("System")  # "Dark", "Light", ou "System"
ctk.set_default_color_theme("blue")  # Tema de cor padrão

# Limpa o terminal ao iniciar o programa
os.system("cls")

# Configuração da janela principal
window = ctk.CTk()
window.title("Calculadora Amplificador Operacional")  # Título da janela
window.geometry("600x250")  # Dimensões da janela
window.resizable(0, 0)  # Desabilita redimensionamento da janela

# Configuração de layout da janela principal
window.columnconfigure(0, weight=1)  # Única coluna, preenchendo uniformemente
window.rowconfigure(0, weight=3)  # Uma linha com peso 3
window.rowconfigure(1, weight=1)  # Uma linha com peso 1

# ------------------ Frame superior (entrada de dados) ------------------
up = ctk.CTkFrame(window)
up.grid(column=0, row=0, sticky="nsew", padx=20)

# Configuração da grade do frame superior
up.columnconfigure((0, 1), weight=1)  # Duas colunas com pesos iguais
up.rowconfigure((0, 1), weight=1)  # Duas linhas com pesos iguais

# Sub-frame superior esquerdo (dados do resistor 1)
up_left = ctk.CTkFrame(up)
up_left.grid(column=0, row=0, sticky="nsew")

r1 = ctk.DoubleVar(value=1)  # Valor inicial de R1
r1_unit = ctk.StringVar(value="ohm")  # Unidade inicial de R1

# Widgets no sub-frame superior esquerdo
ctk.CTkLabel(up_left, text="Valor do resistor 1").pack()
ctk.CTkEntry(up_left, textvariable=r1).pack()  # Entrada para valor de R1
ctk.CTkLabel(up_left, text="Unidade do resistor 1").pack()
ctk.CTkOptionMenu(up_left, values=["ohm", "kohm"], variable=r1_unit).pack()

# Sub-frame superior direito (dados do resistor 2)
up_right = ctk.CTkFrame(up)
up_right.grid(column=1, row=0, sticky="nsew")

r2 = ctk.DoubleVar(value=0)  # Valor inicial de R2
r2_unit = ctk.StringVar(value="ohm")  # Unidade inicial de R2

# Widgets no sub-frame superior direito
ctk.CTkLabel(up_right, text="Valor do resistor 2").pack()
ctk.CTkEntry(up_right, textvariable=r2).pack()  # Entrada para valor de R2
ctk.CTkLabel(up_right, text="Unidade do resistor 2").pack()
ctk.CTkOptionMenu(up_right, values=["ohm", "kohm"], variable=r2_unit).pack()

# Sub-frame inferior do frame superior (botão de cálculo)
up_bottom = ctk.CTkFrame(up)
up_bottom.grid(column=0, row=1, columnspan=2, sticky="nsew")

# ------------------ Funções de cálculo e formatação ------------------
def calcular(resistor1: float, resistor2: float, resistor1_unit: str, resistor2_unit: str) -> float:
    """
    Calcula o ganho do amplificador operacional.
    """
    if resistor1_unit == "kohm":
        resistor1 *= 1000  # Converte para ohms
    if resistor2_unit == "kohm":
        resistor2 *= 1000  # Converte para ohms
    return round(-(resistor2 / resistor1), 3)

def formatar_labels(valor: float, unidade: str) -> str:
    """
    Formata os valores dos resistores com a unidade correta.
    """
    if unidade == "kohm":
        return f"{valor}ΩK"
    return f"{valor}Ω"

ganho = ctk.DoubleVar()  # Variável para armazenar o ganho calculado

# Botão de cálculo
ctk.CTkButton(
    up_bottom,
    text="CALCULAR",
    command=lambda: (
        ganho.set(calcular(r1.get(), r2.get(), r1_unit.get(), r2_unit.get())),
        r1_label.configure(text=formatar_labels(r1.get(), r1_unit.get())),
        r2_label.configure(text=formatar_labels(r2.get(), r2_unit.get())),
    )
).pack(expand=True, fill="both")

# ------------------ Frame inferior (resultados) ------------------
bottom = ctk.CTkFrame(window)
bottom.grid(column=0, row=1, sticky="nsew", padx=20)

# Configuração da grade do frame inferior
bottom.columnconfigure((0, 1, 2), weight=1)  # Três colunas com pesos iguais

# Widgets no frame inferior - Títulos
ctk.CTkLabel(bottom, text="R1").grid(row=0, column=0, sticky="n")
ctk.CTkLabel(bottom, text="R2").grid(row=0, column=1, sticky="n")
ctk.CTkLabel(bottom, text="Ganho").grid(row=0, column=2, sticky="n")

# Widgets no frame inferior - Valores
r1_label = ctk.CTkLabel(bottom, text=formatar_labels(r1.get(), r1_unit.get()), font=("Arial", 16))
r1_label.grid(row=1, column=0, sticky="n")

r2_label = ctk.CTkLabel(bottom, text=formatar_labels(r2.get(), r2_unit.get()), font=("Arial", 16))
r2_label.grid(row=1, column=1, sticky="n")

ctk.CTkLabel(bottom, textvariable=ganho, font=("Arial", 16)).grid(row=1, column=2, sticky="n")

# ------------------ Loop principal ------------------
window.mainloop()
