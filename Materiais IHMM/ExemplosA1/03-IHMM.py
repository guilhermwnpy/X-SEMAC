"""
- Demonstração AmpOp -
Inteface da "Calculadora Amplificador Operacional"
usando Tkinter e em formato Script
"""

import os
import tkinter as tk
from tkinter import ttk

# Limpa o terminal ao iniciar o programa
os.system("cls")

# Configuração da janela principal
window = tk.Tk()
window.title("Calculadora Amplificador Operacional")  # Título da janela
window.geometry("600x250")  # Dimensões da janela
window.resizable(0, 0)  # Desabilita redimensionamento da janela

# Configuração de layout da janela principal
window.columnconfigure(0, weight=1)  # Única coluna, preenchendo uniformemente
window.rowconfigure(0, weight=3)  # Uma linha com peso 3
window.rowconfigure(1, weight=1)  # Uma linha com pesos 1

# ------------------ Frame superior (entrada de dados) ------------------
up = ttk.Frame(window)
up.grid(column=0, row=0, sticky="nsew", padx=20)  # Padding lateral

# Configuração da grade do frame superior
up.columnconfigure((0, 1), weight=1)  # Duas colunas com pesos iguais
up.rowconfigure((0, 1), weight=1)  # Duas linhas com pesos iguais

# Sub-frame superior esquerdo (dados do resistor 1)
up_left = ttk.Frame(up)
up_left.grid(column=0, row=0, sticky="nsew")  # Primeira coluna do frame superior

r1 = tk.DoubleVar(value=1)  # Valor inicial de R1
r1_unit = tk.StringVar(value="ohm")  # Unidade inicial de R1

# Widgets no sub-frame superior esquerdo
ttk.Label(up_left, text="Valor do resistor 1").pack()  # Rótulo do resistor 1
ttk.Entry(up_left,textvariable=r1).pack()  # Entry para valor de R1
ttk.Label(up_left, text="Unidade do resistor 1").pack()  # Rótulo da unidade
ttk.Combobox(up_left, values=["ohm", "kohm"], textvariable=r1_unit).pack()  # Combobox para unidade

# Sub-frame superior direito (dados do resistor 2)
up_right = ttk.Frame(up)
up_right.grid(column=1, row=0, sticky="nsew")  # Segunda coluna do frame superior

r2 = tk.DoubleVar(value=0)  # Valor inicial de R2
r2_unit = tk.StringVar(value="ohm")  # Unidade inicial de R2

# Widgets no sub-frame superior direito
ttk.Label(up_right, text="Valor do resistor 2").pack()  # Rótulo do resistor 2
ttk.Entry(up_right, textvariable=r2).pack()  # Entry para valor de R2
ttk.Label(up_right, text="Unidade do resistor 2").pack()  # Rótulo da unidade
ttk.Combobox(up_right, values=["ohm", "kohm"], textvariable=r2_unit).pack()  # Combobox para unidade

# Sub-frame inferior do frame superior (botão de cálculo)
up_bottom = ttk.Frame(up)
up_bottom.grid(column=0, row=1, columnspan=2, sticky="nsew")  # Ocupa ambas as colunas

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

ganho = tk.DoubleVar()  # Variável para armazenar o ganho calculado

# Botão de cálculo
ttk.Button(
    up_bottom,
    text="CALCULAR",
    command=lambda: (
        ganho.set(calcular(r1.get(), r2.get(), r1_unit.get(), r2_unit.get())),
        r1_label.config(text=formatar_labels(r1.get(), r1_unit.get())),
        r2_label.config(text=formatar_labels(r2.get(), r2_unit.get())),
    )
).pack(expand=True, fill="both")  # Botão centralizado e preenchendo o espaço

# ------------------ Frame inferior (resultados) ------------------
bottom = ttk.Frame(window)
bottom.grid(column=0, row=1, sticky="nsew", padx=20)  # Padding lateral

# Configuração da grade do frame inferior
bottom.columnconfigure((0, 1, 2), weight=1)  # Três colunas com pesos iguais

# Widgets no frame inferior - Títulos
ttk.Label(bottom, text="R1").grid(row=0, column=0, sticky="n")  # Título da coluna R1
ttk.Label(bottom, text="R2").grid(row=0, column=1, sticky="n")  # Título da coluna R2
ttk.Label(bottom, text="Ganho").grid(row=0, column=2, sticky="n")  # Título da coluna Ganho

# Widgets no frame inferior - Valores
r1_label = ttk.Label(bottom, text=formatar_labels(r1.get(), r1_unit.get()), font=("Arial", 16))
r1_label.grid(row=1, column=0, sticky="n")  # Valor de R1

r2_label = ttk.Label(bottom, text=formatar_labels(r2.get(), r2_unit.get()), font=("Arial", 16))
r2_label.grid(row=1, column=1, sticky="n")  # Valor de R2

ttk.Label(bottom, textvariable=ganho, font=("Arial", 16)).grid(row=1, column=2, sticky="n")  # Valor do ganho

# ------------------ Loop principal ------------------
window.mainloop()
