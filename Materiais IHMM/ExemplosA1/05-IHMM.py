"""
- Introdução a Classes -
Demonstração de objetos que representam componentes eletrônicos
"""

class Resistor:
    def __init__(self, resistencia:float, tolerancia:float):
        self.resistencia = resistencia
        self.tolerancia = tolerancia
    
    def info(self): 
        return f"Resistor: {self.resistencia}R +- {self.tolerancia}%"

    
    def __add__(self, other:"Resistor"):
        return self.resistencia + other.resistencia

    def __mul__(self, other:"Resistor"):
        return round(1 / ( (1/self.resistencia) + (1/other.resistencia)), 4)


class Capacitor:
    def __init__(self, capacitancia:float, tensao_maxima:float):
        self.capacitancia = capacitancia
        self.tensao_maxima = tensao_maxima
	
    def info(self):
        return (f"Capacitor: {self.capacitancia}F, " + 
        f"Tensão Máxima: {self.tensao_maxima}V")
    

r1 = Resistor(150, 5)
r2 = Resistor(220, 5)
c1 = Capacitor(220, 5)
c2 = Capacitor(330, 5)

print(f"R1 - {r1.info()}")
print(f"R2 - {r2.info()}")
print(f"C1 - {c1.info()}")
print(f"C2 - Capacitor: {c2.capacitancia}F, Tensão Máxima: {c2.tensao_maxima}V")

print(f"Resistores em Série: {r1+r2}R")
print(f"Resistores em Paralelo: {r1*r2}R")