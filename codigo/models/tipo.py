from dataclasses import dataclass
from quarto import Quarto
@dataclass

class Tipo:
    id:int
    quarto:'Quarto'
    nome:str
    preco:float