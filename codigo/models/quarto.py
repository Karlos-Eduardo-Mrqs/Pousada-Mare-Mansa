from dataclasses import dataclass

@dataclass
class Quarto:
    def __init__(self, numero_quarto:int, disponibilidade:bool, capacidade:int, tipo:int):    
        self.numero_quarto = numero_quarto
        self.disponibilidade = disponibilidade
        self.capacidade = capacidade
        self.tipo = tipo