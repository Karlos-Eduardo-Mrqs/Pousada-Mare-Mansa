from dataclasses import dataclass
from quarto import Quarto
from cliente import Cliente
from datetime import date
@dataclass

class Agendamento:
    id:int
    data_entrada:date
    data_saida:date
    cliente:'Cliente'
    quarto:'Quarto'