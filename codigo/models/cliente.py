from dataclasses import dataclass

@dataclass
class Cliente:
    def __init__(self, cpf:str, nome:str, email:str,):    
        self.cpf = cpf
        self.nome = nome    
        self.email = email