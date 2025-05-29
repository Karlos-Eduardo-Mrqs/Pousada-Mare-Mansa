from dataclasses import dataclass
<<<<<<< Updated upstream
<<<<<<< Updated upstream
@dataclass
=======
from tipo import Tipo
>>>>>>> Stashed changes

@dataclass
class Quarto:
<<<<<<< Updated upstream
    numero_quarto:int
    disponibilidade:bool
    capacidade:int
    # tipo: Tipo
=======
    numero_quarto: int
    disponibilidade: bool
    capacidade: int
    tipo: 'Tipo'
>>>>>>> Stashed changes
=======
from tipo import Tipo

@dataclass
class Quarto:
    numero_quarto: int
    disponibilidade: bool
    capacidade: int
    tipo: 'Tipo'
>>>>>>> Stashed changes
