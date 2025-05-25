from dataclasses import dataclass
from tipo import Tipo
@dataclass

class Quarto:
    numero_quarto:int
    disponibilidade:bool
    capacidade:int
    tipo: 'Tipo'