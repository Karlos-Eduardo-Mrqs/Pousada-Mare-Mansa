from datetime import date
from quarto import Quarto
from cliente import Cliente
from dataclasses import dataclass

@dataclass
class Agendamento:
    def __init__(self, id:int, data_entrada:date, data_saida:date,cliente:Cliente, quarto:Quarto):    
        self.id = id
        self.data_entrada = data_entrada
        self.data_saida = data_saida
        self.cliente = cliente
        self.quarto = quarto